# Import necessary libraries
import pandas as pd
import numpy as np
import re
import nltk
import matplotlib.pyplot as plt
import seaborn as sns

from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv('datasets/Tweets.csv')

# Explore the dataset
print("Number of tweets: ", len(df))
print("Number of airlines: ", len(df['airline'].unique()))
print("Number of sentiments: ", len(df['airline_sentiment'].unique()))

# Visualize the sentiment distribution
sns.countplot(x='airline_sentiment', data=df)
plt.show()

# Visualize the sentiment distribution by airline
sns.countplot(x='airline', hue='airline_sentiment', data=df)
plt.show()

# Print the most common reasons for negative sentiment
negative_tweets = df[df['airline_sentiment'] == 'negative']['text']
negative_reasons = negative_tweets.str.extract(r'(\w+)\s+during')
negative_reasons_count = negative_reasons.value_counts()
print(negative_reasons_count.head(10))

# Clean the tweet text
stop_words = set(stopwords.words('english'))
def clean_text(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text) # Remove mentions
    text = re.sub(r'\bhttps?:\/\/\S+|www\.\S+', '', text) # Remove URLs
    text = re.sub(r'[^A-Za-z\s]+', '', text) # Remove non-alphabetic characters
    text = text.lower() # Convert to lowercase
    text = ' '.join([word for word in text.split() if word not in stop_words]) # Remove stop words
    return text

df['text_clean'] = df['text'].apply(lambda x: clean_text(x))

# Split the dataset into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(df['text_clean'], df['airline_sentiment'], test_size=0.2, random_state=42)

# Vectorize the tweet text
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_val_vec = vectorizer.transform(X_val)

# Train a Naive Bayes model
nb = MultinomialNB()
nb.fit(X_train_vec, y_train)

# Make predictions on the validation set
y_val_pred = nb.predict(X_val_vec)

# Evaluate the model accuracy
accuracy = accuracy_score(y_val, y_val_pred)
print("Validation accuracy: ", accuracy)
