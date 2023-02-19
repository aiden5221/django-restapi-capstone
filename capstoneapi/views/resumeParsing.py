from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..services import resumeParse

@api_view(['POST'])
def getResume(request):
    file = request.FILES['file'].read()
    data = resumeParse.getData(file)
    
    return Response(status=status.HTTP_200_OK)