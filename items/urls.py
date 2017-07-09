from django.conf.urls import url

from rest_framework import routers
from rest_framework_nested import routers as nested_routers

from .views import DealList, ItemViewSet, DealViewSet


urlpatterns = [
    url(r'^deals/(?P<deal_type>(personal|following))?/$', DealList.as_view(), name='deal-list')
]

items_router = routers.SimpleRouter()
items_router.register(r'items', ItemViewSet, base_name='item')

deals_router = nested_routers.NestedSimpleRouter(items_router, r'items', lookup='item')
deals_router.register(r'deals', DealViewSet, base_name='item-deals')

urlpatterns += items_router.urls
urlpatterns += deals_router.urls
