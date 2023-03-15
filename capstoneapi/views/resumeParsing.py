from rest_framework.decorators import api_view
from django.http import JsonResponse
from ..services import resumeParse

@api_view(['POST'])
def getResume(request):
    if request.method == 'POST':
        resume_file = request.FILES.get('resume_parse')
        if resume_file:
            data = resumeParse.getData(resume_file)
            return JsonResponse(data,status=201,safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'},status=400)
