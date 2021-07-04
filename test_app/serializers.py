from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import TestModel


class SimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        # --> se voglio mettere solo alcuni fields
        # fields = ("name", "description")

        # --> se voglio metterli tutti
        fields = "__all__"


# Serializer per il model TestModel (superata dak ModelSerializer)
# class SimpleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     phone_number = serializers.IntegerField()
#     is_live = serializers.BooleanField()
#     amount = serializers.FloatField()
#     extra_name = serializers.CharField(read_only=True)
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         return TestModel.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         TestModel.objects.filter(id=instance.id).update(**validated_data)
#         return TestModel.objects.get(id=instance.id)
