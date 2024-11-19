from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from .models import *
from .forms import *

# Create your views here.
def inicio_sesion(request):
    if request.method == 'GET':
        return render(request, 'inicio_sesion.html', {'form': AuthenticationForm()})

    elif request.method == 'POST':
        email = request.POST.get('email', '').lower()
        password = request.POST.get('password', '')

        try:
            # Buscar al usuario por correo
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user and user.check_password(password):
            login(request, user)
            return redirect('pagina_principal')
        else:
            return render(request, 'inicio_sesion.html', {
                'form': AuthenticationForm(),
                'error': 'Correo o contraseña incorrectos.'
            })

def cerrar_sesion(request):
    logout(request)
    return redirect('pagina_principal')


# def crear_cuenta(request):
#     if request.method == 'GET':
#         return render(request, 'crear_cuenta.html', {'form': UserCreationForm()})

#     if request.method == 'POST':
#         form_data = {
#             'apellidop': request.POST.get('apellidop', '').lower(),
#             'apellidom': request.POST.get('apellidom', '').lower(),
#             'nombres': request.POST.get('nombres', '').lower(),
#             'dni': request.POST.get('dni', ''),
#             'email': request.POST.get('email', '').lower(),
#             'password1': request.POST.get('password1', ''),
#             'password2': request.POST.get('password2', ''),
#         }

#         nombre_completo = f"{form_data['apellidop']} {form_data['apellidom']} {form_data['nombres']}".lower()
#         nombre_completo_ordenado = f"{form_data['nombres']} {form_data['apellidop']} {form_data['apellidom']}".lower()
#         is_valid, nombre_lista_reniec = validate_dni(form_data['dni'])
        
#         if is_valid:
#             apellido_paterno, apellido_materno, nombres_juntos = map(str.lower, nombre_lista_reniec)
#             nombre_reniec = f"{apellido_paterno} {apellido_materno} {nombres_juntos}"
#             correo_edu = f"{nombres_juntos[0]}{apellido_paterno}{apellido_materno[0]}@certus.edu.pe"
#             print(f'correo_edu = {correo_edu}')
#             print('email = ',form_data['email'])
#         else:
#             return render(request, 'crear_cuenta.html', {
#                 'form': UserCreationForm(),
#                 'error': 'DNI inválido o no encontrado en RENIEC.'
#             })

#         # Validaciones
#         errors = []

#         # Validar el formato de DNI
#         if len(form_data['dni']) != 8 or not form_data['dni'].isdigit():
#             errors.append('Ingresar un DNI válido.')

#         # Comparar nombres completos con RENIEC
#         if nombre_completo != nombre_reniec:
#             errors.append('Los nombres y apellidos no coinciden con RENIEC.')

#         # Validar el formato del correo institucional
#         if form_data['email'] != correo_edu:
#             errors.append('Correo institucional inválido.')

#         # Verificar que las contraseñas coincidan
#         if form_data['password1'] != form_data['password2']:
#             errors.append('Las contraseñas no coinciden.')

#         if errors:
#             return render(request, 'crear_cuenta.html', {
#                 'form': UserCreationForm(),
#                 'error': ' '.join(errors)
#             })

#         # Crear el usuario si todas las validaciones pasan
#         try:
#             user = User.objects.create_user(
#                 username=nombre_completo_ordenado,
#                 email=correo_edu,
#                 password=form_data['password1'],
#                 first_name=form_data['nombres'],
#                 last_name=f"{form_data['apellidop']} {form_data['apellidom']}"
#             )
#             login(request, user)
#             return redirect('pagina_principal')
#         except IntegrityError:
#             return render(request, 'crear_cuenta.html', {
#                 'form': UserCreationForm(),
#                 'error': 'El nombre de usuario ya existe.'
#             })

#     return render(request, 'crear_cuenta.html', {'form': UserCreationForm()})
    

