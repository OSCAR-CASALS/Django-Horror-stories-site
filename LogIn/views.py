from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from SearchAndReadApp.models import Story, Opinion
from django.utils import timezone

# Create your views here.
def LogIn(request):
    ncorrect = ''
    if request.method == "POST":
        user = authenticate(username = request.POST['UserName'], password = request.POST['PassWord'])
        if user is not None:
            login(request, user)
        ncorrect='Username or password is incorrect.'
    if request.user.is_authenticated:
        if request.GET.get('LoggedOut') != '':
            LikedStories = Opinion.objects.filter(username=request.user.username).filter(liked=1)
            publishedStories = Story.objects.filter(title_and_user__contains=request.user.username)
            PublishedStoriesDef = []
            for tit in publishedStories:
                if tit.title_and_user.split(' by ')[-1] == request.user.username:
                    PublishedStoriesDef.append(tit)
            titles = set()
            for story in LikedStories:
                titles.add(story.st.title_and_user)
            return render(request, 'UserPage.html', {'FirstName': request.user.first_name, 'LastName': request.user.last_name, 'likedStories': titles, 'PublishedStories': PublishedStoriesDef})
    logout(request)
    
    return render(request, 'LogInPage.html', {'IncMessage': ncorrect})

def PublishStory(request):
    return render(request, 'PublishPage.html')

def publishedStory(request):
    Title = '"' + request.POST['title'] + '"' + ' by ' + request.user.username 
    newstory = Story(title_and_user = Title, story = request.POST['StoryToPublish'], pub_date = timezone.now())
    newstory.save()
    return render(request, 'StoryPublished.html', {'Title': request.POST['title']})