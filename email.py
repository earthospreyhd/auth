import smtplib
EMAIL_ADDRESS = "earthosprey81@gmail.com"
PASSWORD = "password"

def send_email (content, to_addr):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_ADDRESS, PASSWORD)
    server.sendmail(EMAIL_ADDRESS, to_addr, content)
    server.quit()
