from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'full_name',
            'phone',
            'Passport',
            'Hudud',
            'Shahar',
            'tashkilot',
            'malumot',
            'mutaxasislik',
            'lavozim',
            'unvoni',
            'oqishshakli',
            'oqishturi',
            'sportturi',
            'talimtili',
            'passportcopy',
            'image',
            'diplomcopy',
            'inn',
            'buyruq',
            'razryad',
        ]
