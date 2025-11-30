from rest_framework.permissions import BasePermission


class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.role == "ADMIN"


class CustomerPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.role == "CUSTOMER"
