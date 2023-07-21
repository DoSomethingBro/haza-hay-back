from django.shortcuts import render
# from django.http import HttpResponse
# from rest_framework.views import APIView
from rest_framework.response import Response
from Haza.models import User
from Haza.serialize import HazaSerializer
from rest_framework import generics,status
from rest_framework.views import APIView
# Create your views here.





class ListUserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = HazaSerializer

class ListUsersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = HazaSerializer
    lookup_field = "matricule"

class VerifyUser(APIView):
    def post(self,request,*args,**kwargs):
        userobj = User.objects.get(email = request.data.get("email"))
        if userobj is not None :
            if userobj.password == request.data.get("password"):
                return Response({"Logged in Successfully"}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"email or password incorrect"},status=status.HTTP_403_FORBIDDEN)



# class UserAdd(APIView):
#     def post(self,request):
#         UserObj = HazaSerializer(data=request.data)
#         if UserObj.is_valid():
#             UserObj.save()
#             return Response(200)
#         return Response(UserObj.errors)
    
# class UserShow(APIView):
#     def get(self,request):
#         UserObj = User.objects.all()
#         Serialise = HazaSerializer(UserObj,many=True)
#         return Response(Serialise.data)
    

# class UserUpdate(APIView):
#     def post(self,request,pk):
#         try:
#             UpdateObj = User.objects.get(pk=pk)
#         except:
#             return Response("Error in Database")
        
#         UserObj = HazaSerializer(UpdateObj,data=request.data)
#         if UserObj.is_valid():
#             UserObj.save()
#             return Response(200)
#         return Response(UserObj.errors)
    
# class UserDelete(APIView):
#     def post(self,request,pk):
#         try:
#             DeleteObj = User.objects.get(pk=pk)
#         except:
#             return Response("Error in Database")
#         DeleteObj.delete()
#         return Response(200)
#         return Response(UserObj.errors)