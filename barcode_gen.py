import qrcode
from PIL import Image

for i in range(1,25):
    print(i)
    url = f"https://atmslibrary.streamlit.app/?book_id=BOOK_00{i}"
    print(url)
    img = qrcode.make(url)
    img.save(rf"/Users/Ajay/PycharmProjects/barcode_scanner/barcodes/BOOK_00{i}.png")
