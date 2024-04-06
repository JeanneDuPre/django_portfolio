from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

urlpatterns= [
    path('', views.random_projects, name='home'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('zukunft/', views.zukunft, name="zukunft"),
    path('vita/', TemplateView.as_view(template_name='vita.html'), name='vita'),
    path('zukunft/', TemplateView.as_view(template_name='zukunft.html'), name='zukunft'),
    path('impressum/', TemplateView.as_view(template_name='impressum.html'), name='impressum')
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)