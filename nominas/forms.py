from django.forms import ModelForm, ModelChoiceField, DateField, DecimalField, fields, DateInput, CharField
from nominas.models import Empleado, Rol, Cargo, Departamento, TipoContrato
class RolPago(ModelForm):
    empleado = ModelChoiceField(
        queryset = Empleado.objects.all(),
        label = "Empleado",
        empty_label="Selecciones el empleado"

    )
    aniomes= DateField(label="Año y mes", widget=DateInput(attrs={'type':'date'}))
    horas_extra = DecimalField(label="Horas extras")
    bono = DecimalField(label="Bono")
    

    class Meta:
        model = Rol
        fields =["empleado", "aniomes", "horas_extra", "bono"]

class EmpleadoForms(ModelForm):
    nombre = CharField(label = "Nombre")
    cedula = CharField(label= "Cedula")
    direccion = CharField(label = "Direccion")
    sueldo = DecimalField(label ="Sueldo")
    cargo = ModelChoiceField(
        queryset =Cargo.objects.all(),
        label = "Cargo",
        empty_label = "Seleccione su cargo"
    )
    departamento = ModelChoiceField(
        queryset= Departamento.objects.all(),
        label= "Departamento",
        empty_label = "Seleccione su departamento"
    )
    tipo_contrato = ModelChoiceField(
        queryset= TipoContrato.objects.all(),
        label= "Contrato",
        empty_label = "Seleccione su Contrato"
    )
    class Meta:
        model = Empleado
        fields = ["nombre","cedula","direccion","sexo","sueldo","cargo","departamento","tipo_contrato"]

