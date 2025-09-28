from django.urls import include, path

urlpatterns = [
    path('employees/', include('employees.api.urls')),
]
