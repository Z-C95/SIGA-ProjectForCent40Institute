import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asistencias.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser creado: admin / admin123')
else:
    print('Superuser ya existe.')
