# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics, permissions
from .serializers import RiskListSerializer, RiskDataSerializer
from .authorizations import IsRiskOwner
from .models import Risk

class RiskListView(generics.ListAPIView):
    """This class handles the http requests for a list of risks owned by the user (insurer)."""
    serializer_class = RiskListSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )
    def get_queryset(self):
        """This view returns a list of all the risks for the currently authenticated user."""
        return Risk.objects.filter(insurer=self.request.user)

class RiskDataView(generics.RetrieveAPIView):
    """This class handles the http requests for risk data for a specified risks"""
    queryset = Risk.objects.all()
    serializer_class = RiskDataSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsRiskOwner,
    )
