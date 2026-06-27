from rest_framework_nested import routers
from .views import (
    DrinkViewSet,
    CategoryViewSet,
    OrderViewSet,
    PromotionViewSet,
    ReviewViewSet,
    FavoriteViewSet,
    IngredientViewSet,
)


router = routers.DefaultRouter()
router.register(r'drinks', DrinkViewSet, basename='Drink')
router.register(r'category', CategoryViewSet, basename='Category')
router.register(r'order', OrderViewSet, basename='Order')
router.register(r'promotion', PromotionViewSet, basename='Promotion')
router.register(r'favorite', FavoriteViewSet, basename='favorite')
router.register(r'ingredient', IngredientViewSet, basename='ingredient')
drinks_router = routers.NestedDefaultRouter(router, r'drinks', lookup='drink')
drinks_router.register(r'reviews', ReviewViewSet, basename='drink-reviews')


urlpatterns = router.urls + drinks_router.urls
