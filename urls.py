"""
URL configuration.

One Django server now does everything:
  http://127.0.0.1:8000/app/login.html   -> the website (frontend folder)
  http://127.0.0.1:8000/api/...          -> the API
"""

from django.conf import settings
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from django.views.static import serve


def home(request):
    return JsonResponse({
        "message": "Employee Management System API is running successfully!",
        "status": "Success"
    })


# The frontend folder sits next to the backend folder
FRONTEND_DIR = settings.BASE_DIR.parent / 'frontend'


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('employees.urls')),

    # The website
    path('app/', RedirectView.as_view(url='/app/login.html')),
    re_path(r'^app/(?P<path>.*)$', serve, {'document_root': FRONTEND_DIR}),
]