import imaplib
import email
import os

# IMAP server settings
IMAP_SERVER = 'imap.outlook.com'
EMAIL = 'your_shared_mailbox@example.com'  # Shared mailbox email address
PASSWORD = 'your_password'

# Connect to the IMAP server
mail = imaplib.IMAP4_SSL(IMAP_SERVER)
mail.login(EMAIL, PASSWORD)

# Select the shared mailbox
mail.select('inbox')

# Search for emails from a specific sender
sender_email = 'specific_sender@example.com'
status, email_ids = mail.search(None, f'(FROM "{sender_email}")')

# Loop through the email IDs
for email_id in email_ids[0].split():
    status, data = mail.fetch(email_id, '(RFC822)')
    raw_email = data[0][1]
    msg = email.message_from_bytes(raw_email)

    # Loop through the parts of the email (can be multipart)
    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue

        # Check if the part is an attachment
        filename = part.get_filename()
        if filename:
            # Download the attachment
            with open(filename, 'wb') as f:
                f.write(part.get_payload(decode=True))
                print(f"Attachment '{filename}' downloaded.")

# Logout and close the connection
mail.logout()
