from django.shortcuts import render

def home(request):
    import json
    import requests

    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=2B134812-E3A0-46FC-BE79-833C3C8082BE")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    return render(request, 'home.html', {'api':api})

def about(request):
    return render(request, 'about.html', {})