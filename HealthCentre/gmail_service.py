# import os
# import pickle
# import base64
# from email.mime.text import MIMEText
# from google.auth.transport.requests import Request
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build

# SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# def get_gmail_service():
#     creds = None
#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             creds = pickle.load(token)
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)
#     service = build('gmail', 'v1', credentials=creds)
#     return service

# def send_email(subject, message_text, to):
#     service = get_gmail_service()
#     message = MIMEText(message_text)
#     message['to'] = to
#     message['from'] = 'your-email@gmail.com'
#     message['subject'] = subject
#     raw = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
#     body = {'raw': raw}
#     try:
#         message = service.users().messages().send(userId='me', body=body).execute()
#         print('Message Id: %s' % message['id'])
#         return message
#     except Exception as e:
#         print(f'An error occurred: {e}')
#         return None