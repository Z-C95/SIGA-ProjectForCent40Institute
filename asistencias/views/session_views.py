from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages


@login_required
def logout_all_devices(request):
    """Eliminar todas las sesiones activas del usuario actual.

    Esto cierra la sesión en otros dispositivos y en el actual (si se desea).
    """
    user = request.user
    deleted = 0
    for s in Session.objects.all():
        try:
            data = s.get_decoded()
        except Exception:
            continue
        if data.get('_auth_user_id') == str(user.id):
            s.delete()
            deleted += 1

    messages.success(request, f'Sesiones cerradas: {deleted}')
    return redirect('asistencias:editar_perfil')
