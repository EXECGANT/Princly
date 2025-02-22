from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models,serializer
from library.crud_operations import CRUDOperations
import random
import yagmail

# Create 6-digits otp:
def generate_otp():
    otp = str(random.randint(100000, 999999))
    if not models.UserModel.objects.filter(otp=otp).exists(): 
        return otp
    
def send_otp_email(email, otp):
    sender = 'abijithmailforjob@gmail.com'
    password = 'kgqzxinytwbspurf'
    subject = "ForgetPassword OTP"
    content = f"""
    OTP : {otp}
    """
    yagmail.SMTP(sender, password).send(
        to=email,
        subject=subject,
        contents=content
    )
    
class SignupView(APIView):
    def post(self,request):
        useremail=request.data.get('user_email')
        password=request.data.get('password')
        confirm_password=request.data.get('confirm_password')
        check_response= CRUDOperations.getFilteredData(model=models.UserModel, serializer=serializer.UserSerializer,user_email = useremail)
        if check_response:
            return Response({'error': 'User Already Exists'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if password == confirm_password:
                response = CRUDOperations.addNewData(serializer=serializer.UserSerializer, data=request.data)
                if response['status']:
                    return Response(data=response['data'], status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "Password Incorrect"}, status=status.HTTP_400_BAD_REQUEST)
class LoginView(APIView):
    def post(selif,request):
        useremail=request.data.get('user_email')
        pass_key=request.data.get('password')
        check_response= CRUDOperations.getFilteredData(model=models.UserModel, serializer=serializer.UserSerializer,user_email = useremail)
        if check_response:  
            user_data = check_response[0] if isinstance(check_response, list) else check_response 
            password=user_data.get('password')
            user_id = user_data.get('id')
            if password == pass_key:
                data={
                    'user_id':user_id,
                    'user_name':user_data.get('user_name')
                }
                return Response(data=data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'User Email or Password Incorrect'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class ForgetPasswordView(APIView):
    def post(self, request):
        action = request.data.get('action')
        if action == "send_otp":
            return self.send_otp(request)
        elif action == "verify_otp":
            return self.verify_otp(request)
        else:
            return Response({"error": "Invalid action specified."}, status=status.HTTP_400_BAD_REQUEST)

    def send_otp(self, request):
        user_email = request.data.get('user_email')
        check_response = CRUDOperations.getFilteredData(model=models.UserModel,serializer=serializer.UserSerializer,user_email=user_email)
        if check_response:
            user_data = check_response[0] if isinstance(check_response, list) else check_response
            print(user_data)
            user_id = user_data.get('id')
            otp = generate_otp()
            email = user_data.get('user_email')

            otp_response = CRUDOperations.updateExistingData(model=models.UserModel,serializer=serializer.UserOTPSerializer,id=user_id,data={"otp": otp})
            if otp_response['status']:
                send_otp_email(email, otp)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response({"error": "OTP not sent"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    def verify_otp(self, request):
        user_email = request.data.get('user_email')
        otp_input = request.data.get('otp')
        if not user_email or not otp_input:
            return Response({"error": "User email and OTP are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        check_response = CRUDOperations.getFilteredData(model=models.UserModel,serializer=serializer.UserDataSerializer,user_email=user_email)
        if check_response:
            user_data = check_response[0] if isinstance(check_response, list) else check_response
            otp = user_data.get('otp') 
            user_id = user_data.get('id')
            if otp == otp_input:
                data={
                    'user_id':user_id,
                    'user_email':user_email
                }
                return Response(data=data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid OTP."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self,request,id):
        new_password=request.data.get('password')
        confirm_password=request.data.get('confirm_password')
        if new_password == confirm_password:
            response = CRUDOperations.updateExistingData(model=models.UserModel, serializer=serializer.UserDataSerializer, id=id, data=request.data)
            if response['status']:
                return Response(data=response['data'], status=status.HTTP_200_OK)
            else:
                return Response({"error": "Password Not Saved"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Password Incorrect"}, status=status.HTTP_400_BAD_REQUEST)

    
class UsersView(APIView):
    def get(self,request):
        pass
    def post(self,request):
        
        pass
    def patch(self,request):
        pass
    def delete(self,request):
        pass
    
    
    
    
    
    
    