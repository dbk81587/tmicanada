from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey

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
    views = models.IntegerField(null=True, blank=True, default=0)
    replies = models.IntegerField(null=True, blank=True, default=0)
    name = models.CharField(max_length=10, blank=True)
    date = models.DateField(null=True, blank=True)
    memo = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']


class MPTTComment(MPTTModel):
    board = models.ForeignKey('Board', related_name='commentss', on_delete=models.CASCADE)
    author = models.CharField(max_length=12, blank=True)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    class MPTTMeta:
        # comments on one level will be ordered by date of creation
        order_insertion_by=['created_at']

    class Meta:
        ordering=['author',]