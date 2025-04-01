from email.message import EmailMessage
import ssl 
import smtplib
import os



def send_email(sender, recipient, subject, text_body, html_body, attachment_path=None):
        
        
    try:
        my_mail = EmailMessage()
        my_mail["From"] = sender
        my_mail["To"] = recipient
        my_mail["subject"] = subject       
        
        
        my_mail.set_content(text_body)
        my_mail.add_alternative(content_manager=html_body, subtype="html")
        
        if attachment_path:
            with open(attachment_path, "rb") as file:
                file_data = file.read()
                file_name = os.path.basename(attachment_path)
                my_mail.add_attachment(content_manager=file_data, maintype="application", subtype="pdf", filename=file_name) 
                
                
        my_mail = ssl.create_default_context()
        with smtplib.SMTP_SSL("_HostType: smtp.gmail.com, port: 465, context=context") as server: # type: ignore
            email_password = os.getenv("EMAIL_PASSWORD")
            if not email_password:
                raise ValueError("Email password not set in environment variables.")
            server.login(sender, email_password)            
            server.sendmail(sender, recipient, my_mail.as_string()) 
            
        print("Email sent successfully.")
        
    except Exception as e:
        print(f'An error occurred: {e}')
        
if __name__ == "__main__":
    EMAIL_SENDER = "desirejoseph278@gmail.com"
    EMAI_RECIPIENT = "yebave5034@pokeline.com"
    SUBJECT = "Welcome to Alfred Computer Institute"
    TEXT_BODY = """
    Congratulations on your new role! Please find attached your offer letter.
    """
        
    HTML_BODY = """
        <html>
            <body>
                <h1 style="color: #4CAF50;">Welcome to Alfred Computer Institute</h1>
                <p>We are thrilled to have you join our team as a secretary.</p>
                <p>
                   Below is an overview ofyour responsbilities and our organization.
                   For further details, please refer to the attached offer letter.
                <p>
                
                <p>
                   Best Regards,<br>
                   <strong>Alfred Computer Institute</strong>
                   
                </p>
            </body>
        </html>
        """
        
    ATTACHMENT_PATH = "offer_letter .pdf" 
    
    send_email(
        EMAIL_SENDER,
        EMAI_RECIPIENT,
        SUBJECT,
        TEXT_BODY,
        HTML_BODY,
        ATTACHMENT_PATH
    )
        
            
            
            