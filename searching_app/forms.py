from .models import Actor
from django import forms
class ActorSearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    label='Search name or surname!',
                    widget=forms.TextInput(attrs={'placeholder': 'search here!'})
                  )

    search_age_exact = forms.IntegerField(
                    required = False,
                    label='Search age (exact match)!'
                  )

    search_age_min = forms.IntegerField(
                    required = False,
                    label='Min age'
                  )


    search_age_max = forms.IntegerField(
                    required = False,
                    label='Max age'
                  )