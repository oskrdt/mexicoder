from django.contrib import admin
from soccer.models import SoccerPeople
from soccer.models import SoccerTeam
from soccer.models import SoccerLeage
admin.site.register(SoccerPeople)
admin.site.register(SoccerTeam)
admin.site.register(SoccerLeage)

# Register your models here.
