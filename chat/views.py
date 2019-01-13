from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .filters import UserFilter
from .models import ChatRoom, Message
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def signup(request):
    if request.POST:
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not (User.objects.filter(username=username) or
        (User.objects.filter(email=email))):
            User.objects.create_user(username, email, password)
            user = authenticate(username=username, email=email,
                                password=password)
            login(request, user)
            return HttpResponseRedirect('/chat/')
        else:
            return render(request, 'signup.html',
            {'error': 'Looks like username, email, and password already exists.'})
    return render(request, 'signup.html', {'error': ''})


def logIn(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user == None:
            return render(request, 'login.html',
                {'error': 'Invalid Username/Password'})
        else:
            login(request, user)
            return HttpResponseRedirect('/chat/')
    return render(request, 'login.html', {'error': ''})


@login_required
def logOut(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def list_chats(request):
    chat_rooms_sender = ChatRoom.objects.all().filter(sender=request.user)
    chat_rooms_receiver = ChatRoom.objects.all().filter(receiver=request.user)
    return render(request, 'chats_list.html', {'chat_rooms_sender': chat_rooms_sender,
                                               'chat_rooms_receiver': chat_rooms_receiver})


@login_required
def new_chatroom(request):
    user_list = User.objects.all()
    user_filtered = UserFilter(request.GET, queryset=user_list)
    if request.GET:
        user_filtered = UserFilter(request.GET, queryset=user_list)
    if request.POST:
        sender = request.user
        receiver = request.POST.get("user")
        user_receiver = User.objects.filter(username=receiver)
        if sender.username != user_receiver[0].username:
            chat_rooms_1 = ChatRoom.objects.filter(sender=sender, receiver=user_receiver[0])
            chat_rooms_2 = ChatRoom.objects.filter(sender=user_receiver[0], receiver=sender)
            print(chat_rooms_1)
            if (len(user_receiver) != 0):
                if (len(chat_rooms_1) == 0 and len(chat_rooms_2) == 0):
                    chat_room = ChatRoom.objects.create(
                        sender=sender,
                        receiver=user_receiver[0]
                    )
                    chat_room.save()
                    return redirect("chat")
                else:
                    return render(request, 'users.html', {'user_filtered': user_filtered,
                                                               'no_user': "Chat already exists"})
            else:
                return render(request, 'users.html', {'user_filtered': user_filtered, 'no_user': "No such user"})
        else:
            return render(request, 'users.html', {'user_filtered': user_filtered, 'no_user': "Same user is not allowed."})
    else:
        return render(request, 'users.html', {'user_filtered': user_filtered, 'no_user': ""})

@login_required
def conversation(request, id):
    chat_room = ChatRoom.objects.filter(id=id)

    if len(chat_room) != 0:
        chat_room = ChatRoom.objects.filter(id=id)[0]
        if request.user == chat_room.sender or request.user == chat_room.receiver:
            if request.user == chat_room.sender:
                user1 = request.user.username
                user2 = chat_room.receiver
            else:
                user1 = chat_room.sender
                user2 = request.user.username
            return render(request, 'conversation.html', {'user1': user1, 'user2': user2, 'id': id})

        else:
            return redirect("chat")
    else:
        return redirect("chat")
