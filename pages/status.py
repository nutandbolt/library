import streamlit as st
from sheets_db import get_all_books
import pandas as pd

st.set_page_config(page_title="Library Status", layout="wide")

st.title("📚 Library – Current Book Status")

books = get_all_books()

df = pd.DataFrame(books)

# Reorder columns nicely
df = df[["book_id", "title", "author", "name", "status", "last_updated"]]

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)
