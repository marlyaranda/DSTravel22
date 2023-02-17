"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from ejemplo.views import (index, saludar_a, sumar, 
                            buscar, monstrar_familiares,
                            BuscarFamiliar, AltaFamiliar,
                            ActualizarFamiliar, BorrarFamiliar,
                            FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar, FamiliarDetalle)
from ejemplo_dos.views import (index, PostDetalle, PostListar, 
                               PostCrear, PostBorrar, PostActualizar,
                               UserSignUp, UserLogin, UserLogout, 
                               AvatarActualizar, UserActualizar, MensajeCrear, MensajeListar, MensajeDetalle, 
                               VueloCrear, VueloDetalle, VueloListar, VueloActualizar, VueloBorrar, VueloComprar, CompraListar )
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('saludar-a/<nombre>/', saludar_a),
    path('sumar/<int:a>/<int:b>/', sumar),
    path('buscar/',buscar),
    path('mi-familia/', monstrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('panel-familia/', FamiliarList.as_view()),
    path('panel-familia/crear', FamiliarCrear.as_view()),
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()),
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()),
    path('panel-familia/<int:pk>/detalle', FamiliarDetalle.as_view()),
    path('success_updated_message/',TemplateView.as_view(template_name="ejemplo/success_updated_message.html")),
    path('dstravel/', index, name="ejemplo-dos-index"),
    path('', index, name="ejemplo-dos-index"),
    path('dstravel/<int:pk>/detalle/', PostDetalle.as_view(), name="ejemplo-dos-detalle"),
    path('dstravel/listar/', PostListar.as_view(), name="ejemplo-dos-listar"),
    path('dstravel/crear/', staff_member_required(PostCrear.as_view()), name="ejemplo-dos-crear"),
    path('dstravel/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="ejemplo-dos-borrar"),
    path('dstravel/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="ejemplo-dos-actualizar"),
    path('dstravel/signup/', UserSignUp.as_view(), name ="ejemplo-dos-signup"),
    path('dstravel/login/', UserLogin.as_view(), name= "ejemplo-dos-login"),
    path('dstravel/logout/', UserLogout.as_view(), name="ejemplo-dos-logout"),
    path('dstravel/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="ejemplo-dos-avatars-actualizar"),
    path('dstravel/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="ejemplo-dos-users-actualizar"),
    path('dstravel/mensajes/crear/', MensajeCrear.as_view(), name="ejemplo-dos-mensajes-crear"),
    path('dstravel/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="ejemplo-dos-mensajes-detalle"),
    path('dstravel/mensajes/listar/', MensajeListar.as_view(), name="ejemplo-dos-mensajes-listar"),
    path('dstravel/vuelos/crear/', staff_member_required(VueloCrear.as_view()), name="vuelocrear"),
    path('dstravel/vuelos/<int:pk>/detalle/', VueloDetalle.as_view(), name="vuelodetalle"),
    path('dstravel/vuelos/listar/', VueloListar.as_view(), name="vuelolistar"),
    path('dstravel/vuelos/<int:pk>/borrar/', staff_member_required(VueloBorrar.as_view()), name="vueloborrar"),
    path('dstravel/vuelos/<int:pk>/actualizar/', staff_member_required(VueloActualizar.as_view()), name="vueloactualizar"),
    path('dstravel/vuelos/<int:pk>/comprar/', staff_member_required(VueloComprar.as_view()), name="vuelocomprar"),
    path('dstravel/comprar/listar/', staff_member_required(CompraListar.as_view()), name="compralistar"),


]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
