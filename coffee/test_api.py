import pytest
from .models import Category, Ingredient, Drink
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.mark.django_db
def test_category_list():
    client = APIClient()
    response = client.get('/coffee/category/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_drink_list():
    client = APIClient()
    response = client.get('/coffee/drinks/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_drink_list():
    user = User.objects.create_superuser(username='Mrx', password='Mrx1234')
    refresh = RefreshToken.for_user(user)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(refresh.access_token))

    category = Category.objects.create(name='Coffee')
    response = client.post('/coffee/drinks/', {
        'name': 'Latte',
        'price': '320.00',
        'category_id': category.id,
    })

    assert response.status_code == 201


@pytest.mark.django_db
def test_user_list():
    user = User.objects.create_user(username='test', password='test1234')
    refresh = RefreshToken.for_user(user)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(refresh.access_token))

    category = Category.objects.create(name='Coffee')
    response = client.post('/coffee/drinks/', {
        'name': 'Raf',
        'price': '320.00',
        'category_id': category.id,
    })

    assert response.status_code == 403


@pytest.mark.django_db
def test_order_list():
    user = User.objects.create_user(username='test', password='test123456')

    client = APIClient()
    response = client.get('/coffee/order/')

    assert response.status_code == 401


@pytest.mark.django_db
def test_category_token_list():
    user = User.objects.create_superuser(username='test', password='test12345')
    refresh = RefreshToken.for_user(user)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(refresh.access_token))

    category = Category.objects.create(name='Limonade')
    response = client.post('/coffee/category/', {'name': 'Limonade'})

    assert response.status_code == 201


@pytest.mark.django_db
def test_category_wth_token_list():
    user = User.objects.create_user(username='test', password='test9122')

    client = APIClient()

    category = Category.objects.create(name='Tea')
    response = client.post('/coffee/category/', {'name': 'Tea'})

    assert response.status_code == 401


@pytest.mark.django_db
def test_ingredient_admin_list():
    user = User.objects.create_superuser(username='mrx', password='mrx12345')
    refresh = RefreshToken.for_user(user)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(refresh.access_token))

    category = Category.objects.create(name='Coffee')
    drink = Drink.objects.create(name='Latte', price='320', category=category)
    response = client.post('/coffee/ingredient/', {
        'name': 'karamel',
        'is_allergen': True,
        'extra_price': '49.00',
        'drinks_ids': [drink.id],
        }, format='json')

    assert response.status_code == 201


@pytest.mark.django_db
def test_ingredient_user_list():
    user = User.objects.create_user(username='test', password='tester123')
    refresh = RefreshToken.for_user(user)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(refresh.access_token))

    category = Category.objects.create(name='Coffee')
    drink = Drink.objects.create(name='Raf', price='349', category=category)
    response = client.post('/coffee/ingredient/', {
        'name': 'Salted Caramel',
        'is_allergen': True,
        'extra_price': '59.00',
        'drinks_ids': [drink.id],
    }, format='json')

    assert response.status_code == 403