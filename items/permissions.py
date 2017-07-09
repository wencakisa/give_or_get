from rest_framework import permissions


class IsNotDealItemOwner(permissions.BasePermission):
    message = 'You should not be the owner of the item in order to create a deal.'

    def has_object_permission(self, request, view, obj):
        return request.user != obj.owner
