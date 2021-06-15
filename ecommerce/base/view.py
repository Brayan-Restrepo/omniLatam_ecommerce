# -*- coding: utf-8 -*-

import json

from django.urls import reverse

from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.metadata import SimpleMetadata
from .decorators import permission

class BaseViewSet(viewsets.ModelViewSet):

    # Nombre de la aplicación.
    app_code = None
    permission_code = None
    # Cuales metodos tendran acceso libre.
    # ['list', 'add', 'retrieve', 'change', 'delete']
    free_access : list = []
    # Cuales metodos estan prohibidos.
    # ['list', 'add', 'retrieve', 'change', 'delete']
    deny_access : list = []

    def initialize_request(self, request, *args, **kwargs):
        return super().initialize_request(request, *args, **kwargs)

    @api_view(['post'])
    def info(self, request):

        simple_metadata = SimpleMetadata()
        metedata = simple_metadata.determine_metadata(request, self)
        metedata_serializer = {}
        metedata_serializer['fields'] = metedata['actions']['POST']
        metedata_serializer['name'] = metedata['name']
        metedata_serializer['description'] = metedata['description']

        try:
            new_info_data = json.loads(json.dumps(self.serializer_class.info_data))
        except AttributeError as error:
            new_info_data = {}

        for key, value in new_info_data['fields'].items():
            if key in metedata_serializer['fields']:

                # Filtros.
                try:
                    metedata_serializer['fields'][key]['filters'] = self.filter_class.Meta.fields[key]
                except KeyError:
                    pass

                # Ordenamiento.
                metedata_serializer['fields'][key]['ordering'] = True if key in self.ordering_fields else False

                try:
                    for choice in metedata_serializer['fields'][key]['choices']:
                        choice['label'] = choice['display_name']
                except KeyError:
                    pass

                if 'source' in value:
                    value['source']['url'] = request.build_absolute_uri(reverse(value['source']['url']))
                metedata_serializer['fields'][key].update(value)

        metedata_serializer['order'] = new_info_data['order']

        return Response(metedata_serializer)

    @permission('list')
    def list(self, request):
        if request.GET.get('nopaginate'):
            self.pagination_class = None
        return super().list(request)
    
    @permission('add')
    def create(self, request):
        return super().create(request)

    @permission('retrieve')
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk)

    @permission('change')
    def update(self, request, pk=None):
        return super().update(request, pk)

    @permission('change')
    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk)
    
    @permission('delete')
    def destroy(self, request, pk=None):
        return super().destroy(request, pk)
