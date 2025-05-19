from django.shortcuts import render, redirect, get_object_or_404
from .models import Propiedad,Contacto,Documento
from .forms import PropiedadForm
from .forms import ContactoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User

def index(request):
    return render(request, 'principal/index.html')


def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contacto/?enviado=1')  # 👈 redirige con bandera
    else:
        form = ContactoForm()
    return render(request, 'principal/contacto.html', {'form': form})



def propiedades(request):
    return render(request, 'principal/propiedades.html')

# Vista para gestionar propiedades (admin)
@user_passes_test(lambda u: u.is_superuser)
def propiedades_admin(request):
    propiedades = Propiedad.objects.all()
    return render(request, 'principal/propiedades_admin.html', {'propiedades': propiedades})



# Vista para agregar propiedad
def agregar_propiedad(request):
    if request.method == 'POST':
        form = PropiedadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('propiedades_admin')
    else:
        form = PropiedadForm()
    return render(request, 'principal/agregar_propiedad.html', {'form': form})

def clientes(request):
    contactos = Contacto.objects.all().order_by('-id')
    return render(request, 'principal/clientes.html', {'contactos': contactos})

def documentos(request):
    return render(request, 'principal/documentos.html')

def subir_documento(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        ubicacion = request.POST.get('ubicacion')
        tipo = request.POST.get('tipo')
        archivo = request.FILES.get('documento')

        if nombre and ubicacion and tipo and archivo:
            Documento.objects.create(
                nombre=nombre,
                ubicacion=ubicacion,
                tipo=tipo,
                documento=archivo
            )
            return redirect('/subir_documento/?enviado=1')
    return render(request, 'principal/subir_documento.html')

def registro(request):
    return render(request, 'principal/registro.html')


@login_required
def marketing(request):
    return render(request, 'principal/marketing.html')



# Vista para propiedades públicas

def propiedades_public(request):
    propiedades = Propiedad.objects.all()
    ubicacion = request.GET.get('ubicacion')
    tipo = request.GET.get('tipo')
    tipo_inmueble = request.GET.get('tipo_inmueble')
    recamaras = request.GET.get('recamaras')

    if ubicacion:
        propiedades = propiedades.filter(ubicacion__icontains=ubicacion)

    if tipo:
        propiedades = propiedades.filter(tipo_compra=tipo)

    if tipo_inmueble:
        propiedades = propiedades.filter(tipo_inmueble=tipo_inmueble)

    if recamaras:
        propiedades = propiedades.filter(numero_recamaras__gte=recamaras)
    return render(request, 'principal/propiedades.html', {'propiedades': propiedades})


# Crear nueva propiedad
def agregar_propiedad(request):
    if request.method == 'POST':
        form = PropiedadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('propiedades_admin')
    else:
        form = PropiedadForm()
    return render(request, 'principal/agregar_propiedad.html', {'form': form})

# Editar propiedad
# Editar Propiedad
def editar_propiedad(request, propiedad_id):
    propiedad = get_object_or_404(Propiedad, id=propiedad_id)

    if request.method == 'POST':
        propiedad.titulo = request.POST['titulo']
        propiedad.descripcion = request.POST['descripcion']
        propiedad.ubicacion = request.POST['ubicacion']
        propiedad.precio = request.POST['precio']

        if 'foto_principal' in request.FILES:
            propiedad.foto_principal = request.FILES['foto_principal']

        propiedad.save()
        return redirect('propiedades_admin')

    return render(request, 'principal/editar_propiedad.html', {'propiedad': propiedad})

# Eliminar Propiedad
def eliminar_propiedad(request, propiedad_id):
    propiedad = get_object_or_404(Propiedad, id=propiedad_id)
    propiedad.delete()
    return redirect('propiedades_admin')

# Vista de login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']  # Cambiado de 'email' a 'username'
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')  # Redirige donde desees
        else:
            messages.error(request, 'Credenciales incorrectas. Por favor, intenta de nuevo.')

    return render(request, 'principal/login.html')

# Vista de registro de usuario normal
def register_view(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        telefono = request.POST['telefono']  # Guardaremos este dato después en perfil extendido si quieres
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']

        if password == confirm_password:
            if User.objects.filter(username=email).exists():
                return render(request, 'principal/registro.html', {'error': 'El correo ya está registrado.'})
            else:
                user = User.objects.create_user(username=email, email=email, password=password, first_name=nombre)
                user.save()
                return redirect('login')  # Redirigimos al login después de registrar
        else:
            return render(request, 'principal/registro.html', {'error': 'Las contraseñas no coinciden.'})

    return render(request, 'principal/registro.html')

# Vista de logout
def logout_view(request):
    logout(request)
    return redirect('index')


def eliminar_contacto(request, contacto_id):
    contacto = get_object_or_404(Contacto, id=contacto_id)
    contacto.delete()
    messages.success(request, 'Contacto eliminado correctamente.')
    return redirect('clientes')  

def documentos(request):
    nombre = request.GET.get('nombre', '').strip()
    tipo = request.GET.get('tipo', '')
    ubicacion = request.GET.get('ubicacion', '')

    documentos = Documento.objects.all()

    if nombre:
        documentos = documentos.filter(nombre__icontains=nombre)
    if tipo:
        documentos = documentos.filter(tipo=tipo)
    if ubicacion:
        documentos = documentos.filter(ubicacion=ubicacion)

    context = {
        'documentos': documentos,
        'nombre': nombre,
        'tipo': tipo,
        'ubicacion': ubicacion,
    }
    return render(request, 'principal/documentos.html', context)
