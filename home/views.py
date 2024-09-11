from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
User = get_user_model()

# END PAGES
def index(request):
    context = {
    }
    return render(request,'home/index.html',context)