from django.contrib.auth.models import UserManager


class CustomerManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().exclude(
            is_superuser=True
        ).exclude(
            is_staff=True
        )


class EmployeeManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_staff=True
        ).exclude(
            is_superuser=True
        )


class AdministratorManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_superuser=True
        )
