import json
import streamlit as st
import pyperclip

st.set_page_config(layout="wide", page_title="Emoji CheatSheet", page_icon="🌟")

# Load the emoji JSON data
@st.cache_data
def load_emoji_data():
    with open("emoji.json", "r", encoding="utf-8") as f:
        emoji_data = json.load(f)
    return emoji_data

emoji_data = load_emoji_data()

# Function to search for emojis
def search_emoji(search_term):
    return {key: value for key, value in emoji_data.items() if search_term.lower() in key.lower()}


def display_emojis_in_table(emojis):
    keys = list(emojis.keys())  # Get the list of keys
    col_count = min(len(keys), 5)  # Calculate the number of columns
    row_count = (len(keys) + col_count - 1) // col_count  # Calculate the number of rows

    cols = st.columns(col_count)  # Create the columns

    for i, key in enumerate(keys):
        row = i // col_count  # Calculate the current row index
        col = i % col_count  # Calculate the current column index

        with cols[col]:
            st.write(f"{key}: {emojis[key]}")
            copy_button = st.button(key=key, help="Click to copy",  label= "Copy Value")  # Add a copy value button
            if copy_button:
                pyperclip.copy(emojis[key])  # Copy the value to the clipboard
                st.toast('Copied to clipboard!', icon="📋")

        if row < row_count - 1:
            st.write("")  # Add spacing between rows


# Create the Streamlit app
st.title("🌋Emoji CheetSheet : Search & Copy🌋")

search_term = st.sidebar.text_input("Search Emoji")



if search_term:
    searched_emojis = search_emoji(search_term)
    display_emojis_in_table(searched_emojis)

else:
    display_emojis_in_table(emoji_data)

