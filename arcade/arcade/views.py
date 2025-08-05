from django.shortcuts import render

def custom_swagger_ui_view(request):
    return render(request, "drf_spectacular/custom_swagger.html")
