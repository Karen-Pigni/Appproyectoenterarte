from django.db import models

class Eventos(models.Model):
    idEvento = models.IntegerField(primary_key=True)
    idUser = models.IntegerField(null=True)
    idTicket = models.IntegerField(null=True)

    class Meta:
        db_table = 'eventos'

class EventosData(models.Model):
    idEventoData = models.IntegerField(primary_key=True)
    idEvento = models.IntegerField(null=True)
    titulo = models.CharField(max_length=255, null=True)
    descripcion = models.CharField(max_length=255, null=True)
    fecha = models.DateField(null=True)
    foto = models.BinaryField(null=True)
    categoria = models.CharField(max_length=20, null=True)
    genero = models.CharField(max_length=20, null=True)
    provincia = models.CharField(max_length=20, null=True)
    localidad = models.CharField(max_length=20, null=True)
    calle = models.CharField(max_length=30, null=True)
    numero = models.CharField(max_length=10, null=True)
    rss = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'eventos_data'

class Permisos(models.Model):
    idPermiso = models.IntegerField(primary_key=True)
    idUser = models.IntegerField(null=True)
    restricciones = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'permisos'

class Roles(models.Model):
    idRol = models.IntegerField(primary_key=True)
    idUser = models.IntegerField(null=True)
    rol = models.CharField(max_length=25, null=True)

    class Meta:
        db_table = 'roles'

class Ticket(models.Model):
    idTicket = models.IntegerField(primary_key=True)
    idEvento = models.IntegerField(null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    fechayhora = models.DateTimeField(null=True)

    class Meta:
        db_table = 'ticket'

class UserData(models.Model):
    idUserData = models.IntegerField(primary_key=True)
    idUser = models.IntegerField()
    nombres = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fechaNac = models.DateField()
    tel = models.CharField(max_length=15)

    class Meta:
        db_table = 'user_data'

class Users(models.Model):
    idUser = models.IntegerField(primary_key=True)
    idUserData = models.IntegerField(null=True)
    idPermiso = models.IntegerField(null=True)
    idRol = models.IntegerField(null=True)
    email = models.CharField(max_length=40, null=True)
    password = models.CharField(max_length=40, null=True)

    class Meta:
        db_table = 'users'
