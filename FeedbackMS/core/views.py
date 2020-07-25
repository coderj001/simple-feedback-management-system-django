from django.shortcuts import render,redirect
from django.contrib import messages
from core.models import Teacher,FeedBack

def home(request):
	return render(request,'core/home.html',context={})

def feedback(request):
	if request.method == 'GET':
		teacher=Teacher.objects.all()
		return render(request,'core/feedback.html', context={"teachers":teacher})
	if request.method == 'POST':
		name=request.POST['username']
		teacher=Teacher.objects.get(id=request.POST['teacher'])
		rating=request.POST['rating']
		detail=request.POST['detail']
		FeedBack.objects.create(name=name,teacher=teacher,rating=rating,detail=detail).save()
		messages.success(request, 'Created Successfuly')
		return redirect('home')