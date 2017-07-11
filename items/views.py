from rest_framework import viewsets
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from rest_framework.response import Response
from rest_framework import status

from rest_condition.permissions import Not

from .models import Item, Deal
from .serializers import DealReadSerializer, ItemSerializer, DealSerializer
from .permissions import IsDealBuyer, IsItemOwner
from .filters import IsItemOwnerFilterBackend, IsActiveItemFilterBackend, DealTypeFilterBackend


class ItemAbstractAPIView:
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class PersonalItemList(ItemAbstractAPIView, generics.ListAPIView):
    filter_backends = (IsItemOwnerFilterBackend,)


class DealList(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = DealReadSerializer
    filter_backends = (IsActiveItemFilterBackend, DealTypeFilterBackend)
    queryset = Deal.objects.all()


class ItemViewSet(ItemAbstractAPIView, viewsets.ModelViewSet):
    permission_classes_by_action = {
        'list': (IsAuthenticated,),
        'retrieve': (IsAuthenticated,),
        'create': (IsAuthenticated,),
        'update': (IsAuthenticated, IsItemOwner),
        'destroy': (IsAuthenticated, IsItemOwner)
    }

    def get_permissions(self):
        return [
            permission()
            for permission
            in self.permission_classes_by_action[self.action]
        ]

    def create(self, request, *args, **kwargs):
        context = {'request': request}

        serializer = self.serializer_class(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, pk=None):
        item = generics.get_object_or_404(Item, id=pk)
        self.check_object_permissions(request, item)

        serializer = self.get_serializer(item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        headers = self.get_success_headers(serializer.data)

        return Response(serializer.validated_data, status=status.HTTP_200_OK, headers=headers)


class DealViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes_by_action = {
        'list': (IsAuthenticated,),
        'retrieve': (IsAuthenticated,),
        'create': (IsAuthenticated, Not(IsItemOwner)),
        'update': (IsAuthenticated, IsDealBuyer),
        'destroy': (IsAuthenticated, IsItemOwner)
    }
    serializer_class = DealSerializer

    def get_permissions(self):
        return [
            permission()
            for permission
            in self.permission_classes_by_action[self.action]
        ]

    def get_queryset(self):
        item_pk = self.kwargs.get('item_pk')
        item = generics.get_object_or_404(Item, id=item_pk)

        return item.deal_set

    def create(self, request, item_pk=None, *args, **kwargs):
        item = generics.get_object_or_404(Item, id=item_pk)
        self.check_object_permissions(request, item)

        context = {'request': request, 'item': item}

        serializer = self.serializer_class(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, item_pk=None, pk=None):
        item = generics.get_object_or_404(Item, id=item_pk)
        self.check_object_permissions(request, item)

        deal = generics.get_object_or_404(item.deal_set, id=pk)
        deal.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
