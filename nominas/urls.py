from django.urls import path
from .views import Inicio, Listado,Crear_Nomina, Crear_Empleado, updateEmpleado,Eliminar
urlpatterns =[
    path("", Inicio,name="inicio"),
    path("listado/", Listado,name="Listado"),
    path("create_nominas/",Crear_Nomina,name="Crear_Nomina"),
    path("crear_empleado/",Crear_Empleado,name="Crear_Empleado"),
    path("update_empleado/<int:id>",updateEmpleado, name="Actualizar_empleado"),
    path("Eliminar_empleado/<int:id>", Eliminar, name="Eliminar")
]