from django.shortcuts import render
import requests

def home(request):
    data = None

    if request.method == "POST":
        country = request.POST.get('country')
        try:
            response = requests.get(
                f'https://restcountries.com/v3.1/name/{country}?fullText=true'
            )
            response.raise_for_status()
            data = response.json()[0]
        except:
            data = None

    return render(request, 'home.html', {'data': data})
