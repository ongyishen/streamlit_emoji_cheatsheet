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
    # check the count of emojis if zero then display Record Not Found and return
    if len(emojis) == 0:
        st.error("Record Not Found")
        return

    keys = list(emojis.keys())  # Get the list of keys
    col_count = min(len(keys), 5)  # Calculate the number of columns
    # Calculate the number of rows
    row_count = (len(keys) + col_count - 1) // col_count

    cols = st.columns(col_count)  # Create the columns

    for i, key in enumerate(keys):
        row = i // col_count  # Calculate the current row index
        col = i % col_count  # Calculate the current column index

        with cols[col]:
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"{key}:")
            with col2:
                # Add a copy value button
                st.code(emojis[key])

        if row < row_count - 1:
            st.write("")  # Add spacing between rows


# Create the Streamlit app
st.title("🌋Emoji CheatSheet : Search & Copy🌋")

search_term = st.sidebar.text_input("Search Emoji")


if search_term:
    searched_emojis = search_emoji(search_term)
    display_emojis_in_table(searched_emojis)

else:
    display_emojis_in_table(emoji_data)
