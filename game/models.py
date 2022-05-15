from django.db.models import Model, CharField


class Game(Model):
    code = CharField(max_length=4)
