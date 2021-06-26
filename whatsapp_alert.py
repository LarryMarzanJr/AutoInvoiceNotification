import pywhatkit

# set array of phone numbers (test)
phone_numbers = ['+6281242181136','+6285398916361','+6282196660447',]

for number in phone_numbers:
    pywhatkit.sendwhatmsg_instantly(number, "[Testing WhatsApp Auto Send] to the MOOOON")