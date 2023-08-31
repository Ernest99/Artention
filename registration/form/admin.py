from django.contrib import admin
from .models import EventRegistration

class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "address", "dob", "inspiration", "art_works", "signature"]
    search_display = ["name", "email", "phone", "address", "dob", "inspiration", "art_works", "signature"]

admin.site.register(EventRegistration, EventRegistrationAdmin)
