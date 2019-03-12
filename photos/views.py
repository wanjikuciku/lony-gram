# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from .models import Image,Follow,Profile,Comments
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import ImageForm,ProfileForm
from .email import send_welcome_email

# Create your views here.
@login_required(login_url = "accounts/login")
def index(request):
    user_has_liked_list = []
    images = Image.objects.all().order_by("-pub_date")
    for image in images:
        user = image.user
        followers = user.user_followers.all()
        arr_ = []
        for follower in followers:
            arr_.append(follower.followed_by.id)

        if request.user.id in arr_:
            image.user.is_following = True
        else: 
            image.user.is_following = False
        
        if image.user.id == request.user.id:
            user.me = True
        else:
            user.me = False
        if request.user in image.likes.all():
            image.user_has_liked = True
        else:
            image.user_has_liked = False
    return render(request,"index.html", {"images":images,"user":request.user})

def like(request):
    user = request.user
    if request.method == 'POST':
        ObjectId = int(request.POST['objectid'])
        Tip = str(request.POST['contentType'])

        likes = LikeModel.objects.filter(object_id=ObjectId, content_object=Tip) # in here we filtered the particular post with its id
        if likes: # if the particular post is there
            if str(user) in str(likes): # then we check the user which is us, in there
                like_obj = LikeModel.objects.get(user=user,object_id=ObjectId, content_object=Tip) #if we there and we returned this data, this part for saving data, I mean if this data is already created than we dont have to delete and create again, we just change LikeModel.liked true or false state, so that if you create like and it will never delete, it just change liked or like state
            else:
                pass

        if Tip == 'UserPost':
            post_content_type_by = UserPost.objects.all().first()

            if str(user) not in str(likes):
                like = LikeModel.objects.create(user=user, liked=True, content_object=ContentType.objects.get_for_model(Tip), object_id=ObjectId)
                like.save() # if data is created then we say 'new'
                okey = 'new'

            elif str(user) in str(likes) and like_obj.liked:
                like_obj.liked = False
                like_obj.save() # if data is already there, then we save it False
                okey = 'false'

            elif str(user) in str(likes) and like_obj.liked == False:
                like_obj.liked = True
                like_obj.save() # if data is already changed to False and we save again to True
                okey = 'true'


    return render(request,'ajaxlike.html',{'likes':likes,'okey':okey})

def like(request):
    user = request.user
    images = Image.objects.all()
    image_id = request.POST.get("id")
    if image_id != None:
        idss.objects.create(identifier = request.POST.get("id"))
    last_one = idss.objects.all()
    mwisho = idss.objects.get(pk = last_one.count())
    image = Image.objects.get(pk = mwisho.identifier)
    to_red = None
    if user in image.likes.all():
        image.likes.remove(user)
        to_red = 0
    else:
        image.likes.add(user)
        to_red = 1
    likes = image.likes.all().count()
    data = {"likes":likes, "to_red": to_red}
    return JsonResponse(data)

def comment(request):
    image_id = request.POST.get("id")
    image = Image.objects.get(pk = image_id)
    Comments.objects.create(user = request.user, image = image, comm = request.POST.get("comment"))
    
    user = request.user.username
    comment = request.POST.get("comment")

    data = {"user":user, "comment":comment}
    return JsonResponse(data)

def follow(request):
    image = Image.objects.get(id = request.POST.get("id"))
    user = image.user
    followed = None
    followers = user.user_followers.all()
    if Follow.objects.filter(user = user, followed_by = request.user):
        Follow.objects.filter(user = user, followed_by = request.user).delete()
        followed = 0
    else:
        Follow.objects.create(user = user, followed_by = request.user)
        followed = 1
    data = {"hey":"hey", "followed":followed}
    return JsonResponse(data)

def follow_in_profile(request):
    user = User.objects.get(id = request.POST.get("id"))
    followed = None
    followers = user.user_followers.all()
    if Follow.objects.filter(user = user, followed_by = request.user):
        Follow.objects.filter(user = user, followed_by = request.user).delete()
        followed = 0
        count = user.user_followers.all().count()
    else:
        Follow.objects.create(user = user, followed_by = request.user)
        followed = 1
        count = user.user_followers.all().count()
    data = {"hey":"hey", "followed":followed, "count":count}
    return JsonResponse(data)

def add_image(request):
    user = request.user
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit = False)
            image.user = user
            image.save()
            return redirect("index")
    else:
        form = ImageForm()
    return render(request, "add_image.html", {"form":form})

def update_profile(request):
    user = request.user
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            new_bio = form.cleaned_data["bio"]
            new_pic = form.cleaned_data["pic"]
            profile = Profile.objects.get(user = request.user)
            profile.bio = new_bio
            profile.pic = new_pic
            profile.save()
            final_url = "/profile/" + str(request.user.id) + "/"
            return redirect(final_url)
    else:
        form = ProfileForm()
    return render(request, "update_profile.html", {"form":form})  

def search_user(request):
    if "user_search_term" in request.GET and request.GET["user_search_term"]:
        term = request.GET.get("user_search_term")
        users = Profile.search_user(term)
        print(users)
        return render(request, "search.html", {"users":users,"title":term})

def my_profile(request):
    user = request.user
    return render(request, "my-profile.html", {"user":user, "current_user":request.user})

def profile(request,id):
    user = User.objects.get(id = id)
    followers = user.user_followers.all()
    followers_arr = []
    for follower in followers:
        followers_arr.append(follower.followed_by.id)
    
    if request.user.id in followers_arr:
        is_following = True
    else:
        is_following = False
    
    if request.user.id == int(id):
        return redirect("my_profile")
    else:
        return render(request, "profile.html", {"user":user,"current_user":request.user, "is_following": is_following})
