import qrcode


def generate_personalized_qr(room_id):
    base_url = "https://www.example.com/"

    personalized_url = base_url + "?room_id=" + str(room_id)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(personalized_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(f"backend/src/qrcode/images/room_{room_id}_qrcode.png")


room_id = 1234
generate_personalized_qr(room_id)
