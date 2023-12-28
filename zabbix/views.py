from django.shortcuts import render
from banco.models import HostsAtivosZB
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . forms import HostsAtivosZBModelForm
from django.urls import reverse_lazy

# Create your views here.
def hosts(request):

    hosts_ativos = HostsAtivosZB.objects.all()[:100]
    search = request.GET.get('search')
    if search:
        hosts_ativos=HostsAtivosZB.objects.filter(host__icontains=search)

    search_id = request.GET.get('search_id')
    if search_id:
        hosts_ativos=HostsAtivosZB.objects.filter(id__icontains=search_id)
    
    
    #hosts_ativos = HostsAtivosZB.objects.all()[:100]
    context = {
        'hosts_ativos' : hosts_ativos,
        
    }

    return render(request, 'hosts.html', context)


class ListView(DetailView):
    model = HostsAtivosZB
    template_name = 'list_view.html'
    


class ListUpdate(UpdateView):
    model = HostsAtivosZB
    form_class = HostsAtivosZBModelForm
    template_name = 'host_update.html'
    success_url = '/hosts/'
