from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, logout
from account.models import UserModel

# Create your views here.

def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        userN = UserModel.objects.filter(user_name=user_name).exists()

        mail = UserModel.objects.filter(email=email).exists()

        if(userN):
            return JsonResponse({'message': 'user name already exist'}, status=400)

        if(mail):
            return JsonResponse({'message': 'email already exist'}, status=400)

        if password != password2:
            return JsonResponse({'message': 'password does not match'}, status=400)
        else:
            user = UserModel.objects.create_user(
                full_name=full_name,
                user_name=user_name,
                email=email,
                password=password
            )
            user.save()
            return JsonResponse({'message': 'Sign up successfully'}, status=201)
    return render(request, 'signup.html')

def loginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        User = authenticate(request, email=email, password=password)
        if User:
            return JsonResponse({'message': 'Login successfully'}, status=200)
            return redirect('/')
        return JsonResponse({'message': 'User does not exist'}, status=404)
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/account/login')
