from django.contrib.auth.models import Permission

from events.core.models import CustomUser


def create_user_with_permission(permissions):
    user = CustomUser.objects.create_user(
        email="somemail@gmail.com", username="someusername", city="somecity", state="somestate"
    )
    user.set_password("somepassword")

    for permission in permissions:
        app_label, codename = permission.split(".")
        permission = Permission.objects.get(codename=codename, content_type__app_label=app_label)

        user.user_permissions.add(permission)

    return user