from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models.ad import Ad
from ads.serializers.ad import AdSerializer, AdCreateSerializer, AdUpdateSerializer, AdImageSerializer


class AdListView(ListAPIView):
    """ Только для авторизованых пользователей"""
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """ Объявления по категориям. """

        # Фильтровать по идентификатору категории
        category = request.GET.getlist("cat", [])
        if category:
            self.queryset = self.queryset.filter(category_id__in=category)

        # Фильтровать по названию обьявлений
        if request.GET.get("text", None):
            self.queryset = self.queryset.filter(name__icontains=request.GET.get("text"))

        # Filter by user location
        if request.GET.get("location", None):
            self.queryset = self.queryset.filter(author__locations__name__icontains=request.GET.get("location"))

        # Фильтровать по цене
        price_from = request.GET.get('price_from', None)
        price_to = request.GET.get('price_to', None)
        if price_from:
            self.queryset = self.queryset.filter(
                price__gte=price_from
            )
        if price_to:
            self.queryset = self.queryset.filter(
                price__lte=price_to
            )

        return super().get(request, *args, **kwargs)


class AdDetailView(RetrieveAPIView):
    """Только для авторизованых пользователей"""
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]


class AdCreateView(CreateAPIView):
    """Создать новое объявление"""
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer


class IsCreatedByOrAdminOrModerator:
    pass


class AdUpdateView(UpdateAPIView):
    """Обновить объявление по id"""
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer
    permission_classes = [IsAuthenticated, IsCreatedByOrAdminOrModerator]


class AdImageView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdImageSerializer
    permission_classes = [IsAuthenticated, IsCreatedByOrAdminOrModerator]


class AdDeleteView(DestroyAPIView):
    """Удалить обьявление по id"""
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, IsCreatedByOrAdminOrModerator]
