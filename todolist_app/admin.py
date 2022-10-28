from django.contrib import admin
from todolist_app.models import Priority, Todo

# Register your models here.
admin.site.register(Todo)
admin.site.register(Priority)