# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.8.10

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /django-resapi

# Setting the work directory
WORKDIR /django-resapi

# Copy the current directory contents into the container at /django-resapi
ADD . /django-resapi



# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Install nltk dependencies
RUN [ "python", "-c", "import nltk; nltk.download('stopwords')"]

# Install spacy dependencies
RUN ["python", "-m" ,"spacy", "download", "en_core_web_sm"]

RUN ["pip", "install" ,"PyPDF2<3.0"]


