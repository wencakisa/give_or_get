from rest_framework import viewsets
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from rest_framework.response import Response
from rest_framework import status

from .models import Item, Deal
from .serializers import ItemSerializer, DealSerializer
from .permissions import IsNotDealItemOwner, IsDealBuyer, IsDealItemOwner
from .filters import IsActiveFilterBackend, DealTypeFilterBackend


class DealList(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = DealSerializer
    filter_backends = (IsActiveFilterBackend, DealTypeFilterBackend)
    queryset = Deal.objects.all()


class ItemViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.filter(owner=self.request.user)


class DealViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes_by_action = {
        'list': (IsAuthenticated,),
        'retrieve': (IsAuthenticated,),
        'create': (IsAuthenticated, IsNotDealItemOwner),
        'update': (IsAuthenticated, IsDealBuyer),
        'destroy': (IsAuthenticated, IsDealItemOwner)
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

    def create(self, request, item_pk=None):
        item = generics.get_object_or_404(Item, id=item_pk)
        self.check_object_permissions(request, item)

        context = {'request': request, 'item': item}

        serializer = self.serializer_class(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED, headers=headers)
