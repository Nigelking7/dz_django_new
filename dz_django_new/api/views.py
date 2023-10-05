from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import UserSerializer, GoodSerializer, StorageSerializer, FromAndToStorageSerializer
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

    @action(detail=True, methods=['post'])
    def fromstorage(self, request, pk=None):
        if request.user.choice == "C":

            data = request.data
            serializer = FromAndToStorageSerializer(data=data)

            if serializer.is_valid():
                good = serializer.validated_data['good']
                quantity = serializer.validated_data['quantity']

                storage_instance = Storage.objects.get(id=pk)
                goods_data = storage_instance.goods
                print(f"Storage ID: {storage_instance.id}")
                print(f"Storage Name: {storage_instance.name}")
                print("Goods Data:")

                if goods_data.get(good, 0) >= quantity:
                    storage_instance.goods[good] -= quantity
                    storage_instance.save()
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                return Response(status=status.HTTP_200_OK)

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    @action(detail=True, methods=['post'])
    def tostorage(self, request, pk=None):
        if request.user.choice == "P":
            data = request.data
            serializer = FromAndToStorageSerializer(data=data)

            if serializer.is_valid():
                good = serializer.validated_data['good']
                quantity = serializer.validated_data['quantity']

                storage_instance = Storage.objects.get(id=pk)
                goods_data = storage_instance.goods
                print(f"Storage ID: {storage_instance.id}")
                print(f"Storage Name: {storage_instance.name}")
                print("Goods Data:")
                print(storage_instance.goods)
                if good not in goods_data:
                    storage_instance.goods[good] = quantity
                    storage_instance.save()
                else:
                    storage_instance.goods[good] += quantity
                    storage_instance.save()
                return Response(status=status.HTTP_200_OK)

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
