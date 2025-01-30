from django.http import JsonResponse
from datetime import datetime

def get_info(request):
    response_data = {
            "email":"mohaomar495@gmail.com",
            "current_datetime": datetime.utcnow().isoformat() + "Z",
            "github_url": "https://github.com/mohaomar495/HNG12-Backend-Task0"
            }
    return JsonResponse(response_data)
