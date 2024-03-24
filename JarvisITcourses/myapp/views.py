from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from myapp.models import Student
from myapp.forms import StudentForm
from django.http import HttpResponseRedirect
@login_required	
def read(request):
	student=Student.objects.all()
	return render(request,'apps/result.html',{'e':student})
def insert(request):
	form=StudentForm()
	if request.method=="POST":
		form=StudentForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request,'apps/insert.html',{'form':form})
def delete(request,id):
	e=Student.objects.get(id=id)
	e.delete()
	return redirect('/result')
def update(request,id):
	student=Student.objects.get(id=id)
	if request.method=="POST":
		form=StudentForm(request.POST,instance=student)
		if form.is_valid():
			form.save()
		return redirect('/result')
	return render(request,'apps/update.html',{'e':student})
def index(request):
	return render(request,'apps/index.html')
def contact(request):
	return render(request,'apps/contact.html')
def service(request):
	return render(request,'apps/service.html')
def gallery(request):
	return render(request,'apps/gallery.html')
def about(request):
	return render(request,'apps/about.html')
def home(request):
	return render(request,'apps/home.html')
def logout(request):
	return render(request,'apps/logout.html')
def signup_view(request):
	form=SignUpForm()
	if request.method=="POST":
		form=SignUpForm(request.POST)
		User=form.save()
		User.set_password(user.password)
		User.save()
		return HttpResponseRedirect('/accounts/login')
	return render(request,'apps/insert.html',{'form':form})
# Create your views here.
