from django.contrib import admin 
from django.contrib.auth.models import Group #import for Group model in the admin area

# Register your models here.
from .models import Contact #registers the contact in the admin area

#class for customizing our admin model 
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'email', 'info', 'phone')
    list_display_links = ('id', 'name')
    list_editable = ('info',)
    list_per_page = 10
    search_fields = ('name', 'gender', 'email', 'info', 'phone')
    list_filter = ('gender', 'data_added')


admin.site.register(Contact, ContactAdmin) #registers the Contact model and its customization class in the admin area

admin.site.unregister(Group) #unregisters the Group model in the admin area


