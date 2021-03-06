from django.shortcuts import render
from .forms import tinyFormTest
from django.http import JsonResponse
from .models import tinytest
from . import chatbot
import time
import random

def home(request):
	wait = random.uniform(0, 2)
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
				print("random wait => " + str(wait))
				time.sleep(wait)
				res = chatbot_(name)
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



def chatbot_(userQuery):

	sent = chatbot.preprocess(userQuery)
	return chatbot.previous_chats(sent)
	# if userQuery == 'Hi':
	# 	return 'Hello'
	# else:
	# 	return 'WRONG INPUT'