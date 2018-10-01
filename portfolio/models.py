from django.db import models
from django.forms import ModelForm

# Create your models here.
class Board(models.Model):
    LOCATION_CHOICES = (
        ('Canada', 'Canada'),
        ('AB', 'AB'),
        ('BC', 'BC'),
        ('MB', 'MB'),
        ('NB', 'NB'),
        ('NS', 'NS'),
        ('ON', 'ON'),
        ('PEI', 'PEI'),
        ('QB', 'QB'),
        ('SK', 'SK'),
        ('Territories','Territories')
    )
    location = models.CharField(
        max_length=50,
        choices=LOCATION_CHOICES,
        blank=True,
        default='Canada',
        help_text='Location',
    )
    title = models.CharField(max_length=100, blank=True)
    views = models.IntegerField(null=True, blank=True)
    replies = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=10, blank=True)
    date = models.DateField(null=True, blank=True)
    memo = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

   

    class Meta:
        ordering = ['-id']