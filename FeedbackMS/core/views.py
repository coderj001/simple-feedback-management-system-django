from django.shortcuts import render
from core.models import Teacher,FeedBack

def home(request):
	return render(request,'core/home.html',context={})

def feedback(request):
	if request.method == 'GET':
		teacher=Teacher.objects.all()
		return render(request,'core/feedback.html', context={"teachers":teacher})
	else:
		pass