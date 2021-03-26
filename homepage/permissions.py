from rest_framework import permissions

# This class is to perform the authenication of the registered users to provide necessary permission via tokens.
class IsProfileRegistered(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
