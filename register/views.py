from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def IntroduceDataForm(request):
    missingInfo = ''
    if request.method == "POST":
        missingInfo = 'Someone else already has that username'
        if User.objects.filter(username=request.POST['Username']).count() == 0:
            if request.POST['Username'].find(" ") == -1:
                newUser = User.objects.create_user(username=request.POST['Username'], email=request.POST['email'], password=request.POST['Password'], first_name=request.POST['FirstName'], last_name=request.POST['LastName'])
                return render(request, "finished.html", {'Name': newUser.first_name, 'LastName': newUser.last_name, 'UserName': newUser.username})
            missingInfo = 'There can not be any white spaces in username.'
    return render(request, 'RegisterForm.html', {'MissingForm': missingInfo})