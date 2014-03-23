# coding: utf-8


def lang(request):
    return {'CURRENT_LANGUAGE': request.LANGUAGE_CODE}
