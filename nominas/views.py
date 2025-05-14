from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Empleado, Rol, Cargo, Departamento, TipoContrato
from .forms import RolPago, EmpleadoForms


# Create your views here.
def Inicio(request):
    return render(request,"inicio.jinja")

def Listado(request):
    empleados= Empleado.objects.all()
    nomias = Rol.objects.all()
    return render(request,"listado.jinja",{"empleados":empleados, "nominas":nomias})

def Crear_Empleado(request):
    # formulario = EmpleadoForms() 
    # return render(request, "crear_empleado.jinja", {"formulario":formulario})
    if request.method == "POST":
        formulario = EmpleadoForms(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data["nombre"]
            cedula = formulario.cleaned_data["cedula"]
            sueldo= formulario.cleaned_data["sueldo"]
            direccion = formulario.cleaned_data["direccion"]
            SEXO_CHOICES = dict(Empleado.SEXO_CHOICES)
            sexo_key = formulario.cleaned_data["sexo"] 
            sexo = SEXO_CHOICES[sexo_key]
            cargo = Cargo.objects.get(descripcion=formulario.cleaned_data["cargo"])
            departamento = Departamento.objects.get(descripcion=formulario.cleaned_data["departamento"])
            tipo_contrato = TipoContrato.objects.get(descripcion=formulario.cleaned_data["tipo_contrato"])
            empleado = Empleado(
                nombre= nombre,
                cedula=cedula,
                direccion=direccion,
                sueldo=sueldo,
                sexo=sexo,
                cargo=cargo,
                departamento=departamento,
                tipo_contrato=tipo_contrato
            )
            empleado.save()
            
            return HttpResponseRedirect("/listado/")
    else:
        formulario = EmpleadoForms()
    return render(request,"crear_empleado.jinja", {"formulario":formulario})


            
    

def Crear_Nomina(request):
    if request.method == "POST":
        formulario = RolPago(request.POST)
        if formulario.is_valid():
            empleado = Empleado.objects.get(nombre=formulario.cleaned_data["empleado"])
            aniomes = formulario.cleaned_data["aniomes"]
            horas_extra = formulario.cleaned_data["horas_extra"]
            bono = formulario.cleaned_data["bono"]
            tot_ing = empleado.sueldo + horas_extra + bono
            iess = 0.0945
            tot_des = float(iess) * float(empleado.sueldo)
            neto = float(tot_ing) - float(tot_des)
            rol_pago = Rol(
                empleado = empleado,
                aniomes = aniomes,
                sueldo = empleado.sueldo,
                horas_extra = horas_extra,
                bono = bono,
                iess = iess * float(100),
                tot_ing= tot_ing,
                tot_des = tot_des,
                neto = neto
            )
            rol_pago.save()
            return HttpResponseRedirect("/listado/")
    else:
        formulario = RolPago()
    return render(request,"create_nominas.jinja", {"formulario":formulario})

def updateEmpleado(request, id):
    if request.method == "POST":
        formulario = EmpleadoForms(request.POST, instance= Empleado.objects.get(pk=id))
        if formulario.is_valid():
            empleado=formulario.save(commit=False)
            SEXO_CHOICES = dict(Empleado.SEXO_CHOICES)
            sexo= SEXO_CHOICES[formulario.cleaned_data['sexo']]
            empleado.sexo = sexo
            empleado.save()
            return HttpResponseRedirect("/listado/")
    else:
        empleado = Empleado.objects.get(pk=id)    
        formulario = EmpleadoForms(instance = empleado)
    return render(request, 'update_empleado.jinja',{"formulario":formulario, 'id':id})

def Eliminar(request,id):
    empleado = Empleado.objects.get(pk=id)
    empleado.delete()
    return HttpResponseRedirect("/listado/")

#hola 
#hola lola