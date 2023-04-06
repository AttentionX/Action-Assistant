import io
from google.cloud import vision
from google.oauth2 import service_account

class customClient:
    def __init__(self):
        # Change this to the correct path
        credentials = service_account.Credentials.from_service_account_file('/path/to/service_account.json')
        self.client = vision.ImageAnnotatorClient(credentials=credentials)

    # Return OCR Texts from Google Vision API
    def getOCR(self, image_path):
        """Returns the OCR text from the given image."""
        client = self.client
        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()
        image = vision.Image(content=content)
        response = client.document_text_detection(image=image)
        texts = response.full_text_annotation.text
        return texts
    
    