from django.db import models
from users.models import User
from .utils import now_timestamp


# Create your models here.
class Order(models.Model):
    class PizzaType(models.TextChoices):
        MARGHERITA = "Margherita"
        PROSCIUTTO_CRUDO = "Prosciutto Crudo"
        QUATTRO_FORMAGGI = "Quattro Formaggi"
        HAWAII = "Hawaii"
        DIAVOLA = "Diavola"
        TUNA = "Tuna"

    pizza = models.CharField(max_length=50, choices=PizzaType.choices)
    ordered_by = models.OneToOneField(User, on_delete=models.CASCADE)
    ordered_at = models.BigIntegerField(default=now_timestamp)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.pizza


