from django.http import JsonResponse
from datetime import datetime

def get_info(request):
    response_data = {
            "email":"mohaomar495@gmail.com",
            "current_datetime": datetime.utcnow().isoformat() + "Z",
            "github_url": "https://github.com/mohaomar495/HNG12-BackEnd-Internship/"
            }
    return JsonResponse(response_data)
