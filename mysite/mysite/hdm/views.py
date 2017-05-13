from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import HDM

def hdm_new(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    hdms = HDM.objects.all()
    return render(request, 'hdm/hdm_new.html', {'hdms': hdms})

