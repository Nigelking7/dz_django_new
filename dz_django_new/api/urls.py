import path
from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import UserModelViewSet, GoodViewSet, StorageViewSet


router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('good', GoodViewSet)
router.register('storage', StorageViewSet)
#router.register('storage\<pk>\tostorage', StorageViewSet.tostorage)






urlpatterns =[
    #path('user/', UserModelViewSet.as_view),
    # Другие URL-пути
]

urlpatterns.extend(router.urls)
