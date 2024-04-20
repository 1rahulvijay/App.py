import sys
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import getpass


class DataProcessor:
    def process_data(self):
        logging.debug("Debug message")
        logging.info("Info message")
        logging.warning("Warning message")
        logging.error("Error message")
        logging.critical("Critical message")
        result = 1 / 0  # This will raise a ZeroDivisionError
        return result


class ExceptionHandler:
    def handle_exception(self, error):
        logging.error("An error occurred: %s", error)
        EmailSender().send_email("Error occurred", str(error))
        sys.exit(1)


class EmailSender:
    def send_email(self, subject, message):
        # Your email sending logic here
        sender_email = "rahulvijayvargiya@outlook.com"
        receiver_email = "rahulvijay464@gmail.com"
        password = getpass.getpass()

        # Create message object
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject

        # Attach message body
        msg.attach(MIMEText(message, "plain"))

        # Attach error log file
        filename = "error.log"
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        msg.attach(part)

        # Connect to SMTP server and send email
        server = smtplib.SMTP("smtp.office365.com", 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()


# Main program
def main():
    try:
        data_processor = DataProcessor()
        result = data_processor.process_data()
        print("Result:", result)
    except Exception as e:
        ExceptionHandler().handle_exception(e)


if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(filename="error.log", level=logging.ERROR)

    # Run the main program
    main()
