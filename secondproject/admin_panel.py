from django.contrib.admin import AdminSite
from django.contrib import admin
from secondproject.models import SecondAdminUser  # Import models for second admin

class SecondProjectAdmin(AdminSite):
    site_header = "Second Project Admin"
    site_title = "Second Project Admin Portal"
    index_title = "Welcome to Second Project Admin Panel"

second_admin_site = SecondProjectAdmin(name="second_admin")

# Register models separately for the second admin panel
second_admin_site.register(SecondAdminUser)  # Add other models if needed
