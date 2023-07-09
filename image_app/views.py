from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Image

# def upload_image(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         image_file = request.FILES['image']
#         image_data = image_file.read()
#         Image.objects.create(title=title, image_data=image_data)
#         return redirect('image_list')
#     return render(request, 'upload_image.html')
from django.shortcuts import render, redirect
from .models import Image
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Image
import base64

from django.contrib.auth.decorators import login_required

@login_required
def upload_image(request):
    if request.method == 'POST':
        title = request.POST['title']
        image_file = request.FILES['image']
        image_data = image_file.read()

        # Save the image to the Image model with the authenticated user
        Image.objects.create(user=request.user, title=title, image_data=image_data)
        return redirect('image_list')
    return render(request, 'upload_image.html')

# @login_required
# def image_list(request):
#     images = Image.objects.filter(user=request.user)
#     return render(request, 'image_list.html', {'images': images})

from django.contrib.auth.models import User

@login_required
def image_list(request):
    images = Image.objects.filter(user=request.user)
    return render(request, 'image_list.html', {'images': images})


from django.contrib.auth.models import User
from django.contrib.auth.models import User

@login_required
def send_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)

    if request.method == 'POST':
        return redirect('send_image_form', image_id=image_id, username=request.POST.get('username'))

    return render(request, 'send_image.html', {'image': image})

from django.contrib import messages

@login_required
def send_image_form(request, image_id):
    image = get_object_or_404(Image, id=image_id)

    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            recipient = User.objects.get(username=username)
            Image.objects.create(user=recipient, title=image.title, image_data=image.image_data)
            return redirect('image_list')
        except User.DoesNotExist:
            messages.error(request, 'User does not exist.')
            return redirect('send_image_form', image_id=image_id)

    return render(request, 'send_image_form.html', {'image': image})


def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    if request.method == 'POST':
        image.delete()
        return redirect('image_list')
    return render(request, 'delete_image.html', {'image': image})


from django.shortcuts import render

def scan_photo(request):
    return render(request, 'scan_photo.html')


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('image_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'




# from django.contrib.auth.models import User

# @login_required
# def send_image(request, image_id):
#     image = get_object_or_404(Image, id=image_id)

#     if request.method == 'POST':
#         username = request.POST['username']
#         recipient = User.objects.get(username=username)

#         # Create a new Image object with the recipient user
#         Image.objects.create(user=recipient, title=image.title, image_data=image.image_data)
#         return redirect('image_list')

#     return render(request, 'send_image.html', {'image': image})
