from pyresparser import ResumeParser
import spacy
from collections.abc import Iterable
spacy.load('en_core_web_sm')


directory = 'Resume'
header = ['Name', 'Number', 'Email', 'Skills', 'Experience']

parsedData = []
count = 1
arrNames = []
arrEmails = []
arrNumber = []
arrSkills = []
arrExperience = []
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if f.endswith(".pdf"):
        data = ResumeParser(f)
        data = data.get_extracted_data()
        arrNames.append(data['name'])
        arrEmails.append(data['email'])
        arrNumber.append(data['mobile_number'])
        arrSkills.append(",".join(data['skills']))
        
        if type(data['experience']) == str:
            arrExperience.append(data['experience'])
        elif isinstance(data['experience'], Iterable):
            arrExperience.append(",".join(data['experience']))
        else:
            # Handle other cases as necessary
            pass

print("Resumes Successfully Parsed")

