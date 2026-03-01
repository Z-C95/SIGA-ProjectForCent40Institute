from django.conf import settings
from django.contrib.auth.views import LoginView
from django.utils import timezone


class CustomLoginView(LoginView):
    """LoginView que soporta el checkbox `remember_me` en la plantilla.

    Si `remember_me` está marcado la sesión se mantiene por
    `settings.SESSION_COOKIE_AGE`. Si no, la sesión expira al cerrar
    el navegador (`set_expiry(0)`).
    """

    template_name = "registration/login.html"

    def form_valid(self, form):
        remember = self.request.POST.get("remember_me")
        if remember:
            # Mantener sesión por el tiempo configurado
            self.request.session.set_expiry(settings.SESSION_COOKIE_AGE)
        else:
            # Expira al cerrar el navegador
            self.request.session.set_expiry(0)

        # Ejecutar el login estándar y luego registrar el último acceso
        response = super().form_valid(form)

        try:
            user = self.request.user
            # Actualizamos el campo `last_login` explícitamente
            user.last_login = timezone.now()
            user.save(update_fields=["last_login"]) 
        except Exception:
            # No bloquear el flujo de login por errores al guardar
            pass

        return response
