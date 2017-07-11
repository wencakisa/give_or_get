from rest_framework import permissions


class IsDealBuyer(permissions.BasePermission):
    message = 'You can not perform this action unless you are not a buyer.'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.buyer


class IsItemOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
