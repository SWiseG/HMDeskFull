from django.shortcuts import render

# Create your views here.
def sample_view(request):
    current_user = request.user
    return current_user
