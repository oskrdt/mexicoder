from django.db import models

# Create your models here.

#soccer league, team, coach and player information
#teams belong to leagues, coach and players belongs to team.

#class Soccer(models.Model):
#  leage = models.CharField(max_length=50)
#  team = models.CharField(max_length=50)
#  coach = models.CharField(max_length=50)
#  player = models.CharField(max_length=50)
#
#def __unicode__(self):
#  return self.leage + " / " + self.team + " / " + self.coach + " / " + self.player
  
class SoccerLeage(models.Model):
  leage_name = models.CharField(max_length=50)
  
def __str__(self):
  return self.leage_name
  
class SoccerTeam(models.Model):
  team_name = models.CharField(max_length=50)
  team_leage_name = models.ForeignKey(SoccerLeage)
  
def __str__(self):
  return self.team_name + " / " + self.team_leage_name
  
class SoccerPeople(models.Model):
  people_coach = models.CharField(max_length=50)
  people_player = models.CharField(max_length=50)
  people_team = models.ForeignKey(SoccerTeam)

def __str__(self):
  return self.people_coach + " / " + self.people_player + " / " + self.people_team
