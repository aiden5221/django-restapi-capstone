from pyresparser import ResumeParser
import spacy
from collections.abc import Iterable
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os
spacy.load('en_core_web_sm')
def getData(file_content):
    # Pass the text to the ResumeParser method
    path = default_storage.save('tmp/' + file_content.name, ContentFile(file_content.read()))
    tmpFile = os.path.join(settings.MEDIA_ROOT, path)
    data = ResumeParser(tmpFile).get_extracted_data()
    os.remove(tmpFile)
    name = data['name']
    email = data['email']
    mobile = data['mobile_number']
    skills = ",".join(data['skills'])
    parsedData = {"name":name,"email":email,"mobile":mobile,"skills":skills}
    
    return parsedData