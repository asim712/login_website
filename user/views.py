


from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Post,About,Photo

# Create your views here.
def index(request):
    posts = Post.objects.all()
    abouts = About.objects.all()
    return render(request, 'index.html', {'posts':posts,"abouts":abouts})

# post block 
def post(request,pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'post.html',{'posts':posts})


# login block 
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        
        else:
            messages.info(request,'Credential Invalid')
            return redirect('login')

    return render(request, 'login.html')

# logout block
def logout(request):
    auth.logout(request)
    return redirect('/')
    
# signup block 
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 =request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password2)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'Password not same')
            return redirect('signup')

    
    return render(request,'signup.html')

# gallery block
def gallery(request):
    photos = Photo.objects.all()
    return render(request,'gallery.html',{'photos':photos})

# contact block 
def contact(request):
    return render(request, 'contact.html')