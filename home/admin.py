from django.contrib import admin
from .models import AdmissionEnquiry

@admin.register(AdmissionEnquiry)
class AdmissionEnquiryAdmin(admin.ModelAdmin):
    list_display = ('parent_name', 'phone', 'email', 'program', 'submitted_at')
    list_filter = ('program', 'submitted_at')
    search_fields = ('parent_name', 'phone', 'email')
    readonly_fields = ('submitted_at',)
