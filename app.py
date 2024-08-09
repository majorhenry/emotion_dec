import streamlit as st
# import pandas as pd
# import numpy as np
# import altair as alt
import re
import joblib
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Preprocess function
def preprocess_text(text):
    text = str(text)
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    tokens = text.split()
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return ' '.join(tokens)

model = joblib.load("model/project_emotion_detection_model.pkl")

_EMOTION_LABELS = {
    '0':'admiration',
    '1':'amusement 😒',
    '2':'anger 😠',
    '3':'annoyance 😠',
    '4':'approval 🤨',
    '5':'caring',
    '6':'confusion',
    '7':'curiosity',
    '8':'desire',
    '9':'disappointment 😞',
    '10':'disapproval 🤨',
    '11':'disgust',
    '12':'embarrassment 😊',
    '13':'excitement',
    '14':'fear 😨',
    '15':'gratitude',
    '16':'grief',
    '17':'joy 😃',
    '18':'love ❤️',
    '19':'nervousness 😰',
    '20':'optimism',
    '21':'pride 😤',
    '22':'realization',
    '23':'relief 😅',
    '24':'remorse',
    '25':'sadness 😢',
    '26':'surprise 😲',
    '27':'neutral 😐',
}


def main():
    st.title("Emotion Detection from Text")
    st.subheader("Using Google goemotion dataset to detect emotion in text")

    with st.form(key='text_form'):
        user_text = st.text_input("Enter text here")
        submit_text = st.form_submit_button(label='Submit')

    if submit_text:
        col1, col2 = st.columns(2)
        new_text = user_text
        new_text_processed = [preprocess_text(new_text)]
        prediction = model.predict(new_text_processed)
        pred_emotion = _EMOTION_LABELS[prediction[0]]
        st.write(f"Predicted emotion: {pred_emotion} and {prediction[0]}")

        with col1:
            st.success("Your Text")
            st.write(user_text)

            st.success("Prediction")
            st.write(f"{prediction}")

        with col2:
            st.success("Prediction Probability")

if __name__ == '__main__':
    main()
