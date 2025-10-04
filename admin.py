from django.contrib import admin
from .models import Voter, County, Constituency, Candidate, Vote

admin.site.register(Voter)
admin.site.register(County)
admin.site.register(Constituency)
admin.site.register(Candidate)
admin.site.register(Vote)