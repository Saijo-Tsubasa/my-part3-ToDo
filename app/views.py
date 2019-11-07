from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'app/user_detail.html', {'user':user})
