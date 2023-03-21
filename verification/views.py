from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from verification.models import AvailableVoter
from django.db.models import Q
from .forms import SearchForm, RegisterForm

def index(request):

    # f = open('VotersRoll.csv', 'r') 
    # for line in f:  
    #     line =  line.split(',') 
    #     product = AvailableVoter()  
    #     product.fullname = line[0]  
    #     product.email = line[1]  
    #     product.new = False  
    #     product.status = True 
    #     product.save() 
    # f.close() 
    # 
    #   
    context = {}  
    context['data_found'] = True  
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            value= search_form.cleaned_data['search_value']
            voter_list = AvailableVoter.objects.filter(Q(email__contains=value) | Q(fullname__contains=value)).values()
            if not voter_list.exists():
                context['data_found'] = False 
                register_form = RegisterForm()
                context['register_form'] = register_form   
    else:
        search_form = SearchForm()
        voter_list = AvailableVoter.objects.all()
   
    paginator = Paginator(voter_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['search_form'] = search_form
    context['page_obj'] = page_obj

    return render(request, 'welcome.html',  context)

def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            product = AvailableVoter()  
            product.fullname = register_form.cleaned_data['fullname'] 
            product.email = register_form.cleaned_data['email']
            product.new = True  
            product.status = False 
            product.save() 
    return redirect('/')     
