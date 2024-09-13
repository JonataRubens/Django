from django.shortcuts import render

# View para a página inicial (home)
def home(request):
    return render(request, 'home.html')