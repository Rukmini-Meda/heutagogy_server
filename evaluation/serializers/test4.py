from rest_framework import serializers
from evaluation.models import Test4, AudioDescriptionPair


class AudioDescriptionPairSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField('get_image')

    class Meta:
        model = AudioDescriptionPair
        fields = ['audio', 'description', ]

    def get_image(self, obj):
        request = self.context.get('request')
        url = obj.picture.url
        return request.build_absolute_uri(url)


class Test2Serializer(serializers.ModelSerializer):
    pictures = AudioDescriptionPairSerializer(many=True)
    
    class Meta:
        model = Test4
        fields = ['name', 'heading', 'pictures', ]