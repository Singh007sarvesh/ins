from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from userdetail.models import User
from userdetail.serializers import UserSerializer
from rest_framework.authentication import(BasicAuthentication,
	TokenAuthentication)
# Create your views here.


class UserList(APIView):
	authentication_classes = (TokenAuthentication, BasicAuthentication)
	def get(self, request):
		user = User.objects.all()
		user_serialized = UserSerializer(user, many = True)
		return JsonResponse(user_serialized.data, safe = False)
	def post(self, request):
		user_name = request.POST["user_name"]
		password = request.POST["password"]
		state = request.POST["state"]
		gender = request.POST["gender"]
		first_name = request.POST["first_name"]
		last_name = request.POST["last_name"]
		user = User(user_name = user_name, password = password, state = state,
			gender = gender,first_name = first_name, last_name = last_name)
		user.save()
		return HttpResponse('create success')
