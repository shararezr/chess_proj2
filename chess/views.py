from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.mail import send_mail
import random



n=random.randint(100000, 999999)
n=str(n)

def home(request):
    return render(request, "chess/home.html")


def login(request):
    try:
        user = User.objects.get(username=request.POST['username'], password=request.POST['password'])
        if user.check == True:
        	return render(request, 'chess/chess_page.html')
        else:
        	return render(request, "chess/home.html", {'error1': "your account is not active"})
    except:
        return render(request, "chess/home.html", {'error2': "NO USER FOUND!!"})


def register(request):
    if (not User.objects.filter(username=request.POST['username']) and not User.objects.filter(
            email=request.POST['email'])):
		
        user = User(username=request.POST['username'].lower(), password=request.POST['password'],key=n,
                    email=request.POST['email'].lower())
        user.save()
 
        send_mail(
            'play chess free!!!',
            'Hi!!' + user.username + 'wellcome to our game!!'+
            'here is your code activation: '+n,
            'zolghadrsharare@gmail.com',
            [user.email]
        )
        return render(request,'chess/active_page.html')

    else:
        return render(request, 'chess/register.html', {'register_error': "username or email already Exists!!"})




def register_page(request):
	return render(request,'chess/register.html')

def active_page(request):
 
	username = request.POST['username']
	key = request.POST['key']
	user1 = User.objects.filter(username=username)
	
	if not user1 :
		return render(request, 'chess/active_page.html', {'activecode_error1': "user is not found!!"})

	user = User.objects.get(username=username)
	tmp_user = user
	tmp_user.check = True
	user.delete()
	tmp_user.save()

	if  tmp_user.key == n:
		return render(request, 'chess/chess_page.html')
		
	else:
		return render(request, 'chess/active_page.html', {'activecode_error2': "your code is wrong!!"})

def chess_page(request):
	return render(request, 'chess/chess_page.html')