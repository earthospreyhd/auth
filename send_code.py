from email import send_email
from authlib import gen_code
from custom_errors import EmailError

def send_code(email, pin, devid):
    code = gen_code(email, devid)
    
    try:
        send_email(code, email)
    except Exception:
        raise EmailError("an error has occurred while sending the code to the email")
    
    return