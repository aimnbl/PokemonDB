from django.shortcuts import render
from django.db.models import Q
from .models import Pokemon, Type
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
# Create your views here.

def search(request):
    page = request.GET.get('page', 1)
    contain_value = False
    for i in request.GET.values():
        if i != "" :
            contain_value = True
            break

    if request.method == "GET":
        search_name = request.GET['name']
        search_gen = request.GET['gen']
        search_status = request.GET['status']
        search_type = request.GET.getlist('type[]')
        result = Pokemon.objects.all()
        if contain_value:
            if search_name != '':
                result = result.filter(Q(name__icontains = search_name) | Q(pokedex_no__icontains = search_name))
            if search_gen != '':
                result = result.filter(generation__iexact = search_gen)
            if search_status != '':
                result = result.filter(status__iexact = search_status)
            if search_type:
                if len(search_type) == 1:
                    result = result.filter(Q(type_1_id__in = search_type) | Q(type_2_id__in = search_type))
                else:
                    result = result.filter(Q(type_1_id__in = search_type) & Q(type_2_id__in = search_type))

        paginator = Paginator(result.order_by('id'), 10)
        try:
            pokemon = paginator.page(page)
        except PageNotAnInteger:
            pokemon = paginator.page(1)
        except EmptyPage:
            pokemon = paginator.page(paginator.num_pages)

        return render(request, 'search.html', {'pokemon':pokemon})

def pokemain(request):
    type = Type.objects.all()
    return render(request, 'main.html', {'type': type})

def pokeprofile(request):
    pokemon = Pokemon.objects.get(id__exact = request.GET['id'])
    alt_pokemon = Pokemon.objects.filter(pokedex_no = pokemon.pokedex_no).exclude(id = pokemon.id)
    return render(request, 'profile.html', {'pokemon': pokemon, 'alt_pokemon': alt_pokemon})    