from rest_framework import serializers

from order_process.models import Request
from materials.api.serializers import ArticleSerializer


class RequestSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(many=False)

    class Meta:
        model = Request
        fields = "__all__"