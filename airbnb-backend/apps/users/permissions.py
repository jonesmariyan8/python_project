from rest_framework import permissions

class IsHost(permissions.BasePermission):
    """
    Custom permission to only allow hosts to edit their own listings.
    """

    def has_object_permission(self, request, view, obj):
        return obj.host == request.user

class IsGuest(permissions.BasePermission):
    """
    Custom permission to only allow guests to book listings.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_guest

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners to manage their own bookings.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user