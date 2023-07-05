from concurrent.futures.process import _process_chunk
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserForm
from .models import Company
import csv
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .utils import process_chunk
from .models import Company
from django.db.models import Q

# CSV File Upload Logic
@login_required(login_url='loginview_url')
@csrf_exempt
def upload(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8')
        csv_data = csv.reader(decoded_file.splitlines())  # , delimiter=','
        next(csv_data)
        for row in csv_data:
            Company.objects.create(industry_name=row[0], domain=row[1],year_founded=row[2], 
                                   size_range=row[3],locality=row[4], country=row[5],linkedIn_url=row[6]
                                   ,current_estimate_emp=row[7], total_estimate_emp=row[8],)
        # with open('uploaded_file.csv', 'wb+') as destination:
        #     for chunk in csv_file.chunks():
        #         destination.write(chunk)

        return render(request, 'success.html')
    
    return render(request, 'upload.html')

#######################################################################################
# Query Filter

def filter_records(request):
    #Get the filter parameters from the request
    filter_param1 = request.GET.get('industry_name', None)
    filter_param2 = request.GET.get('domain', None)
    
    # Build the query based on the filter parameters
    query = Q()
    if filter_param1:
        query &= Q(industry_name=filter_param1)
    if filter_param2:
        query &= Q(domain=filter_param2)

    # Apply the filters and get the count of matching records
    count = Company.objects.filter(query).count()
    
    messages.add_message(request, messages.SUCCESS, f'{count} Records found for the query')
    return render(request, 'filter_count.html' )




#######################################################################################

# Authentication Logics
@login_required(login_url='loginview_url')
def userView(request):
    obj = User.objects.all()
    teml_nm = 'users.html'
    context = {'data': obj}
    return render(request, teml_nm, context)


@login_required(login_url='loginview_url')
def signupView(request):
    form = UserForm()
    templ_nm = 'register.html'
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'User added successfully.')
            return redirect('users')
    context = {'form': form}
    return render(request, templ_nm, context)

def loginView(request):
    templ_nm = 'login.html'
    context = {}
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        user = authenticate(username=un, password=pw)
        print(user)
        if user is not None:
            login(request, user)

            return redirect('upload')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, templ_nm, context)




def logoutView(request):
    logout(request)
    return redirect('loginview_url')