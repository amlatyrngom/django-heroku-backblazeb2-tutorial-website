from django.shortcuts import render

# In members/views.py
from django.core.urlresolvers import reverse_lazy # similar to reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import Member

class AllMembersView(ListView):
    model = Member
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(AllMembersView, self).get_context_data(**kwargs)
        context['title'] = 'All Members'
        return context

class NewMemberView(CreateView):
    template_name = "new_member.html"
    model = Member # Model of the object that will be created
    fields = ['name', 'short_bio', 'picture']
    success_url = reverse_lazy("members:all_members") # Redirect Url after creating the object

    def get_context_data(self, **kwargs):
        context = super(NewMemberView, self).get_context_data(**kwargs)
        context['title'] = "New Member"
        return context
