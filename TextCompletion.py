from transformers import pipeline, set_seed
import torch
def chatForNRounds(n=20):
    generator = pipeline('text-generation', model='gpt2')
    for chatForNRounds in range(n):
        inputFromUser = input("\nYou: ")
        output = generator(inputFromUser,max_length=30, num_return_sequences =1)
        print("model: ",output)

if __name__== "__main__":
    chatForNRounds(n=20)