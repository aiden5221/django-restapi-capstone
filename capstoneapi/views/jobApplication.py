from ..models import JobApplication
from ..serializer import JobApplicationSerializer
from ..services.shortlist import createShortlist

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def jobApplication_list(request):
    
    if request.method == 'GET':
        # get all job applications
        jobApplications = JobApplication.objects.all()
        # serialize them
        serializer = JobApplicationSerializer(jobApplications, many=True)
        # return json
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = JobApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Response isnt valid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def jobApplication_detail(request, id):
    
    # Get the specific job application to work with and return 404 if not found
    try:
        jobApp = JobApplication.objects.get(pk=id)
    except JobApplication.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = JobApplicationSerializer(jobApp)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = JobApplicationSerializer(jobApp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        jobApp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Endpoint to run shortlist on given jobID
@api_view(['GET'])
def jobApplication_shortlist(request, id, length):

    # Get the specific job application to work with and return 404 if not found
    try:
        jobApp = JobApplication.objects.get(pk=id)
    except JobApplication.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    serializer = JobApplicationSerializer(jobApp)

    shortlist = createShortlist(serializer.data, length)

    return Response(shortlist, status=status.HTTP_200_OK)

@api_view(['GET'])
def jobApplication_listByName(request, name):
    try:
        jobApps = JobApplication.objects.filter(jobName__icontains=name)
    except JobApplication.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = JobApplicationSerializer(jobApps, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)