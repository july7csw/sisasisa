from django.http import HttpResponse

class HealthCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == "/ping":
            return HttpResponse("pong")
        response = self.get_response(request)
        return response