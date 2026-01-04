import qrcode

url = "http://localhost:8501/?book_id=BOOK_001"
img = qrcode.make(url)
img.save("BOOK_001.png")
