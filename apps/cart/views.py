from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from apps.shop.models import ProductModel, ProductStatusType
from .cart import CartSession


class CartSummaryView(View):

    def get(self, request):
        cart = CartSession(request.session)
        cart_items = cart.get_cart_items()
        total_quantity = cart.get_total_quantity()
        total_payment_price = cart.get_total_payment_amount()
        context = {
            'cart_items': cart_items,
            'total_quantity': total_quantity,
            'total_payment_price': total_payment_price,
        }
        return render(request, 'cart/cart-summary.html', context)


class SessionAddProductView(View):

    def post(self, request, *args, **kwargs):
        cart = CartSession(request.session)
        product_id = request.POST.get("product_id")
        if product_id and ProductModel.objects.filter(id=product_id, status=ProductStatusType.publish.value).exists():
            cart.add_product(product_id)
        if request.user.is_authenticated:
            cart.merge_session_cart_in_db(request.user)
        return JsonResponse({"cart": cart.get_cart_dict(), "total_quantity": cart.get_total_quantity()})


class SessionUpdateProductQuantityView(View):

    def post(self, request, *args, **kwargs):
        cart = CartSession(request.session)
        product_id = request.POST.get("product_id")
        quantity = request.POST.get("quantity")
        if product_id and quantity:
            cart.update_product_quantity(product_id, quantity)
        if request.user.is_authenticated:
            cart.merge_session_cart_in_db(request.user)
        return JsonResponse({"cart": cart.get_cart_dict(), "total_quantity": cart.get_total_quantity()})


class SessionRemoveProductView(View):

    def post(self, request, *args, **kwargs):
        cart = CartSession(request.session)
        product_id = request.POST.get("product_id")
        if product_id:
            cart.remove_product(product_id)
        if request.user.is_authenticated:
            cart.merge_session_cart_in_db(request.user)
        return JsonResponse({"cart": cart.get_cart_dict(), "total_quantity": cart.get_total_quantity()})
