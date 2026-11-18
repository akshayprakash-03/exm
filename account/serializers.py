from rest_framework import serializers

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields = ('username', 'email', 'password')


        def create(self, validated_data):
            e=User.objects.create_user(**validated_data)
            e.save()
            return e

