import streamlit as st
from sheets_db import get_book, update_checkout, update_return

st.set_page_config(page_title="Library Book", layout="centered")

book_id = st.query_params.get("book_id")

if not book_id:
    st.warning("Scan the QR code on a book.")
    st.stop()

book = get_book(book_id)

if not book:
    st.error("Book not found.")
    st.stop()

st.subheader(book["title"])
st.write(f"**Author:** {book['author']}")
st.info(f"**Status:** {book['status']}")

if book["status"] == "Checked Out":
    st.write(f"**Checked out by:** {book['name']}")

st.divider()

# --- Checkout ---
if book["status"] == "Available":
    name = st.text_input("Enter your name")

    if st.button("✅ Check Out"):
        if name.strip() == "":
            st.warning("Please enter your name.")
        else:
            update_checkout(book_id, name)
            st.success("Book checked out successfully.")
            st.rerun()

# --- Return ---
else:
    if st.button("🔁 Return"):
        update_return(book_id)
        st.success("Book returned.")
        st.rerun()

st.divider()

# Link to status page
st.page_link("pages/status.py", label="📋 View All Books Status")
