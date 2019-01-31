from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from userdetail.models import User as UserModel
from userdetail.serializers import UserSerializer
from rest_framework.authentication import(BasicAuthentication,
	TokenAuthentication)
class User(APIView):
	authentication_classes = (TokenAuthentication, BasicAuthentication)
	def get(self, request, pk):
		user = UserModel.objects.get(id = pk)
		user_serialized = UserSerializer(user)
		return JsonResponse(user_serialized.data, safe = False)
	def delete(self, request, pk):
		user = UserModel.objects.get(id = pk)
		user.delete()
		return HttpResponse("deleted")
	def patch(self, request, pk):
		# import pdb;pdb.set_trace()
		user = UserModel.objects.get(id = pk)
		serializer = UserSerializer(user, data=request.data, partial = True)
		if serializer.is_valid():
			serializer.save()
			return HttpResponse("Updated")
		return HttpResponse("Error..")


