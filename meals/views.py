from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
from meals.services.meal_service import MealService
from meals.services.product_service import ProductService
from meals.helper import parse_json_from_request
from meals.services.pdf_service import PdfService
from meals.services.category_service import CategoryService
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from meals.services.user_service import UserService


def custom_middleware(get_response):
    def middleware(request):
        try:
            response = get_response(request)
            return response

        except Exception as ex:
            return JsonResponse({'detail': str(ex)}, safe=False, status=400)

    return middleware

def custom_middleware2(get_response):
    def middleware(request, id):
        try:
            response = get_response(request, id)
            return response

        except Exception as ex:
            return JsonResponse({'detail': str(ex)}, safe=False, status=400)

    return middleware


@api_view(['GET'])
@permission_classes([AllowAny])
@custom_middleware
def product_list(request: WSGIRequest):
    products = ProductService().product_list()
    return JsonResponse(products, safe=False)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@custom_middleware
def create_product(request: WSGIRequest):
    parameters = parse_json_from_request(request)
    ProductService().create_product(parameters)
    return HttpResponse()


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
@custom_middleware2
def delete_product(request: WSGIRequest, id :str):
    parameters = {'id': id}
    ProductService().delete_product(parameters)
    return HttpResponse()


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@custom_middleware2
def update_product(request: WSGIRequest, id: str):
    parameters = parse_json_from_request(request)
    parameters['id'] = id
    ProductService().update_product(parameters)
    return HttpResponse()


@api_view(['GET'])
@permission_classes([AllowAny])
@custom_middleware2
def get_product(request: WSGIRequest, id: str):
    parameters = {'id': id}
    product = ProductService().get_product(parameters)
    return JsonResponse(product, safe=False)


@api_view(['GET'])
@permission_classes([AllowAny])
@custom_middleware
def meal_list(request: WSGIRequest):
    meals = MealService().meal_list()
    return JsonResponse(meals, safe=False)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@custom_middleware
def create_meal(request: WSGIRequest):
    parameters = parse_json_from_request(request)
    MealService().create_meal(parameters, request.user)
    return HttpResponse()


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@custom_middleware2
def delete_meal(request: WSGIRequest, id: str):
    parameters = {'id': id}
    MealService().delete_meal(parameters, request.user)
    return HttpResponse()


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@custom_middleware2
def update_meal(request: WSGIRequest, id: str):
    parameters = parse_json_from_request(request)
    parameters['id'] = id
    MealService().update_meal(parameters)
    return HttpResponse()


@api_view(['GET'])
@permission_classes([AllowAny])
@custom_middleware2
def get_meal(request: WSGIRequest, id: str):
    parameters = {'id': id}
    meal = MealService().read_meal(parameters)
    return JsonResponse(meal)


@api_view(['GET'])
@permission_classes([AllowAny])
@custom_middleware
def category_list(request: WSGIRequest):
    parameters = parse_json_from_request(request)
    meals = CategoryService().category_list(parameters)
    return JsonResponse(meals, safe=False)


@api_view(['POST'])
@permission_classes([IsAdminUser])
@custom_middleware
def create_category(request: WSGIRequest):
    parameters = parse_json_from_request(request)
    CategoryService().create_category(parameters)
    return HttpResponse()


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
@custom_middleware2
def delete_category(request: WSGIRequest, id: str):
    parameters = {'id': id}
    CategoryService().delete_category(parameters)
    return HttpResponse()

@api_view(['GET'])
@permission_classes([AllowAny])
@custom_middleware2
def get_category(request: WSGIRequest, id: str):
    parameters = {'id': id}
    meal = CategoryService().read_category(parameters)
    return JsonResponse(meal, safe=False)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@custom_middleware2
def update_category(request: WSGIRequest, id: str):
    parameters = parse_json_from_request(request)
    parameters['id'] = id
    CategoryService().update_category(parameters)
    return HttpResponse()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@custom_middleware2
def generate_pdf(request: WSGIRequest, id:str):
    parameters = parse_json_from_request(request)
    parameters['id'] = id

    meal = MealService().get_meal(parameters)
    response = PdfService().generate_pdf(meal, request.user)

    return response if response else HttpResponse()


@api_view(['GET'])
@permission_classes([IsAdminUser])
@custom_middleware
def user_list(request: WSGIRequest):
    parameters = parse_json_from_request(request)
    users = UserService().user_list(parameters)
    return JsonResponse(users, safe=False)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
@custom_middleware2
def delete_user(request: WSGIRequest, id: str):
    parameters = {'id': id}
    UserService().delete_user(parameters)
    return HttpResponse()


@api_view(['PUT'])
@permission_classes([IsAdminUser])
@custom_middleware2
def update_user(request: WSGIRequest, id: str):
    parameters = parse_json_from_request(request)
    parameters['id'] = id
    UserService().update_user(parameters)
    return HttpResponse()


@api_view(['GET'])
@permission_classes([IsAdminUser])
@custom_middleware2
def get_user(request: WSGIRequest, id: str):
    parameters = {'id': id}
    user = UserService().read_user(parameters)
    return JsonResponse(user)