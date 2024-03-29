from django.views import generic
from .models import Animal, Species, Domain, Kingdom, Phylum, Class, Order, Family, Genus
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.views import View
from django.db.models import Q


class DomainDeleteView(generic.DeleteView):
    model = Domain
    template_name = 'confirm_delete_templates/domain_confirm_delete.html'
    success_url = reverse_lazy('bird_list')


class KingdomDeleteView(generic.DeleteView):
    model = Kingdom
    template_name = 'confirm_delete_templates/kingdom_confirm_delete.html'
    success_url = reverse_lazy('bird_list')


class PhylumDeleteView(generic.DeleteView):
    model = Phylum
    template_name = 'confirm_delete_templates/phylum_confirm_delete.html'
    success_url = reverse_lazy('bird_list')


class ClassDeleteView(generic.DeleteView):
    model = Class
    template_name = 'confirm_delete_templates/class_confirm_delete.html'
    success_url = reverse_lazy('bird_list')


class OrderDeleteView(generic.DeleteView):
    model = Order
    template_name = 'confirm_delete_templates/order_confirm_delete.html'
    success_url = reverse_lazy('bird_list')


class FamilyDeleteView(generic.DeleteView):
    model = Family
    template_name = 'confirm_delete_templates/family_confirm_delete.html'
    success_url = reverse_lazy('bird_list')


class GenusDeleteView(generic.DeleteView):
    model = Genus
    template_name = 'confirm_delete_templates/genus_confirm_delete.html'
    success_url = reverse_lazy('bird_list')


class SpeciesDeleteView(generic.DeleteView):
    model = Species
    template_name = 'confirm_delete_templates/species_confirm_delete.html'
    success_url = reverse_lazy('bird_list')


from .forms import SearchForm


class BirdList(generic.ListView):
    model = Domain
    paginate_by = 10
    template_name = 'lists/domain_list.html'
    context_object_name = 'domains'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm()
        return context


class BirdSearchView(generic.ListView):
    template_name = 'search.html'
    context_object_name = 'search_results'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search_query')
        return Animal.objects.filter(name__icontains=query)


class KingdomList(generic.ListView):
    template_name = 'lists/kingdom_list.html'
    context_object_name = 'kingdoms'

    def get_queryset(self):
        domain_name = self.kwargs['domain_name']
        domain = Domain.objects.get(name=domain_name)
        return Kingdom.objects.filter(domain=domain)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['domain_name'] = self.kwargs['domain_name']
        return context


class PhylumList(generic.ListView):
    template_name = 'lists/phylum_list.html'
    context_object_name = 'phylums'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kingdom_name = self.kwargs['kingdom_name']
        kingdom = Kingdom.objects.get(name=kingdom_name)
        domain_name = kingdom.domain.name
        context['domain_name'] = domain_name
        context['kingdom_name'] = kingdom_name
        return context

    def get_queryset(self):
        kingdom_name = self.kwargs['kingdom_name']
        kingdom = Kingdom.objects.get(name=kingdom_name)
        return Phylum.objects.filter(kingdom=kingdom)


class ClassList(generic.ListView):
    template_name = 'lists/class_list.html'
    context_object_name = 'classes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # kingdom_name = self.kwargs['kingdom_name']
        phylum_name = self.kwargs['phylum_name']
        # kingdom = Kingdom.objects.get(name=kingdom_name)
        phylum = Phylum.objects.get(name=phylum_name)
        domain_name = phylum.kingdom.domain.name
        kingdom_name = phylum.kingdom.name
        phylum_name = phylum.name
        context['domain_name'] = domain_name
        context['kingdom_name'] = kingdom_name
        context['phylum_name'] = phylum_name
        return context

    def get_queryset(self):
        phylum_name = self.kwargs['phylum_name']
        phylum = Phylum.objects.get(name=phylum_name)
        return Class.objects.filter(phylum=phylum)


class OrderList(generic.ListView):
    template_name = 'lists/order_list.html'
    context_object_name = 'orders'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        class_name = self.kwargs['class_name']
        class_ = Class.objects.get(name=class_name)
        domain_name = class_.phylum.kingdom.domain.name
        kingdom_name = class_.phylum.kingdom.name
        phylum_name = class_.phylum.name
        class_name = class_.name
        context['domain_name'] = domain_name
        context['kingdom_name'] = kingdom_name
        context['phylum_name'] = phylum_name
        context['class_name'] = class_name
        return context

    def get_queryset(self):
        class_name = self.kwargs['class_name']
        class_ = Class.objects.get(name=class_name)
        return Order.objects.filter(Class=class_)


