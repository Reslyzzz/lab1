from django.http import JsonResponse
from datetime import datetime

def showtime(request):
    current_time = datetime.now()
    return JsonResponse({'time' : current_time})