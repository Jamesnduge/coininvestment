from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    url(r'home$', views.home, name='home'),
    url(r'about$',views.about, name='about'),
    url(r'plans$',views.plans, name='plans'),
    url(r'contact$',views.contact, name='contact'),
    url(r'^$',views.signup, name='signup'),
    url(r'logout$', views.logout, name='logout'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
]

