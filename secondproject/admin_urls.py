from django.urls import path
from secondproject.admin_panel import second_admin_site  # Import second admin site

urlpatterns = [
    path("", second_admin_site.urls),  # Ensure this loads the second admin panel
]
