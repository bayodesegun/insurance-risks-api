from rest_framework.permissions import BasePermission
from .models import Risk


class IsRiskOwner(BasePermission):
    """Custom permission class to allow bucketlist owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to to access Risk object."""
        if isinstance(obj, Risk):
            return obj.insurer == request.user
        return obj.insurer == request.user