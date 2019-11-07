from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Photo

# Create your views here.
def index(request):
    photos = Photo.objects.all().order_by('-created_at')
    return render(request, 'app/index.html', {'photos':photos})

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    photos = user.photo_set.all().order_by('-created_at')
    return render(request, 'app/user_detail.html', {'user':user, 'photos':photos})
