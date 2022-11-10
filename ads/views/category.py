from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from ads.models.category import Category
from ads.permissions.ad import IsCreatedByOrAdminOrModerator
from ads.serializers.category import CatSerializer


class CatViewPagination(PageNumberPagination):
    """ Для категорий свой класс пагинации"""
    page_size = 2
    # page_size - Доп параметр в get запросе например  http://localhost/cat/?page_size=5
    page_size_query_param = 'page_size'
    # Максимальное значение для 'page_size'
    max_page_size = 10


class CatViewSet(viewsets.ModelViewSet):
    """ Для списка категорий"""
    queryset = Category.objects.all().order_by('name')
    serializer_class = CatSerializer
    pagination_class = CatViewPagination
    permission_classes = [IsCreatedByOrAdminOrModerator]
