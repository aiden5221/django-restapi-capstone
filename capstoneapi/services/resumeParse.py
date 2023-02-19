from pyresparser import ResumeParser
import spacy
from collections.abc import Iterable

spacy.load('en_core_web_sm')

def getData(f):
    print(type(f))
    data = ResumeParser(f)
    data = data.get_extracted_data()
    name = data['name']
    email = data['email']
    number = data['number']
    skills = ",".join(data['skills'])
    if type(data['experience']) == str:
        experience = data['experience']
    elif isinstance(data['experience'], Iterable):
        experience = ",".join(data['experience'])
    else:
        # Handle other cases as necessary
        pass
    return [name,email,number,skills]