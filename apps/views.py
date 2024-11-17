from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'apps/index.html')

def About(request):
    return render(request,'apps/about.html')

def Service(request):
    return render(request, 'apps/service.html')

def Project(request):
    return render(request,'apps/project.html')

def Blog(request):
    return render(request,'apps/blog.html')

def Contact(request):
    return render(request,'apps/contact.html')

def Feature(request):
    return render(request,'apps/feature.html')

def Team(request):
    return render(request,'apps/team.html')

def Testimonial(request):
    return render(request,'apps/testimonial.html')


