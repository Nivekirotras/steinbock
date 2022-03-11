import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.http import MediaFileUpload

# Import to use pydrive fuctions
#from pydrive.auth import GoogleAuth
#gauth = GoogleAuth()
#gauth.LocalWebserverAuth()


# Define google service to use
SCOPES = ['https://www.googleapis.com/auth/drive']
# Defines the path to images
DIRECTORY = '/home/pi/PycharmProjects/Steinbock/Images'
# Defines upload folder destination
DESTINATION_FOLDER = '1K4yqNALknlwFQT8ZTl74-BCIfjDKxNyT'


def uploadImage(file_name):
    """Upload file to google folder in FOLDER.
    """
    #Set up a credentials object I think
    #creds = ServiceAccountCredentials.from_json_keyfile_name('client_secrets.json',
    #                                                         ['https://www.googleapis.com/auth/drive'])
    creds = None
    print("Start cred process")
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        print("Token exists")
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            print("Refresh token")
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)
            print("create new token")
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
            print("New token created")

    #Now build our api object, thing
    drive_api = build('drive', 'v3', credentials=creds)

    print("Uploading file " + file_name + "...")

    #We have to make a request hash to tell the google API what we're giving it
    body = {
        'name': file_name,
        'parents': [DESTINATION_FOLDER]
        }
    
    #Now create the media file upload object and tell it what file to upload, in this case an image
    media = MediaFileUpload(os.path.join(DIRECTORY, file_name), mimetype='image/jpeg')

    #Now we're doing the actual post, creating a new file of the uploaded type
    new_file = drive_api.files().create(body=body, media_body=media).execute()
    
    print("File " + file_name + " uploaded")


# Short upload function but requires log in every time
def uploadImageCredentials(file_name):
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
    service = build('drive', 'v3', credentials=creds)
    file_metadata = {'name': file_name}
    media = MediaFileUpload(os.path.join(DIRECTORY, file_name), mimetype='image/jpeg')
    file = service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
    print('File ID: %s' % file.get('id'))


# Upload image using pydrive (requires authentication every time
def UploadImagePydrive(file_name):
    filepath = os.path.join(DIRECTORY, file_name)
    gfile = drive.CreateFile({'parents': [{'id': FOLDER}], 'title': file_name})
    gfile.SetContentFile(filepath)
    gfile.Upload()
    print(f"I uploaded the file: {file_name}")
    
    