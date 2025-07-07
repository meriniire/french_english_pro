import streamlit as st
from deep_translator import GoogleTranslator
import random

# Expanded vocabulary
vocabulary = {
    "Bonjour": "Hello",
    "Merci": "Thank you",
    "S'il vous plaît": "Please",
    "Au revoir": "Goodbye",
    "Chat": "Cat",
    "Chien": "Dog",
    "Pomme": "Apple",
    "Banane": "Banana",
    "Voiture": "Car",
    "Maison": "House",
    "Livre": "Book",
    "Fleur": "Flower",
    "École": "School",
    "Jardin": "Garden",
    "Oiseau": "Bird",
    "Soleil": "Sun",
    "Lune": "Moon"
}

# Function to get a random word
def get_word_of_the_day():
    french_word = random.choice(list(vocabulary.keys()))
    english_word = vocabulary[french_word]
    return french_word, english_word

# Set page configuration
st.set_page_config(page_title=".development of an App that translate french language to English language for primary school students", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    body {
        background-color: #f9f9f9;
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .header {
        background-color: #ffcc00;
        color: #333;
        padding: 20px;
        text-align: center;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .stButton {
        background-color: #ffcc00;
        color: #333;
        border-radius: 5px;
    }
    .stButton:hover {
        background-color: #e6b800;
    }
    .stTextArea {
        border-radius: 5px;
        border: 1px solid #ccc;
    }
    h1, h2 {
        font-family: 'Arial', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# Main App
def main():
    st.markdown("<div class='header'><h1>French to English Translator</h1></div>", unsafe_allow_html=True)
    
    # Word of the Day
    french_word, english_word = get_word_of_the_day()
    st.subheader("Word of the Day")
    st.write(f"**French**: {french_word}  |  **English**: {english_word}")

    # Flashcard feature
    if st.button("Show Flashcard"):
        st.image("https://via.placeholder.com/150", caption=french_word)  # Placeholder for images
        st.write(f"**English Translation**: {english_word}")

    st.subheader("Enter French Text Below:")
    french_text = st.text_area("French Text", "", height=150)

    if st.button("Translate"):
        if french_text:
            # Translate the text
            translated_text = GoogleTranslator(source='fr', target='en').translate(french_text)
            st.subheader("Translated Text:")
            st.write(translated_text)
        else:
            st.warning("Please enter some text to translate.")

    # Simple Quiz
    st.subheader("Quiz: What is the English translation?")
    quiz_question = random.choice(list(vocabulary.items()))
    answer = st.text_input(f"What is '{quiz_question[0]}' in English?")
    
    if st.button("Check Answer"):
        if answer.lower() == quiz_question[1].lower():
            st.success("Correct! 🎉")
        else:
            st.error(f"Oops! The correct answer is '{quiz_question[1]}'.")

    # Daily Challenge
    st.subheader("Daily Challenge")
    challenge_word = random.choice(list(vocabulary.keys()))
    st.write(f"Translate this word: **{challenge_word}**")

    # Additional Vocabulary Learning Section
    st.subheader("Explore More Vocabulary")
    for french, english in vocabulary.items():
        st.write(f"**French**: {french}  |  **English**: {english}")

# Run the app
if __name__ == "__main__":
    main()
