import smtplib

def send_email (content, to_addr):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("earthosprey81@gmail.com", "password")
    server.sendmail("earthosprey81@gmail.com", to_addr, content)
    server.quit()
