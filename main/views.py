from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from main.models import FrameworkModel
from main.serializers import FrameworkListSerializer, FrameworkRetrieveSerializer, FrameworkCreateSerializer


class FrameworkListAPIView(ListAPIView):
    serializer_class = FrameworkListSerializer
    queryset = FrameworkModel.objects.all()


class FrameworkListByLanguageAPIView(ListAPIView):
    serializer_class = FrameworkRetrieveSerializer

    def get_queryset(self):
        language = self.kwargs['language']
        return FrameworkModel.objects.filter(language=language)


class FrameworkCreateAPIView(CreateAPIView):
    serializer_class = FrameworkCreateSerializer
