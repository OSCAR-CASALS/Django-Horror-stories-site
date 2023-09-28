from django.shortcuts import render
from .models import Story, Opinion

# Create your views here.
def home(request):
    return render(request, 'home.html')

def SearchRes(request):
    query = request.GET.get('searchbox')
    result = Story.objects.filter(title_and_user__icontains=query)
    return render(request, 'results.html', {'query' : query, 'matches' : result})

def ReadStory(request):
    title = request.GET.get('SelectedStory')
    final_res = Story.objects.get(pk=title)
    LogInMessage = ''
    user = final_res.title_and_user.split(' by ')[-1].strip()
    if request.user.is_authenticated:
        if request.user.username != user:
            if request.GET.get('LikeButton') == 'YES' and Opinion.objects.filter(st=final_res).filter(username=request.user.username).filter(liked=1).count() == 0:
                if Opinion.objects.filter(st=final_res).filter(username=request.user.username).count() > 0:
                    op = Opinion.objects.filter(st=final_res).get(username=request.user.username)
                    op.liked=1
                    final_res.dislikes -= 1
                else:
                    op = Opinion(st=final_res, username=request.user.username, liked = 1)
                op.save()
                final_res.likes += 1
                final_res.save()
            elif request.GET.get('DisLikeButton') == 'YES' and Opinion.objects.filter(st=final_res).filter(username=request.user.username).filter(liked=-1).count() == 0:
                if Opinion.objects.filter(st=final_res).filter(username=request.user.username).count() > 0:
                    op = Opinion.objects.filter(st=final_res).get(username=request.user.username)
                    op.liked=-1
                    final_res.likes -= 1
                else:
                    op = Opinion(st=final_res, username=request.user.username, liked = -1)
                op.save()
                final_res.dislikes += 1
                final_res.save()
        elif request.GET.get('LikeButton') == 'YES' or request.GET.get('DisLikeButton') == 'YES':
            LogInMessage = 'The person who published the story can not liked it or disliked it.'
    elif request.GET.get('LikeButton') == 'YES' or request.GET.get('DisLikeButton') == 'YES':
        LogInMessage = 'You must log in to like or dislike.'
        
    return render(request, 'ReadStories.html', {'final' : final_res, 'user': user, 'LoginMessage': LogInMessage})