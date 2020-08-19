from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView


urlpatterns = [
    path('accounts/', include('accounts.urls')),  # 아인
    url(r"^$", TemplateView.as_view(template_name="index.html"), name="home"),
    path('admin/', admin.site.urls),
    path("membership/", include("membership.urls")),
    path('order/', include('order.urls')),
    path('reviews/', include('reviews.urls')),  # 아인
]
