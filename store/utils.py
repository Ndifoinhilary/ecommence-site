import json
from .models import *


def cookieCart(request):

    items = []
    order = {"get_cart_total": 0, "get_cart_items": 0, 'shipping': False}
    cartItems = order["get_cart_items"]
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    for i in cart:
        try:
            cartItems += cart[i]['quantity']
            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])
            order['get_cart_items'] += cart[i]['quantity']
            order['get_cart_total'] += total

            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL
                },
                'quantity': cart[i]['quantity'],
                'get_total': total
            }
            items.append(item)
            
            print(product.shipping)
            if product.shipping == True:
                order['shipping'] == False

        except:
            pass
    return {"items": items, "order": order,
            'cartItems': cartItems

            }



def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        cookiesData = cookieCart(request)
        cartItems = cookiesData['cartItems']
        items = cookiesData['items']
        order = cookiesData['order']
    return {"items": items, "order": order,
            'cartItems': cartItems}


def guestOrder(request , data):
    name = data['form']['name']
    email = data['form']['email']
    cookieData = cookieCart(request)
    items = cookieData['items']
        
    customer , created = Customer.objects.get_or_create(
            email =email,
        )
    customer.name = name
    customer.save()
        
    order = Order.objects.create(
            customer = customer,compile =False
        )
        
    for item in items :
        product = Product.objects.get(id = item['product']['id'])
        orderItem = OrderItem.objects.create(
             product = product,
            order = Order,
            quantity = item['quantity']
            )
    
        return customer, order