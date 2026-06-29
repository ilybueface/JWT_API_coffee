from django.contrib import admin
from .models import (
    Category,
    Drink,
    Promotion,
    Ingredient,
    Favorite,
    OrderItem,
    Order,
    Review,
    CoffeeBranch,
)

admin.site.register(Category)
admin.site.register(Drink)
admin.site.register(Promotion)
admin.site.register(Ingredient)
admin.site.register(Favorite)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(CoffeeBranch)
