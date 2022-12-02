from ..models import PotentialEmployee
from ..serializer import PotentialEmployeeSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def potentialEmployee_list(request):
    
    if request.method == 'GET':
        # get all potential employees
        potentialEmployees = PotentialEmployee.objects.all()
        # serialize them
        serializer = PotentialEmployeeSerializer(potentialEmployees, many=True)
        # return json
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PotentialEmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def potentialEmployee_detail(request, id):

    # Get the specific job application to work with and return 404 if not found
    try:
        potentialEmployee = PotentialEmployee.objects.get(pk=id)
    except PotentialEmployee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PotentialEmployeeSerializer(potentialEmployee)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PotentialEmployeeSerializer(potentialEmployee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        potentialEmployee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)