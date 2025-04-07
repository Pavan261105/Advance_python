import segno as ss

qrcode = ss.make_qr(997942610)
qrcode.save(
    "wide_border_qrcode.png",
    scale=10,
    border=5
)


qrcode = ss.make_qr("www.linkedin.com/in/pavanmehta-developer")
qrcode.save("LinkedIn.png",scale=10,border=5)