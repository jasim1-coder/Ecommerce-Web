from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from . models import Customer

# Create your views here.
def show_account(request):
    if request.POST and 'register' in request.POST:
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            address=request.POST.get('address')
            phone=request.POST.get('phone')

            # user creation

            user=User.objects.create(
                username=username,
                password=password,
                email=email,
                # address=address,
                # phone=phone

            )

            #create customer
            customer=Customer.objects.create(
                user=user,
                phone=phone,
                address=address
            )
            return redirect('home')
        except Exception as e:
            error_message="Duplicate username or invalid credential"
            messages.error(request,error_message)
    return render(request, 'account.html')