from django.contrib import admin
from contact.models import Contact, Category

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email', 'category', 'show', )
    ordering = ('-id'),
    search_fields = ('id', 'first_name', 'last_name',)
    list_per_page = 10
    list_max_show_all = 200
    list_editable = ('show',)
    list_display_links = ('first_name', 'last_name', 'id', ) #Link para abrir a edição (padrao é no ID)
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('-id'),
    