class FamilyList(generic.ListView):
    template_name = 'lists/family_list.html'
    context_object_name = 'families'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order_name = self.kwargs['order_name']
        order = Order.objects.get(name=order_name)
        domain_name = order.Class.phylum.kingdom.domain.name
        kingdom_name = order.Class.phylum.kingdom.name
        phylum_name = order.Class.phylum.name
        class_name = order.Class.name
        order_name = order_name
        context['domain_name'] = domain_name
        context['kingdom_name'] = kingdom_name
        context['phylum_name'] = phylum_name
        context['class_name'] = class_name
        context['order_name'] = order_name
        return context

    def get_queryset(self):
        order_name = self.kwargs['order_name']
        order = Order.objects.get(name=order_name)
        return Family.objects.filter(order=order)


class GenusList(generic.ListView):
    template_name = 'lists/genus_list.html'
    context_object_name = 'genuses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        family_name = self.kwargs['family_name']
        family = Family.objects.get(name=family_name)
        domain_name = family.order.Class.phylum.kingdom.domain.name
        kingdom_name = family.order.Class.phylum.kingdom.name
        phylum_name = family.order.Class.phylum.name
        class_name = family.order.Class.name
        order_name = family.order.name
        family_name = family.name
        context['domain_name'] = domain_name
        context['kingdom_name'] = kingdom_name
        context['phylum_name'] = phylum_name
        context['class_name'] = class_name
        context['order_name'] = order_name
        context['family_name'] = family_name
        return context

    def get_queryset(self):
        family_name = self.kwargs['family_name']
        family = Family.objects.get(name=family_name)
        return Genus.objects.filter(family=family)


class SpeciesList(generic.ListView):
    template_name = 'lists/species_list.html'
    context_object_name = 'specieses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genus_name = self.kwargs['genus_name']
        genus = Genus.objects.get(name=genus_name)
        domain_name = genus.family.order.Class.phylum.kingdom.domain.name
        kingdom_name = genus.family.order.Class.phylum.kingdom.name
        phylum_name = genus.family.order.Class.phylum.name
        class_name = genus.family.order.Class.name
        order_name = genus.family.order.name
        family_name = genus.family.name
        genus_name = genus.name
        context['domain_name'] = domain_name
        context['kingdom_name'] = kingdom_name
        context['phylum_name'] = phylum_name
        context['class_name'] = class_name
        context['order_name'] = order_name
        context['family_name'] = family_name
        context['genus_name'] = genus_name
        return context

    def get_queryset(self):
        genus_name = self.kwargs['genus_name']
        genus = Genus.objects.get(name=genus_name)
        return Species.objects.filter(genus=genus)


def bird_detail_view(request, species_name):
    animal = get_object_or_404(Animal, species=species_name)
    return render(request, "bird_detail.html",
                  {
                      "animal": animal,
                  })


class DomainCreate(generic.CreateView):
    model = Domain
    template_name = 'create_list/domain_create.html'
    fields = ['name']
    success_url = reverse_lazy('create_kingdom')


class KingdomCreate(generic.CreateView):
    model = Kingdom
    template_name = 'create_list/kingdom_create.html'
    fields = ['name', 'domain']
    success_url = reverse_lazy('create_phylum')


class PhylumCreate(generic.CreateView):
    model = Phylum
    template_name = 'create_list/phylum_create.html'
    fields = ['name', 'kingdom']
    success_url = reverse_lazy('create_class')


class ClassCreate(generic.CreateView):
    model = Class
    template_name = 'create_list/class_create.html'
    fields = ['name', 'phylum']
    success_url = reverse_lazy('create_order')


class OrderCreate(generic.CreateView):
    model = Order
    template_name = 'create_list/order_create.html'
    fields = ['name', 'Class']
    success_url = reverse_lazy('create_family')


class FamilyCreate(generic.CreateView):
    model = Family
    template_name = 'create_list/family_create.html'
    fields = ['name', 'order']
    success_url = reverse_lazy('create_genus')


class GenusCreate(generic.CreateView):
    model = Genus
    template_name = 'create_list/genus_create.html'
    fields = ['name', 'family']
    success_url = reverse_lazy('create_species')


class SpeciesCreate(generic.CreateView):
    model = Species
    template_name = 'create_list/species_create.html'
    fields = ['name', 'genus']
    success_url = reverse_lazy('create_bird')


