from django.shortcuts import render
from django.http import HttpResponse

from .models import Member

# Create your views here.
def index(request):
	members = Member.objects.all()
	context = {'members':members}
	return render(request, 'elections/index.html',context)
