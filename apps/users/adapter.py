from allauth.account.adapter import DefaultAccountAdapter
from allauth.utils import build_absolute_uri
from django.conf import settings

class CustomAccountAdapter(DefaultAccountAdapter):

    def get_email_confirmation_url(self, request, emailconfirmation):
        url = settings.FRONT_END_BASE_URL + "/verify-email/" + "?key=${0}".format(
            emailconfirmation.key
        )
        ret = build_absolute_uri(
            request,
            url)
        return ret
