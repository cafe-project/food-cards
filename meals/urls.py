from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
urlpatterns = router.urls

urlpatterns += [
    path('product/', views.product_list, name='product_list'),
    path('product-create/', views.create_product, name='create_product'),
    path('product-delete/<str:id>/', views.delete_product, name='delete_product'),
    path('product-update/<str:id>/', views.update_product, name='update_product'),
    path('product-get/<str:id>/', views.get_product, name='get_product'),

    path('meal/', views.meal_list, name='meal_list'),
    path('meal-create/', views.create_meal, name='create_meal'),
    path('meal-delete/<str:id>/', views.delete_meal, name='delete_meal'),
    path('meal-update/<str:id>/', views.update_meal, name='update_meal'),
    path('meal-get/<str:id>/', views.get_meal, name='get_meal'),

    path('user/', views.user_list, name='user_list'),
    path('user-delete/<str:id>/', views.delete_user, name='delete_user'),
    path('user-update/<str:id>/', views.update_user, name='update_user'),
    path('user-get/<str:id>/', views.get_user, name='get_user'),

    path('category/', views.category_list, name='category_list'),
    path('category-create/', views.create_category, name='create_category'),
    path('category-delete/<str:id>/', views.delete_category, name='delete_category'),
    path('category-get/<str:id>/', views.get_category, name='get_category'),
    path('category-update/<str:id>/', views.update_category, name='get_category'),

    path('generate-pdf/<str:id>/', views.generate_pdf, name='generate_pdf'),

]
