# from rest_framework import serializers
# from .models import Image

# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Image
#         fields = '__all__'


from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(help_text="Upload an image file.")
    category = serializers.ChoiceField(
        choices=Image.CATEGORY_CHOICES,
        help_text="Use one of: network, attack, system, ui, other.",
    )

    class Meta:
        model = Image
        fields = ["id", "image", "caption", "category"]