def crear_cuenta(request):
    if request.method == 'GET':
        return render(request, 'crear_cuenta.html', {'form': UserCreationForm()})

    if request.method == 'POST':
        form_data = {
            'tipo_usuario': request.POST.get('tipo_usuario').lower(),
            'nombres': request.POST.get('nombres', '').lower(),
            'apellidop': request.POST.get('apellidop', '').lower(),
            'apellidom': request.POST.get('apellidom', '').lower(),
            'dni': request.POST.get('dni', ''),
            'email': request.POST.get('email', '').lower(),
            'password1': request.POST.get('password1', ''),
            'password2': request.POST.get('password2', ''),
        }

        tipo_usuario = form_data['tipo_usuario'].lower()
        nombre_completo = f"{form_data['apellidop']} {form_data['apellidom']} {form_data['nombres']}".lower()
        nombre_completo_ordenado = f"{form_data['nombres']} {form_data['apellidop']} {form_data['apellidom']}".lower()
        is_valid, nombre_lista_reniec = validate_dni(form_data['dni'])
        
        if is_valid:
            if tipo_usuario == "opcion1":
                print("estudiante")
                apellido_paterno, apellido_materno, nombres_juntos = map(str.lower, nombre_lista_reniec)
                nombre_reniec = f"{apellido_paterno} {apellido_materno} {nombres_juntos}"
                correo_edu = f"{form_data['dni']}@certus.edu.pe"
                print(f'correo_edu = {correo_edu}')
                print('email = ',form_data['email'])
            else:
                print("profesor")
                apellido_paterno, apellido_materno, nombres_juntos = map(str.lower, nombre_lista_reniec)
                nombre_reniec = f"{apellido_paterno} {apellido_materno} {nombres_juntos}"
                correo_edu = f"{nombres_juntos[0]}{apellido_paterno}{apellido_materno[0]}@certus.edu.pe"
                print(f'correo_edu = {correo_edu}')
                print('email = ',form_data['email'])
        else:
            return render(request, 'crear_cuenta.html', {
                'form': UserCreationForm(),
                'error': 'DNI inválido o no encontrado en RENIEC.'
            })

        # Validaciones
        errors = []

        # Validar el formato de DNI
        if len(form_data['dni']) != 8 or not form_data['dni'].isdigit():
            errors.append('Ingresar un DNI válido.')

        # Comparar nombres completos con RENIEC
        if nombre_completo != nombre_reniec:
            errors.append('Los nombres y apellidos no coinciden con RENIEC.')

        # Validar el formato del correo institucional
        if form_data['email'] != correo_edu:
            errors.append('Correo institucional inválido.')

        # Verificar que las contraseñas coincidan
        if form_data['password1'] != form_data['password2']:
            errors.append('Las contraseñas no coinciden.')

        if errors:
            return render(request, 'crear_cuenta.html', {
                'form': UserCreationForm(),
                'error': ' '.join(errors)
            })

        # Crear el usuario si todas las validaciones pasan
        try:
            user = User.objects.create_user(
                username=nombre_completo_ordenado,
                email=correo_edu,
                password=form_data['password1'],
                first_name=form_data['nombres'],
                last_name=f"{form_data['apellidop']} {form_data['apellidom']}"
            )
            login(request, user)
            return redirect('pagina_principal')
        except IntegrityError:
            return render(request, 'crear_cuenta.html', {
                'form': UserCreationForm(),
                'error': 'El nombre de usuario ya existe.'
            })

    return render(request, 'crear_cuenta.html', {'form': UserCreationForm()})


def validate_dni(dni):
    # Verificar si el DNI tiene 8 dígitos y es numérico
    if len(dni) != 8 or not dni.isdigit():
        return False, "DNI inválido: debe tener 8 dígitos"

    # Configuración de Selenium para buscar el DNI en eldni.com
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Modo headless para evitar mostrar el navegador
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    driver = None
    try:
        # Inicializar el navegador
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://eldni.com/')

        # Esperar hasta que el campo de DNI esté disponible
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'dni'))
        )

        # Ingresar el DNI y realizar la búsqueda
        dni_input = driver.find_element(By.ID, 'dni')
        dni_input.clear()
        dni_input.send_keys(dni)

        btn_buscar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn-buscar-datos-por-dni'))
        )
        btn_buscar.click()

        # Esperar a que los datos sean cargados en la página
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'nombres'))
        )

        # Extraer el contenido de la página
        response = driver.page_source
        soup = BeautifulSoup(response, 'html.parser')

        # Extraer los datos del formulario
        apellidop = soup.find('input', {'id': 'apellidop'})['value'].strip()
        apellidom = soup.find('input', {'id': 'apellidom'})['value'].strip()
        nombres = soup.find('input', {'id': 'nombres'})['value'].strip()

        # Verificar que los datos se hayan obtenido correctamente
        if not (apellidop and apellidom and nombres):
            return False, "No se encontraron datos válidos para el DNI ingresado"

        nombre_lista_reniec = [apellidop, apellidom, nombres]
        print(f"Datos extraídos: {nombre_lista_reniec}")
        return True, nombre_lista_reniec

    except Exception as e:
        print(f"Error al validar DNI: {e}")
        return False, "Ocurrió un error al validar el DNI"

    finally:
        if driver:
            driver.quit()


# def perfil_usuario_actual(request):
#     perfil = request.user.perfil  # Obtener el perfil asociado al usuario logueado

#     if request.method == "POST":
#         descripcion = request.POST.get('descripcion')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')

#         # Actualizar descripción
#         perfil.descripcion = descripcion
#         perfil.save()

#         # Actualizar contraseña si ambas coinciden
#         if password1 and password1 == password2:
#             perfil.actualizar_password(password1)
#         elif password1 != password2:
#             messages.error(request, "Las contraseñas no coinciden.")

#         messages.success(request, "Perfil actualizado con éxito.")
#         return redirect('perfil')

#     return render(request, 'perfil_usuario_actual.html', {'perfil': perfil})

@login_required
def perfil_usuario_actual(request):
    usuario = request.user  # Obtienes el usuario autenticado
    return render(request, 'perfil_usuario_actual.html', {'usuario': usuario})


@login_required
def editar_perfil(request):
    # Obtiene el perfil del usuario actual
    perfil = MiPerfil.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()  # Guarda los cambios en el perfil
            return redirect('perfil')  # Redirige a una vista donde el usuario pueda ver su perfil
    else:
        form = PerfilForm(instance=perfil)  # Si es GET, pre-carga el formulario con los datos actuales
    
    return render(request, 'editar_perfil.html', {'form': form})