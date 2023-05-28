import random
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Event(models.Model):
    id_event = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'enterarteapp'


class User(AbstractUser):
    id_user = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    lastname = models.CharField(max_length=100, blank=False)
    username = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)

    groups = models.ManyToManyField(Group, related_name='enterarteapp_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='enterarteapp_users', blank=True)

    class Meta:
        db_table = "User"
        verbose_name = "Date users"
        verbose_name_plural = "Users"

    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username


class UserData(models.Model):
    id_user_data = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    phone = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Permissions(models.Model):
    id_permission = models.AutoField(primary_key=True)
    restrictions = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class EventsData(models.Model):
    id_event_data = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    date = models.DateField()
    photo = models.ImageField(upload_to="Galeria", null=False, blank=False, default=None)
    category = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    province = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    number = models.IntegerField()
    social_networks = models.CharField(max_length=20)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class Events(models.Model):
    id_event = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey('Ticket', related_name='events', on_delete=models.CASCADE)


def generate_random_min_value():
    # Generar un valor mínimo aleatorio entre 10000 y 100250000 (puedes ajustarlo según se requiera)
    return random.randint(10000, 250000)


class Ticket(models.Model):    
    id_ticket = models.IntegerField(
        validators=[MinValueValidator(limit_value=generate_random_min_value), MaxValueValidator(25000000)],
        unique=True
    )
    price = models.DecimalField(max_digits=20, decimal_places=2)
    date_time = models.DateTimeField()
    event = models.ForeignKey(Events, related_name='tickets', on_delete=models.CASCADE)
    
    def clean(self):
        # Realizar la validación de unicidad del número de ticket
        if Ticket.objects.exclude(id=self.id).filter(id_ticket=self.id_ticket).exists():
            raise ValidationError('El número de ticket ya existe.')


class TransactionReport(models.Model):
    id_report = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    order = models.ForeignKey('ShoppingOrder', on_delete=models.CASCADE)


class ShoppingOrder(models.Model):
    id_order = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
            
    
class Roles(models.Model):
    id_rol = models.AutoField(primary_key=True, default=0)
    rol = models.CharField(max_length=15, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permissions, on_delete=models.CASCADE)

