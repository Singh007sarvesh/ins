from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
# Create your views here.


class UserList(APIView):
	def get(self, request):
		return HttpResponse("Hello, world. You're at the polls index.")
	def post(self, request):
		user_name = request.POST["user_name"]
		password = request.POST["password"]
		state = request.POST["state"]
		gender = request.POST["gender"]
		first_name = request.POST["first_name"]
		last_name = request.POST["last_name"]
		user = User(user_name=user_name,password=password,state=state,gender=gender,first_name=first_name,last_name=last_name)
		user.save()
		return HttpResponse('create success')
