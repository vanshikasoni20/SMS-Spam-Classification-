import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

#Loading the saved vectorizer and naive model
tfidf=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))

# Transform_text Function for text preprocessing
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string

nltk.download('stopwords')

ps=PorterStemmer()

def transform_text(text):
    text=text.lower() #converting to lowercase
    text=nltk.word_tokenize(text) #tokenize

    #removing special characters and retaining alphanumeric words
    text=[word for word in text if word.isalnum()]
    
    #removing stopwords and punctuation
    text=[word for word in text if word not in stopwords.words('english') and word not in            string.punctuation]

    #Applying Stemming
    text = [ps.stem(word) for word in text]

    return " ".join(text)

#streamlit code
st.title("SMS Spam Classifier")
input_sms=st.text_area("Enter message")

if st.button('Predict'):
    #preprocess the input message
    transformed_sms=transform_text(input_sms)
    #vectorize the preprocessed message
    transformed_sms_tfidf=tfidf.transform([transformed_sms])
    #predict 
    result=model.predict(transformed_sms_tfidf)[0]
    #Display the result
    if result==1:
        st.header("Spam")
    else:
        st.header("Not Spam")