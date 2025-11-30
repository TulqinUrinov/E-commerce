from rest_framework.permissions import BasePermission


# class IsJWTAuthenticated(BasePermission):
#     """
#     Faqat middleware orqali authenticate bo'lgan user lar uchun
#     """
#
#     def has_permission(self, request, view):
#         return bool(request.user and request.role)


class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.role == "ADMIN"


class CustomerPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.role == "CUSTOMER"
