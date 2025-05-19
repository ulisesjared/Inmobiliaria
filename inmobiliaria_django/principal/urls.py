from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('propiedades/', views.propiedades, name='propiedades'),
    path('propiedades_admin/', views.propiedades_admin, name='propiedades_admin'),
    path('agregar_propiedad/', views.agregar_propiedad, name='agregar_propiedad'),
    path('clientes/', views.clientes, name='clientes'),
    path('marketing/', views.marketing, name='marketing'),
    path('documentos/', views.documentos, name='documentos'),
    path('subir_documento/', views.subir_documento, name='subir_documento'),
    path('registro/', views.register_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('propiedades-admin/', views.propiedades_admin, name='propiedades_admin'),
    path('agregar-propiedad/', views.agregar_propiedad, name='agregar_propiedad'),
    path('editar-propiedad/<int:propiedad_id>/', views.editar_propiedad, name='editar_propiedad'),
    path('eliminar-propiedad/<int:propiedad_id>/', views.eliminar_propiedad, name='eliminar_propiedad'),
    path('propiedades-public/', views.propiedades_public, name='propiedades_public'),
    path('eliminar-contacto/<int:contacto_id>/', views.eliminar_contacto, name='eliminar_contacto'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
