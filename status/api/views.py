from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework import generics, mixins, permissions
from status.models import Status
from status.api.serializers import StatusSerializers
from django.shortcuts import get_object_or_404
import json
from django.shortcuts import render


class StatusApiDetailView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    # permission_classes = []
    # authentication_classes = [SessionAuthentication]
    serializer_class = StatusSerializers
    queryset = Status.objects.all()
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        print(request.body)
        return self.update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print(request.body)
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def perform_destroy(self, instance):
    #     if instance is not None:
    #         return instance.delete()
    #     return None

    def get_object(self):
        queryset = self.get_queryset()
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        print(self.kwargs[lookup_url_kwarg])
        obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj


class StatusApiListCreateView(mixins.CreateModelMixin, generics.ListAPIView):
    # permission_classes = [] TODO Default is changed in settings
    # authentication_classes = []  TODO Default is changed in settings
    serializer_class = StatusSerializers
    queryset = Status.objects.all()

    def get_queryset(self):
        print(self.request.user)
        print(self.request.user.is_authenticated)
        qs = Status.objects.all()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# class StatusApiView(APIView):
#     permission_classes = []
#     authentication_classes = []
#
#     def get(self, request, format=None):
#         qs = Status.objects.all()
#         if request.GET.get('q'):
#             query = request.GET.get('q')
#             qs = qs.filter(content__contains=query)
#         se = StatusSerializers(qs, many=True)
#         return Response(se.data, status=200)

# # CreateModelMixin is for post
# class StatusApiView(mixins.CreateModelMixin, generics.ListAPIView):
#     http_method_names = ['get', 'options', 'post']
#     permission_classes = []
#     authentication_classes = []
#     serializer_class = StatusSerializers
#
#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__contains=query)
#         return qs
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# # StatusApiView also can create because of the mixin
# class StatusCreateApiView(generics.CreateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializers


# class StatusDetailApiView(APIView):
#     def get(self,request, pk, format=None):
#         obj = Status.objects.get(id=pk)
#         data = StatusSerializers(obj)
#         return Response(data.data) TODO

#
# class StatusDetailApiView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializers
#     lookup_field = 'id'  # the bottom method is better TODO
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#     # def get_object(self, *args, **kwargs):
#     #     kw = self.kwargs.get('id')
#     #     return Status.objects.get(id=kw)


# # StatusDetailApiView can also do Update and Delete TODO
# class StatusUpdateApiView(generics.UpdateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializers
#     lookup_field = 'id'
#
#
# class StatusDeleteApiView(generics.DestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializers
#     lookup_field = 'id'
#     # def perform_destroy(self, instance):


# # This is for all Requests TODO
# class StatusAllRequestsApiView(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
#                                mixins.RetrieveModelMixin, generics.ListAPIView, ):
#     permission_classes = []
#     authentication_classes = []
#     serializer_class = StatusSerializers
#     passed_id = None
#
#     # queryset = Status.objects.all()
#
#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__contains=query)
#         return qs
#
#     def get_object(self):
#         qs = self.get_queryset()
#         passed_id = self.request.GET.get('id', None) or self.passed_id
#         obj = None
#         if passed_id is not None:
#             obj = get_object_or_404(qs, id=passed_id)
#             self.check_object_permissions(self.request, obj)
#         return obj
#
#     def get(self, request, *args, **kwargs):
#         new_passed_id = ''
#         url_passed_id = request.GET.get('id', None)
#         json_data = {}
#         try:
#             json_data = json.loads(request.body)
#             new_passed_id = json_data.get('id', None)
#         except:
#             new_passed_id = None
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id
#         if passed_id is not None:
#             return self.retrieve(request, *args, **kwargs)
#         return super().get(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         new_passed_id = ''
#         url_passed_id = request.GET.get('id', None)
#         json_data = {}
#         try:
#             json_data = json.loads(request.body)
#             new_passed_id = json_data.get('id', None)
#         except:
#             new_passed_id = None
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id
#         return self.update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         new_passed_id = ''
#         url_passed_id = request.GET.get('id', None)
#         json_data = {}
#         try:
#             json_data = json.loads(request.body)
#             new_passed_id = json_data.get('id', None)
#         except:
#             new_passed_id = None
#         requested_id = request.body.get('id')
#         passed_id = url_passed_id or new_passed_id or requested_id or None
#         self.passed_id = passed_id
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         new_passed_id = ''
#         url_passed_id = request.GET.get('id', None)
#         json_data = {}
#         try:
#             json_data = json.loads(request.body)
#             new_passed_id = json_data.get('id', None)
#         except:
#             new_passed_id = None
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id
#         return self.destroy(request, *args, **kwargs)
