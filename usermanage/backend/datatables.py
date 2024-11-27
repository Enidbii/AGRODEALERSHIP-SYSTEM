import json

from django.db.models import Q, F
from django.http import JsonResponse

from usermanage.backend.utils import get_request_data
from usermanage.models import OtherUser


class Querying(object):
    def query_employees(self, request):
        data = get_request_data(request)
        corporate_id = data.get('corporate_id')
        try:
            q = Q(corporate_id=corporate_id)
            users = OtherUser.objects.filter(q)
            print(users)
            return JsonResponse({"code": "200.000"})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "404.000"})

    def active_users(self, request):
        data = get_request_data(request)
        status_id =data.get('status_id')
        try:
            q = Q(status=status_id)
            users = OtherUser.objects.filter(q)
            print(users)
            return JsonResponse({"code": "200.000"})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "404.000"})



