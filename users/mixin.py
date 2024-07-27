from django.contrib.auth.models import Permission
from .models import User

# Obtén el usuario al que deseas asignar el permiso
user = User.objects.get(is_superuser=True)



# Obtén el permiso que deseas asignar
permission = Permission.objects.get(codename='user_view')



# Asigna el permiso al usuario
user.user_permissions.add(permission)
