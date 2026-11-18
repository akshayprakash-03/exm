from rest_framework.permissions import BasePermission


class IsSuperUserOrReadOnly(BasePermission):
    def has_permission(self,request,view):
        if request.method=='GET':
            return True
        else:
            return request.user.is_authenticated

    def has_object_permission(self,request,view,obj):
        return request.user.is_superuser()
