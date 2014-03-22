from django.conf import settings


class CurrentLanguage(object):
    def process_request(self, request):
        return {'CURRENT_LANGUAGE': settings.LANGUAGE_CODE}
