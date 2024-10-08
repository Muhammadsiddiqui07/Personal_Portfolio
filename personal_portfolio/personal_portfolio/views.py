from django.shortcuts import render 

def index(request):
    skills = ['Html', 'Css', 'JavaScript', 'Bootstrap', 'React.js', 'Python', 'Django']
    params = {'my_skills': skills}  
    return render(request, 'index.html', params)