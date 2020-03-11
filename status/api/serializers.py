from rest_framework import serializers
from status.models import Status


class StatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['user', 'content', 'img', 'id']

    def validate_content(self, value):
        if len(value) > 240:
            raise serializers.ValidationError("TOOO Long")
        return value

    def img_validate(self, value):
        print(value.url)
        if value is None:
            print(value)
            raise serializers.ValidationError('no Image')

    def validate(self, data):
        content = data.get('content', None)
        if content == '':
            content = None
        img = data.get('img', None)
        if content is None and img is None:
            raise serializers.ValidationError('content or image is required')
        return data
