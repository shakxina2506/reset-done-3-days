from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect
from sms.service import send_otp
from users.forms import SignUpForm
from django.utils import timezone
from .models import OTP
from sms.utils import generate_otp
from .forms import VerifyOTPForm
def register(request):
    form = SignUpForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            email = user.email
            otp = generate_otp()
            send_otp(email,otp)
            OTP.objects.create(user=user,otp=otp)
            return redirect('verify_otp')
    else:
        form = SignUpForm()
    context = {
        'form': form
    }
    return render(request,'register.html',context)



def verify_otp(request):
    if request.method == 'POST':
        form = VerifyOTPForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data['otp']
            obj_otp = OTP.objects.filter(otp=otp).first()
            if not obj_otp:
                return redirect('verify-otp')

            if obj_otp.is_used:
                return redirect('verify-otp')

            if timezone.now() - obj_otp.created_at > timezone.timedelta(minutes=5):
                obj_otp.is_used = True
                obj_otp.save()
                return redirect('verify-otp')

            user = obj_otp.user
            user.is_active = True
            user.save()


            obj_otp.is_used = True
            obj_otp.save()

            return redirect('login')
    else:
        form = VerifyOTPForm()

    return render(request, 'verify.html', {'form': form})

@login_required
def profile(request):
    user=request.user
    context={
        'user':user
    }
    return render(request, 'profile.html',context)


def change_done(request):
     return render(request, 'change_password_done.html')