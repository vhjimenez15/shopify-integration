from rest_framework import serializers
from .models import Image, Option, Product, Variant


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True, required=False)
    options = OptionSerializer(many=True)
    images = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        variants_data = validated_data.pop('variants', [])
        options_data = validated_data.pop('options', [])
        images_data = validated_data.pop('images', [])

        product = Product.objects.create(**validated_data)

        for variant_data in variants_data:
            Variant.objects.create(product=product, **variant_data)

        for option_data in options_data:
            Option.objects.create(product=product, **option_data)

        for image_data in images_data:
            Image.objects.create(product=product, **image_data)

        return product

    def update(self, instance, validated_data):
        variants_data = validated_data.pop('variants', [])
        options_data = validated_data.pop('options', [])
        images_data = validated_data.pop('images', [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        instance.variants.all().delete()
        for variant_data in variants_data:
            Variant.objects.create(product=instance, **variant_data)

        instance.options.all().delete()
        for option_data in options_data:
            Option.objects.create(product=instance, **option_data)

        instance.images.all().delete()
        for image_data in images_data:
            Image.objects.create(product=instance, **image_data)

        return instance
