from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def post_list(request):
	return render(request,'blog/post_list.html',{})
	
