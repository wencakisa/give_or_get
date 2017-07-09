from rest_framework import permissions


class IsNotDealItemOwner(permissions.BasePermission):
    message = 'You should not be the owner of the item in order to create a deal.'

    def has_object_permission(self, request, view, obj):
        return request.user != obj.owner


class IsDealBuyer(permissions.BasePermission):
    message = 'You can not perform this action unless you are not a buyer.'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.buyer


class IsDealItemOwner(permissions.BasePermission):
    message = 'You should be the owner of the item in order to modify a deal.'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
