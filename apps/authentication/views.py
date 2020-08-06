from rest_auth.views import (
    LoginView as BaseLoginView, LogoutView as BaseLogoutView,
    PasswordChangeView as BasePasswordChangeView,
    PasswordResetView as BasePasswordResetView,
    PasswordResetConfirmView as BasePasswordResetConfirmView,
    UserDetailsView as BaseUserDetailsView
)
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class LoginView(BaseLoginView):
    authentication_classes = (JSONWebTokenAuthentication, )

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class LogoutView(BaseLogoutView):
    pass


class PasswordChangeView(BasePasswordChangeView):
    pass


class PasswordResetView(BasePasswordResetView):
    pass


class PasswordResetConfirmView(BasePasswordResetConfirmView):
    pass


class UserDetailsView(BaseUserDetailsView):
    pass
