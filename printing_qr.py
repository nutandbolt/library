import qrcode
from PIL import Image

# =========================
# PRINT SETTINGS
# =========================
DPI = 300
MM_TO_INCH = 1 / 25.4


def mm_to_px(mm):
    return int(mm * MM_TO_INCH * DPI)

# =========================
# PAGE SIZE (A4)
# =========================
PAGE_WIDTH_PX  = mm_to_px(210)
PAGE_HEIGHT_PX = mm_to_px(297)

# =========================
# MARGINS (mm)
# =========================
LEFT_MARGIN_PX   = mm_to_px(9)
RIGHT_MARGIN_PX  = mm_to_px(8)
TOP_MARGIN_PX    = mm_to_px(13)
BOTTOM_MARGIN_PX = mm_to_px(13)

# =========================
# GRID LAYOUT
# =========================
COLS = 3
ROWS = 8
ROW_GAP_PX = mm_to_px(2)

# =========================
# COMPUTE LABEL SIZE
# =========================
AVAILABLE_WIDTH_PX = PAGE_WIDTH_PX - LEFT_MARGIN_PX - RIGHT_MARGIN_PX
AVAILABLE_HEIGHT_PX = PAGE_HEIGHT_PX - TOP_MARGIN_PX - BOTTOM_MARGIN_PX

LABEL_WIDTH_PX = AVAILABLE_WIDTH_PX // COLS
LABEL_HEIGHT_PX = (AVAILABLE_HEIGHT_PX - (ROWS - 1) * ROW_GAP_PX) // ROWS

# =========================
# QR CODE SIZE
# =========================
QR_SIZE_PX = mm_to_px(24)


# =========================
# QR GENERATOR FUNCTION
# =========================
def generate_qr(data, size_px):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=2
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    img = img.resize((size_px, size_px), Image.LANCZOS)
    return img


# =========================
# CREATE A4 SHEET
# =========================
sheet = Image.new("RGB", (PAGE_WIDTH_PX, PAGE_HEIGHT_PX), "white")

# Example QR data (replace with real values)
qr_data_list_1 = [f"https://atmslibrary.streamlit.app/?book_id=BOOK_00{i}" for i in range(1, 10)]
qr_data_list_2 = [f"https://atmslibrary.streamlit.app/?book_id=BOOK_00{i}" for i in range(10, 25)]
qr_data_list = qr_data_list_1 + qr_data_list_2

# =========================
# PLACE QR CODES
# =========================
index = 0
for row in range(ROWS):
    for col in range(COLS):
        if index >= len(qr_data_list):
            break

        qr_img = generate_qr(qr_data_list[index], QR_SIZE_PX)

        x_label = LEFT_MARGIN_PX + col * LABEL_WIDTH_PX
        y_label = TOP_MARGIN_PX + row * (LABEL_HEIGHT_PX + ROW_GAP_PX)

        x_qr = x_label + (LABEL_WIDTH_PX - QR_SIZE_PX) // 2
        y_qr = y_label + (LABEL_HEIGHT_PX - QR_SIZE_PX) // 2

        sheet.paste(qr_img, (x_qr, y_qr))
        index += 1

# =========================
# SAVE FOR PRINTING
# =========================
sheet.save("qr_labels_a4.png", dpi=(DPI, DPI))
print("Saved: qr_labels_a4.png")
