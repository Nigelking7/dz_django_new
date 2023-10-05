from rest_framework.routers import DefaultRouter
from api.views import UserModelViewSet, GoodViewSet, StorageViewSet
router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('good', GoodViewSet)
router.register('storage', StorageViewSet)
urlpatterns = []
urlpatterns.extend(router.urls)
