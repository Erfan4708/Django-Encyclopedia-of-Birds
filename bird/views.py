from django.shortcuts import render

# Create your views here.


from django.views import generic
from .models import Animal, Species, Domain, Kingdom, Phylum, Class, Order, Family, Genus
from django.urls import reverse_lazy ,reverse
from django.shortcuts import get_object_or_404 , render


class BirdList(generic.ListView):
    model = Domain
    paginate_by = 6
    template_name = 'bird_list.html'
    context_object_name = 'birds'


class BirdDeleteView(generic.DeleteView):
    model = Species
    template_name = 'bird_delete.html'
    success_url = reverse_lazy('bird_list')


class KingdomList(generic.ListView):
    template_name = 'kingdom_list.html'
    context_object_name = 'kingdoms'

    def get_queryset(self):
        domain_name = self.kwargs['domain_name']
        domain = Domain.objects.get(name=domain_name)
        return Kingdom.objects.filter(domain=domain)




