import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(new_listings, recipient_email):
    sender_email = 'jorbac04@gmail.com'
    sender_password = 'eovl ptmk tyde dmcb'

    subject = "New Housing Listings Available!"
    body = "Check out the new listings:\n\n" + "\n".join([f"{listing['title']} - {listing['price']}" for listing in new_listings])

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, recipient_email, text)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
