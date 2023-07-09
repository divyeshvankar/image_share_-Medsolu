from django.urls import path
from . import views
from image_app.views import CustomLoginView,send_image

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('', views.image_list, name='image_list'),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
    path('scan/', views.scan_photo, name='scan_photo'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    # path('images/send/<int:image_id>/', send_image, name='send_image'),
     path('images/send/<int:image_id>/form/', views.send_image_form, name='send_image_form'),

]
