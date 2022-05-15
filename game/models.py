from django.db.models import Model, CharField


# Create your models here.
class Game(Model):
    code = CharField(max_length=4)
