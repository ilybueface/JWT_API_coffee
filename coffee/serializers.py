from rest_framework import serializers
from .models import (
    Drink,
    Category,
    Order,
    Promotion,
    Ingredient,
    Favorite,
    OrderItem,
    DetailOfOrder,
    Review,
)


class Categoryserializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
        ]


class Drinkserializers(serializers.ModelSerializer):
    category = Categoryserializers(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model =  Drink
        fields = [
            'id',
            'name',
            'price',
            'category',
            'category_id'
        ]


class OrderItemserializers(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
                  'id',
                  'drink',
                  'quantity'
                  ]


class Orderserializers(serializers.ModelSerializer):
    items = OrderItemserializers(many=True, read_only=True)
    items_data = OrderItemserializers(many=True, write_only=True)

    class Meta:
        model = Order
        fields = [
                  'id',
                  'user',
                  'status',
                  'created_at',
                  'items',
                  'items_data'
                  ]


class Reviewserializers(serializers.ModelSerializer):
    drink = Drinkserializers(read_only=True)
    drink_id = serializers.IntegerField(write_only=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = [
                  'id',
                  'drink',
                  'drink_id',
                  'author',
                  'text',
                  'rating',
                  'created_at'
                  ]


class Promotionserializers(serializers.ModelSerializer):
    drinks = Drinkserializers(read_only=True, many=True)
    drinks_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=Drink.objects.all()
    )

    class Meta:
        model = Promotion
        fields = [
                  'id',
                  'title',
                  'discount_percent',
                  'active_until',
                  'drinks',
                  'drinks_ids'
                  ]


class Favoriteserializer(serializers.ModelSerializer):
    drink = Drinkserializers(read_only=True)
    drink_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Favorite
        fields = [
                  'id',
                  'drink',
                  'drink_id',
                  'added_at'
                  ]


class Ingredientsserializer(serializers.ModelSerializer):
    drinks = Drinkserializers(read_only=True, many=True)
    drinks_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=Drink.objects.all()
    )

    class Meta:
        model = Ingredient
        fields = [
                  'id',
                  'name',
                  'is_allergen',
                  'extra_price',
                  'drinks',
                  'drinks_ids'
                  ]
