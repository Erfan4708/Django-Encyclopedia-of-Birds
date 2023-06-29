from django.urls import path

from .views import BirdList, KingdomDeleteView, PhylumDeleteView, ClassDeleteView, OrderDeleteView, FamilyDeleteView, \
    GenusDeleteView, SpeciesDeleteView, KingdomList, \
    PhylumList, ClassList, OrderList, \
    FamilyList, GenusList, \
    SpeciesList, bird_detail_view, DomainDeleteView, \
    BirdCreate, DomainCreate, KingdomCreate, PhylumCreate, ClassCreate, OrderCreate, FamilyCreate, GenusCreate, \
    SpeciesCreate, search_in_animal

urlpatterns = [
    path('search/', search_in_animal, name='search_bird'),
    path('', BirdList.as_view(), name='bird_list'),
    path('/domain/<str:domain_name>/kingdoms/', KingdomList.as_view(), name='kingdom_list'),
    path('domain/<int:pk>/delete/', DomainDeleteView.as_view(), name='delete_domain'),
    path('kingdoms/<str:kingdom_name>/phylum/', PhylumList.as_view(), name='phylum_list'),
    path('kingdoms/<int:pk>/delete/', KingdomDeleteView.as_view(), name='delete_kingdom'),
    path('phylum/<int:pk>/delete/', PhylumDeleteView.as_view(), name='delete_phylum'),
    path('phylum/<str:phylum_name>/class/', ClassList.as_view(), name='class_list'),
    path('class/<int:pk>/delete/', ClassDeleteView.as_view(), name='delete_class'),
    path('class/<str:class_name>/order/', OrderList.as_view(), name='order_list'),
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='delete_order'),
    path('order/<str:order_name>/family/', FamilyList.as_view(), name='family_list'),
    path('family/<int:pk>/delete/', FamilyDeleteView.as_view(), name='delete_family'),
    path('family/<str:family_name>/genus/', GenusList.as_view(), name='genus_list'),
    path('genus/<int:pk>/delete/', GenusDeleteView.as_view(), name='delete_genus'),
    path('genus/<str:genus_name>/species/', SpeciesList.as_view(), name='species_list'),
    path('species/<int:pk>/delete/', SpeciesDeleteView.as_view(), name='delete_species'),
    path('species/<str:species_name>/animal/', bird_detail_view, name='bird_detail'),
    # path('species/<int:pk>/animal/', BirdDetail.as_view(), name='bird_detail'),
    path('create/domain', DomainCreate.as_view(), name='create_domain'),
    path('create/kingdom', KingdomCreate.as_view(), name='create_kingdom'),
    path('create/phylum', PhylumCreate.as_view(), name='create_phylum'),
    path('create/class', ClassCreate.as_view(), name='create_class'),
    path('create/order', OrderCreate.as_view(), name='create_order'),
    path('create/family', FamilyCreate.as_view(), name='create_family'),
    path('create/genus', GenusCreate.as_view(), name='create_genus'),
    path('create/species', SpeciesCreate.as_view(), name='create_species'),
    path('create/bird', BirdCreate.as_view(), name='create_bird'),

]
