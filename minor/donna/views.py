from django.shortcuts import render
from .forms import tinyFormTest
from django.http import JsonResponse
from .models import tinytest
import time

def home(request):
	form = tinyFormTest()
	if request.is_ajax():
		form = tinyFormTest(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			if request.method == 'POST':
				name = request.POST['name']
				# print(str(name) + 'asd')
				time.sleep(3)
				res = chatbot(name)
				print(res)
			data = {
			"message":name,
			"res":res
			}
			return JsonResponse(data)
	context = {
	'form':form,
	}
	return render(request,'form.html',context)



def chatbot(userQuery):
	if userQuery == 'Hi':
		return 'Hello'
	else:
		return 'WRONG INPUT'