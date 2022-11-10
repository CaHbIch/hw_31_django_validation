from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models.selection import Selection
from ads.permissions.selection import IsCreatedBy
from ads.serializers.selection import SelectionSerializer, SelectionCreateSerializer, SelectionUpdateSerializer


class SelectionListView(ListAPIView):
    """Отобразить все выборки"""
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer


class SelectionDetailView(RetrieveAPIView):
    """Показать выборку по id"""
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer


class SelectionCreateView(CreateAPIView):
    """Создать новый выборку"""
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateSerializer
    permission_classes = [IsAuthenticated]


class SelectionUpdateView(UpdateAPIView):
    """Обновить выборку по id"""
    queryset = Selection.objects.all()
    serializer_class = SelectionUpdateSerializer
    permission_classes = [IsAuthenticated, IsCreatedBy]


class SelectionDeleteView(DestroyAPIView):
    """Удалить выборку по id"""
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated, IsCreatedBy]
