from django.shortcuts import render


from .models import Actor
from .forms import ActorSearchForm
from search_views.search import SearchListView
from search_views.filters import BaseFilter


class ActorsFilter(BaseFilter):
    search_fields = {
        'search_text' : ['name', 'surname'],
        'search_age_exact' : { 'operator' : '__exact', 'fields' : ['age'] },
        'search_age_min' : { 'operator' : '__gte', 'fields' : ['age'] },
        'search_age_max' : { 'operator' : '__lte', 'fields' : ['age'] },

    }


class ActorsSearchList(SearchListView):
    model = Actor
    paginate_by = 30
    template_name = "actors/actors_list.html"
    form_class = ActorSearchForm
    filter_class = ActorsFilter
