import os
import sys
import django

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(__file__))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asistencia.settings')

print("=" * 50)
print("Iniciando build de Django para Vercel")
print("=" * 50)

print("\n1. Configurando Django...")
django.setup()
print("✓ Django configurado correctamente")

from django.core.management import call_command

print("\n2. Ejecutando migraciones...")
try:
    call_command('migrate', '--noinput', verbosity=2)
    print("✓ Migraciones ejecutadas correctamente")
except Exception as e:
    print(f"✗ Error en migraciones: {e}")
    raise

print("\n3. Ejecutando collectstatic...")
try:
    call_command('collectstatic', '--noinput', '--clear', verbosity=2)
    print("✓ Archivos estáticos recolectados")
except Exception as e:
    print(f"✗ Error en collectstatic: {e}")
    raise

print("\n4. Creando superusuario...")
try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("✓ Superuser creado: admin / admin123")
    else:
        print("✓ Superuser ya existe")
except Exception as e:
    print(f"⚠ Error creando superuser (no crítico): {e}")

print("\n" + "=" * 50)
print("Build completado exitosamente!")
print("=" * 50)