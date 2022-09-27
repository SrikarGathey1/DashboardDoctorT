import smtplib, ssl
from random import randint

def otpMessage(reciever):

    otp = randint(100000, 999999)

    port = 465
    password = "fbqzdsujolwqhutv"
    email = "doctortdonotreply@gmail.com"
    message = "Your OTP for email ID verification is " + str(otp) + ". Please enter this OTP where prompted."

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
        server.login(email, password)
        server.sendmail(email, reciever, message)

    return otp

print(otpMessage("venkatnaras123@gmail.com"))