class BirdCreate(generic.CreateView):
    model = Animal
    template_name = 'create_list/bird_create.html'
    fields = ['name', 'weight', 'height', 'parent_group', 'lifespan', 'species']


# class BirdDetail(generic.DeleteView):
#     model = Animal
#     template_name = "bird_detail.html"
#     context_object_name = 'animal'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         species_name = self.kwargs['species_name']
#         species = Species.objects.get(name=species_name)
#         domain_name = species.genus.family.order.Class.phylum.kingdom.domain.name
#         kingdom_name = species.genus.family.order.Class.phylum.kingdom.name
#         phylum_name = species.genus.family.order.Class.phylum.name
#         class_name = species.genus.family.order.Class.name
#         order_name = species.genus.family.order.name
#         family_name = species.genus.family.name
#         genus_name = species.genus.name
#         species_name = species.name
#         context['domain_name'] = domain_name
#         context['kingdom_name'] = kingdom_name
#         context['phylum_name'] = phylum_name
#         context['class_name'] = class_name
#         context['order_name'] = order_name
#         context['family_name'] = family_name
#         context['genus_name'] = genus_name
#         context['species_name'] = species_name
#         return context
#
#     def get_queryset(self):
#         species_name = self.kwargs['species_name']
#         species = Species.objects.get(name=species_name)
#         return Animal.objects.filter(species=species)


from django.db.models import Q


def search_in_animal(request):
    search_result = None
    if request.method == "POST":
        search_name = request.POST.get("search_keyword_name")
        min_weight = request.POST.get("search_keyword_weight_min") or "0"
        max_weight = request.POST.get("search_keyword_weight_max") or "10000"
        min_height = request.POST.get("search_keyword_height_min") or "0"
        max_height = request.POST.get("search_keyword_height_max") or "10000"
        min_lifespan = request.POST.get("search_keyword_lifespan_min") or "0"
        max_lifespan = request.POST.get("search_keyword_lifespan_max") or "10000"
        if min_weight.isnumeric() and max_weight.isnumeric() and min_height.isnumeric() and max_height.isnumeric() and min_lifespan.isnumeric() and max_lifespan.isnumeric():
            search_result = Animal.objects.filter(
                name__icontains=search_name,
                weight__gte=int(min_weight),
                weight__lte=int(max_weight),
                height__gte=int(min_height),
                height__lte=int(max_height),
                lifespan__gte=int(min_lifespan),
                lifespan__lte=int(max_lifespan)
            )
        # else:
        #     return render(request, 'invalid_search.html')
    return render(request, 'search_results.html', {'search_result': search_result})


def compare_bird(request):
    name_1 = request.POST.get("animal_name")
    weight_1 = request.POST.get("animal_weight")
    parent_group_1 = request.POST.get("animal_parent_group")
    height_1 = request.POST.get("animal_height")
    lifespan_1 = request.POST.get("animal_lifespan")

    request.session["name_1"] = name_1
    request.session["weight_1"] = weight_1
    request.session["parent_group_1"] = parent_group_1
    request.session["height_1"] = height_1
    request.session["lifespan_1"] = lifespan_1

    all_animal = Animal.objects.all()
    #
    # redirect('select_bird', context={'name_1': name_1, 'all_animal': all_animal})
    return render(request, 'select_animal.html', {'name_1': name_1,
                                                  'weight_1': weight_1,
                                                  'parent_group_1': parent_group_1,
                                                  'height_1': height_1,
                                                  'lifespan_1': lifespan_1,
                                                  'all_animal': all_animal})


def select_bird(request):
    name_1 = request.POST.get("animal_name_1")
    weight_1 = request.POST.get("animal_weight_1")
    parent_group_1 = request.POST.get("animal_parent_group_1")
    height_1 = request.POST.get("animal_height_1")
    lifespan_1 = request.POST.get("animal_lifespan_1")

    name_2 = request.POST.get("animal_name")
    weight_2 = request.POST.get("animal_weight")
    parent_group_2 = request.POST.get("animal_parent_group")
    height_2 = request.POST.get("animal_height")
    lifespan_2 = request.POST.get("animal_lifespan")
    return render(request, 'compare_animals.html', {'name_1': name_1,
                                                    'weight_1': weight_1,
                                                    'parent_group_1': parent_group_1,
                                                    'height_1': height_1,
                                                    'lifespan_1': lifespan_1,
                                                    'name_2': name_2,
                                                    'weight_2': weight_2,
                                                    'parent_group_2': parent_group_2,
                                                    'height_2': height_2,
                                                    'lifespan_2': lifespan_2
                                                    })
