# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from random import randint

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from models import Booking
from serializers import BookingSerializer

# Create your views here.


class BookingViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    lookup_field = 'code'

    @action(methods=('POST', ), detail=True)
    def create(self, request, **kwargs):
        # return super(BookingViewSet, self).create(request, **kwargs)
        code = ''.join([
            chr(randint(100, 120)) for i in range(6)
        ])
        booking = Booking.objects.create(code=code)
        return Response({'code': booking.code})
