from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
   
    keys = cart.keys()
   
    for id in keys:
        if int(id) == product:
            
            return True
    return False

@register.filter(name='quantity_cart')
def quantity_cart(product,cart):
    
    keys = cart.keys()
    
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0

@register.filter(name='price_total')
def price_total(product,cart):
    
    quantity = product.price * quantity_cart(product,cart)
    
    return quantity


@register.filter(name='product_price_total')
def product_price_total(product,cart):
    sum = 0
    for  p in product:
        sum += price_total(p , cart)
    
    return sum


@register.filter(name='product_total')
def product_total(products,cart):
    sum = 0
    for  p in products:
        sum += quantity_cart(p , cart)
    
    return sum

@register.filter(name='currency')
def currency(number):
    return "₹"+str(number)


@register.filter(name='multiply')
def multiply(price,quantity):
    return price * quantity

