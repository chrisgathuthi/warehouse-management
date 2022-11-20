from rest_framework import permissions

#creating custom permissions
class IsStaffEditorPermissions(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_staff:
            if user.has_perm("shop.view_stock"):#app_name.verb_model_name
                return True
            return False
        return False
   