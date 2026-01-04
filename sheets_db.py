import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

SCOPES = [
        "https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive"
          ]

creds = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=SCOPES
)

client = gspread.authorize(creds)
sheet = client.open("library").worksheet("books")


def get_book(book_id):
    records = sheet.get_all_records()
    for r in records:
        if r["book_id"] == book_id:
            return r
    return None


def update_checkout(book_id, name):
    cell = sheet.find(book_id)
    row = cell.row

    sheet.update(
        f"D{row}:F{row}",
        [[
            name,
            "Checked Out",
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ]]
    )


def update_return(book_id):
    cell = sheet.find(book_id)
    row = cell.row

    sheet.update(
        f"D{row}:F{row}",
        [[
            "",
            "Available",
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ]]
    )


def get_all_books():
    return sheet.get_all_records()


def update_status(book_id, status):
    print(status)
    cell = sheet.find(book_id)
    row = cell.row
    sheet.update(f"D{row}", [[status]])
    sheet.update(f"E{row}", [[datetime.now().strftime("%Y-%m-%d %H:%M:%S")]])
