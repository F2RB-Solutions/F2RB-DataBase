from rest_framework import permissions
from rest_framework.views import View
class IsAdminOrProfessional(permissions.BasePermission):
    def has_permission(self, request, view: View):  
        
        if request.user.is_authenticated:
            user_level = request.user.user_level
            is_superuser = request.user.is_superuser
            return user_level == "professional" or is_superuser or request.method == "GET"
        return False
