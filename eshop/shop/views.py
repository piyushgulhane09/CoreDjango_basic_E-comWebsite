from django.shortcuts import render,HttpResponse,redirect
from .models import Product,Category,Customer,Order
from django.contrib.auth.hashers import make_password, check_password
# from shop.middlewares import auth_middleware

# Create your views here.
def index(request):
    products = Product.objects.all()
    
    category_name = Category.objects.all()
    print(request.session.get('id'))
    print(request.session.get('email'))
    print(request.session.get('name'))
    
    
    # del request.session['cart']
    if request.method == "POST":
        if request.POST.get('product_ID'):
            product_ID = request.POST.get('product_ID')
            remove = request.POST.get('remove')
            cart = request.session.get('cart')     
            if cart:
                quantity = cart.get(product_ID)
                if quantity :
                    if remove:
                        if quantity <= 1:
                            cart.pop(product_ID)
                        else:
                            cart[product_ID] = quantity - 1
                    else:
                        cart[product_ID] = quantity + 1
                else:
                    cart[product_ID] = 1
            else:
                cart = {}
                cart[product_ID] = 1

            request.session['cart'] = cart
            # print(request.session['cart'])
        else:
            pass
    else:
        pass            


    return render(request,"index.html",{'All_products' : products,'Allcategory_name':category_name})


def category(request,category_id):
    category_products = Product.objects.filter(category = category_id)
    category_name = Category.objects.all()
    return render(request,"index.html",{"category_products":category_products,'Allcategory_name':category_name})
    
def signup(request):
    return render(request,"signup.html",{'err_msg': None})

def signupSubmit(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        error_msg = None

        # saving Values for form 
        values = {
            'f_name' : first_name,
            'l_name' : last_name,
            'phone' : phone,
            'email' : email,
        }

        # validating
        if (not first_name):
            error_msg = "First Name Required !!"
        elif len(first_name) < 4:
            error_msg = 'First Name must be 4 char long or more'
        elif not last_name:
            error_msg = 'Last Name Required'
        elif len(last_name) < 4:
            error_msg = 'Last Name must be 4 char long or more'
        elif not phone:
            error_msg = 'Phone Number required'
        elif len(phone) < 10:
            error_msg = 'Phone Number must be 10 char Long'
        elif len(password) < 6:
            error_msg = 'Password must be 6 char long'
        elif email:
            if Customer.objects.filter(email = email):
                error_msg = 'Email Address Already Registered'
            
            
        
        # saving
        if(not error_msg):
            password = make_password(password)
            customer = Customer(first_name=first_name,last_name=last_name,phone=phone,email=email,password=password)
            customer.save()
            # return redirect('http://localhost:8000')
            return redirect('index')

        else:
            return render(request,"signup.html",{'err_msg':error_msg,'values':values})


    else:
        pass

def login(request):

    error_msg = None
    if request.method == "POST":

        email = request.POST.get('email')
        password_ = request.POST.get('password')


        customer = Customer.objects.filter(email = email)

        if  customer:
            password = customer[0].password
            
            if check_password(password_,password) == True:

                request.session['id'] = customer[0].id
                request.session['name'] = customer[0].first_name
                request.session['email'] = customer[0].email

                return redirect("index")
            else:
                error_msg = "Password is  incorrect"
                
        else:
            error_msg = "Emailid is not incorrect"
            print(error_msg)        

    return render(request,"login.html",{'error_msg':error_msg})
        

def logout(request):
    request.session.clear()
    return redirect('login')       

def cart(request):
    

    ids = list(request.session.get('cart').keys())

    # fetchin products of ids
    products = []
    for id in ids:
        t_product = Product.objects.filter(id = id)
        products.extend(t_product)
    print(products)

    return render(request,"cart.html",{'products':products})


def checkout(request):
    if request.session.get('id'):
        cart = request.session.get('cart')
        customer = request.session.get('id')
        address = request.POST.get('email')
        number = request.POST.get('number')
        keys = list(cart.keys())
        products = Product.objects.filter(id__in = keys)
        for product in products:
            order = Order(
                customer = Customer(id=customer),
                product = product,
                address = address,
                price = product.price,
                phone = number,
                quantity = cart.get(str(product.id))
            )
            order.save()
        request.session['cart'] = {}

        return redirect('cart')
    else :
        return redirect('login')


# @auth_middleware
def order(request):
    customer_id = request.session.get('id')
    orders = Order.objects.filter(customer = customer_id).order_by('-date')

    return render(request,"orders.html",{"orders":orders})