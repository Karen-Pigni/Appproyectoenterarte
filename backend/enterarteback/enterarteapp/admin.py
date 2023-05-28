from django.contrib import admin
from .models import Event, User, UserData, Permissions, EventsData, Events, Ticket, TransactionReport, ShoppingOrder, Roles


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id_event', 'title', 'description', 'location', 'price', 'user')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'name', 'lastname', 'username', 'password')


@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ('id_user_data', 'name', 'last_name', 'birthday', 'phone', 'user')


@admin.register(Permissions)
class PermissionsAdmin(admin.ModelAdmin):
    list_display = ('id_permission', 'restrictions', 'user')


@admin.register(EventsData)
class EventsDataAdmin(admin.ModelAdmin):
    list_display = ('id_event_data', 'title', 'description', 'date', 'photo', 'category', 'gender', 'province', 'location',
                    'street', 'number', 'social_networks', 'event')


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('id_event', 'user', 'ticket')


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id_ticket', 'price', 'date_time', 'event')


@admin.register(TransactionReport)
class TransactionReportAdmin(admin.ModelAdmin):
    list_display = ('id_report', 'user', 'event', 'order')


@admin.register(ShoppingOrder)
class ShoppingOrderAdmin(admin.ModelAdmin):
    list_display = ('id_order', 'price', 'date_time', 'user', 'event')


@admin.register(Roles)
class RolesAdmin(admin.ModelAdmin):
    list_display = ('id_rol', 'rol', 'user', 'permission')
