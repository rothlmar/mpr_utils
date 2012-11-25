from django.conf import settings
from django.contrib.auth.models import User
import requests, json

class PersonaBackend(object):

    def authenticate(self,assertion='',secure=False):
        audience = 'https://' if secure else 'http://'
        port = '443' if secure else '80'
        if secure and hasattr(settings,'PERSONA_SECURE_PORT'):
            port = settings.PERSONA_SECURE_PORT
        elif hasattr(settings,'PERSONA_PORT'):
            port = settings.PERSONA_PORT
        audience += settings.PERSONA_HOSTNAME + ':' + port
        data = {'assertion': assertion, 'audience': audience}
        resp = requests.post('https://verifier.login.persona.org/verify', data=data, verify=True)

        if resp.ok:
            verification_data = json.loads(resp.content)
            try:
                user = User.objects.get(username=verification_data['email'])
            except User.DoesNotExist:
                user = User(username=verification_data['email'],email=verification_data['email'])
                user.save()
            return user
        return None

    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
