from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

#%%
def loadTokenizerModel (modelName="microsoft/DialoGPT-medium"):
    print("loading model")
    tokenizer = AutoTokenizer.from_pretrained(modelName)
    model = AutoModelForCausalLM.from_pretrained(modelName)
    print("finished loading model")
    return tokenizer, model

if __name__== "__main__":
    tokenizer, model = loadTokenizerModel(modelName="microsoft/DialoGPT-medium")
#%%
def readInput(tokenizer):
    myinput = input("You: ")
    inputIDs = tokenizer.encode(myinput + tokenizer.eos_token, return_tensors ='pt')

    return inputIDs

def generateResponse(tokenizer,model):
    inputIDs = readInput(tokenizer)
    chatOutput= model.generate(inputIDs,max_length=1250, pad_token_id=tokenizer.eos_token_id)
    chatOutputText = tokenizer.decode(chatOutput[:,inputIDs.shape[-1]:][0], skip_special_tokens=True)
    print("Model >",chatOutputText)

#generateResponse(tokenizer,model)

#%%
def generateResponseForRoundn(tokenizer,model,chatRound,chatHistory):
    inputIDs = readInput(tokenizer)

    allinputs= None
    if chatRound == 0:
        allinputs = inputIDs
    else:
        allinputs = torch.cat([chatHistory,inputIDs],dim=-1)


    allChatOutputsSoFar= model.generate(allinputs,max_length=1250, pad_token_id=tokenizer.eos_token_id)
    chatOutputText = tokenizer.decode(allChatOutputsSoFar[:,allinputs.shape[-1]:][0], skip_special_tokens=True)
    print("Model >",chatOutputText)
    return allChatOutputsSoFar

def chatForNRounds (n=5):
    tokenizer,model = loadTokenizerModel(modelName="microsoft/DialoGPT-medium")
    chatHistory = None
    for chatRound in range (n):
        chatHistory = generateResponseForRoundn(tokenizer,model,chatRound,chatHistory)

chatForNRounds(n=5)