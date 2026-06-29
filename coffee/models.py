from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} | {self.price}"


class DetailOfOrder(models.TextChoices):
    PENDING = 'PD', 'Pending'
    PREPARING = 'PR', 'Preparing'
    READY = 'RD', 'Ready'
    COMPLETED = 'CP', 'Completed'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=2,
        choices=DetailOfOrder.choices,
        default=DetailOfOrder.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} | {self.status}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.order} | {self.drink} | {self.quantity}"


class Review(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.drink} | {self.rating}"


class Promotion(models.Model):
    title = models.CharField(max_length=300)
    discount_percent = models.IntegerField()
    active_until = models.DateField()
    drinks = models.ManyToManyField(Drink)

    def __str__(self):
        return f"{self.title} | {self.discount_percent}%"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'drink')

    def __str__(self):
        return f"{self.user} | {self.drink}"


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    is_allergen = models.BooleanField()
    extra_price = models.DecimalField(max_digits=8, decimal_places=2)
    drinks = models.ManyToManyField(Drink)

    def __str__(self):
        return f"{self.name} | {self.is_allergen}"


class CoffeeBranch(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    latitude = models.DecimalField(max_digits=8, decimal_places=2)
    longitude = models.DecimalField(max_digits=8, decimal_places=2)
    average_check = models.DecimalField(max_digits=8, decimal_places=2)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} | {self.address} {self.email}"
