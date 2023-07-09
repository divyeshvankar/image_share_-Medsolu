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

def upload_image(request):
    if request.method == 'POST':
        title = request.POST['title']
        image_data = request.POST['image'].split(',')[1]  # Extract the base64 image data
        image_data = base64.b64decode(image_data)  # Decode the base64 image data
        Image.objects.create(title=title, image_data=image_data)
        return HttpResponse(status=200)
    return render(request, 'upload_image.html')


def image_list(request):
    images = Image.objects.all()
    return render(request, 'image_list.html', {'images': images})

def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    if request.method == 'POST':
        image.delete()
        return redirect('image_list')
    return render(request, 'delete_image.html', {'image': image})


from django.shortcuts import render

def scan_photo(request):
    return render(request, 'scan_photo.html')

