from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

from synchronise import synchronise

import json


class SynchroniseView(View):


    @csrf_exempt
    def post(self, request, *args, **kwargs):
        """
        Handle the synchronise request.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            payload = request.POST['payload']
            print("POST: {}".format(request.POST))
            post = json.loads(payload)
            return synchronise.handle_post(post)
        except KeyError as ke:
            return HttpResponse("Post contains invalid JSON.\n",
                                status=400)
