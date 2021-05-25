from django.shortcuts import render
class SiteUnderConstruction:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = render(request, 'main/siteuc.html')
        return response

    def process_exception(self, request, exception):
        print("Exception Occured...")
        msg = exception
        return HttpResponse(msg)
