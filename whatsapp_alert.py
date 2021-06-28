import pywhatkit
import sqlite3

# using sqlite3 connection to customer.db database
koneksi = sqlite3.connect('customer.db')
c = koneksi.cursor()
c.execute("SELECT nama,billing_month,billing_year,tagihan,mobile_phone FROM customer WHERE sent=0")
customers = c.fetchall()

# set array of phone numbers (test)
# phone_numbers = ['+6287846644887','+6285398916361','+6282196660447',]

# Looping 'For' Statement
for customer_data in customers:
    # pywhatkit.sendwhatmsg_instantly('phoneNumber', 'message', waitTimeInMinutes, tab_close=True/False)
    pywhatkit.sendwhatmsg_instantly(
        customer_data[4],
        """Yang Terhormat Bapak/Ibu {},

Terima kasih atas kepercayaan Bapak/Ibu pada layanan Internet kami.
Bersama ini kami sampaikan tagihan internet periode bulan {} {} sebesar Rp {},-

Untuk tata cara pembayaran dapat dilakukan dengan beberapa alternatif:
- Pembayaran Tunai
- Pembayaran lewat rekening Bank BTPN 901241230 LARRY BENEDICTO MARZAN JR
- Pembayaran lewat rekening Bank BCA 1700369818 LARRY BENEDICTO MARZAN JR
- Pembayaran lewat Wallet OVO 081242181136
- Pembayaran lewat Wallet DogeCoin DDbrgbjBj6yu3ZurHADthwaJDsxguHafLM

Demikian kami sampaikan. Terima kasih atas partisipasi Anda dalam mendukung program JR-NETWORK Go Green melalui e-billing.
    """.format(customer_data[0], customer_data[1], customer_data[2], customer_data[3]),
    20,
    tab_close=True)