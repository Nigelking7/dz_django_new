from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework import viewsets

from api.serializers import UserSerializer, GoodSerializer, StorageSerializer
from api.models import ApiUser, Good, Storage


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    http_method_names = ['post', "path", "get"]
    serializer_class = UserSerializer


class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer


class StorageViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
"""
class StorageSendToView(viewsets.ModelViewSet):
    def get_queryset(self, request):
        pk = self.kwargs.get('pk')
        try:
            storage = Storage.objects.get(pk=pk)
        except Storage.DoesNotExist:
            return HttpResponse(status=404)
        if request.method == 'POST':
            return storage
        # Логика, использующая значение pk
        # Например, возвращение фильтрованного queryset по значению pk
    # return JsonResponse(serializer.errors, status=400)

"""