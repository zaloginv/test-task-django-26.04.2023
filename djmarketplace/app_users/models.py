from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    gold = 100_000
    silver = 50_000

    STATUS_CHOICES = [
        ('bronze', 'Bronze'),
        ('silver', 'Silver'),
        ('gold', 'Gold'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, blank=True, decimal_places=2, max_digits=8,
                                  validators=[MinValueValidator(0)])
    status = models.CharField(choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0], max_length=10)
    purchases_sum = models.DecimalField(default=0, blank=True, decimal_places=2, max_digits=10,
                                  validators=[MinValueValidator(0)])
