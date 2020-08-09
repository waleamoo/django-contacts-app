from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from django.views.generic import ListView, DetailView
from django.db.models import Q # helps to retrieve a model based on multiple field from a search term
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.
# def home(request):
#     context = {
#         'contacts': Contact.objects.all()
#     }
#     return render(request, 'index.html', context)

# def detail(request, id):
#     context = {
#         'contact':get_object_or_404(Contact, pk=id)
#     }
#     return render(request, 'detail.html', context)

    #manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
#class HomePageView(ListView):
class HomePageView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = Contact
    context_object_name = 'contacts'
    # get only contacts of logged in users 
    def get_queryset(self):
        contacts = super().get_queryset()
        return contacts.filter(manager = self.request.user)


class ContactDetailView(LoginRequiredMixin, DetailView):
    template_name = 'detail.html'
    model = Contact
    context_object_name = 'contact'

@login_required
def search(request):
    if request.GET:
        search_term = request.GET['search_term']
        #search_results = Contact.objects.filter(name__icontains=search_term)
        search_results = Contact.objects.filter(
            Q(name__icontains=search_term) | 
            Q(email__icontains=search_term) | 
            Q(info__icontains=search_term) | 
            Q(phone__iexact=search_term)
        )
        context = {
            'search_term': search_term,
            #'contacts': search_results
            'contacts': search_results.filter(manager = request.user)
        }
        return render(request, 'search.html', context)

    else:
        return redirect('home')

class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = 'create.html'
    fields = ['name', 'email', 'phone', 'info', 'gender', 'image']
    success_url = '/'
    # assign manager to current logged in user 
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        messages.success(self.request, "Contact created successfully.")
        return redirect('home')

class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Contact
    template_name = 'update.html'
    fields = ['name', 'email', 'phone', 'info', 'gender', 'image']
    #success_url = '/'
    # redirects the form to detail page 
    def form_valid(self, form):
        instance = form.save()
        messages.success(self.request, "Contact updated successfully.")
        return redirect('detail', instance.pk)

class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = 'delete.html'
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Contact deleted successfully.")
        return super().delete(self, request, *args, **kwargs)

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = '/'