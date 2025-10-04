from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Voter, Candidate, County, Constituency

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    county = forms.ModelChoiceField(queryset=County.objects.all())
    constituency = forms.ModelChoiceField(queryset=Constituency.objects.all())

    class Meta:
        model = Voter
        fields = ('username', 'email', 'county', 'constituency', 'password1', 'password2')

class VoteForm(forms.Form):
    candidate = forms.ModelChoiceField(queryset=Candidate.objects.none(), widget=forms.RadioSelect)

    def __init__(self, voter, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['candidate'].queryset = Candidate.objects.filter(
            county=voter.county, constituency=voter.constituency)