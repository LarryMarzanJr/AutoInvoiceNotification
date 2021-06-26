import smtplib
from email.message import EmailMessage
import sqlite3

#define variables
def email_alert(subject, body, to):
    user = "your@email.com"
    password = "yourpassword"

    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = user
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

# using sqlite3 connection to customer.db database
# koneksi = sqlite3.connect('customer.db')
# c = koneksi.cursor()
# c.execute("SELECT email FROM customer")
# emails = c.fetchall()

# example for email database
emails = ['customer1@email.com', 'customer2@email.com']

# loop sending email based on customer database
for email in emails:
    if __name__ == '__main__':
        # writing email_alert(subject, body, to)
        email_alert(
            "e-Billing JR-Network",
            """Yang Terhormat Bapak/Ibu _____,

Terima kasih atas kepercayaan Bapak/Ibu pada layanan Internet kami.

Bersama ini kami sampaikan tagihan internet periode bulan _____
Sebesar Rp 200.000,-

Untuk tata cara pembayaran dapat dilakukan dengan beberapa alternatif:
- Pembayaran Tunai
- Pembayaran lewat rekening Bank BTPN 901241230 LARRY BENEDICTO MARZAN JR
- Pembayaran lewat rekening Bank BCA 1700369818 LARRY BENEDICTO MARZAN JR
- Pembayaran lewat Wallet OVO 081242181136
- Pembayaran lewat Wallet DogeCoin DDbrgbjBj6yu3ZurHADthwaJDsxguHafLM

Demikian kami sampaikan. Terima kasih atas partisipasi Anda dalam mendukung program JR-NETWORK Go Green melalui e-billing.
            """,
            email
            )