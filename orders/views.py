from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from .models import Order, ItemOrder, OrderResult, OrderResultItem
from scripts.payment import Payment, CheckingCoupon
from scripts.bot import OrderBot
from scripts.personalize_v2 import Personalize
from accounts.models import UserProxy
from constance import config
from django.utils import timezone

# Create your views here.
def orders(request):
    
    return redirect('profile')

def order(request, order_id):
    
    

    if Order.objects.get(order_id=order_id).user == request.user:
        if Order.objects.get(order_id=order_id).visible == False:
            return redirect('error')
        
        order = Order.objects.filter(order_id = order_id).get()
        order_pay = Order.objects.filter(order_id = order_id)
        
        print('order:' + str(order.order_status))
        #print('order site')
        item_order = ItemOrder.objects.filter(order=order).last().order_result
    
        print("order result", str(item_order))
        price = 100
        if request.method == "POST":
            pay = Payment(price=price, user_email=request.user.email, order_id=order_id)
            if pay == 'payment_accepted':

                
                order_pay.update(order_status = "PA", paid_at=timezone.now())
                #OrderBot(order_id=order_id, user_email=request.user.email, pay_price=price)

                if config.AUTO_CREATE_RESULT:
                    
                    if config.USE_NEW_MIXER:
                        #print('new_mixer')
                        Personalize(order_id = order_id)
                        
                    else:
                        print('old_mixer')

                return redirect('paymentsuccess')
            
        else:
            pass
        return render(request, 'order.html',{'order': order, 'result_id': item_order})
    
    if request.user.is_admin:
        order = Order.objects.filter(order_id = order_id)
        return render(request, 'order.html',{'order': order})
    else:
        return redirect('error')
    

def payment(request, order_id):
    order = Order.objects.filter(order_id = order_id).get()
    order_pay = Order.objects.filter(order_id = order_id)
    new_price = order.pay_price
    if request.method == "POST":
        if 'button_coupon' in request.POST:
            user_email = request.user.email
            coupon_name = request.POST.get("coupon_field")
            base_price = UserProxy.objects.get(email = user_email).price_base

            coupon = CheckingCoupon(user_email=user_email,coupon_name=coupon_name, base_price=base_price)
            new_price = coupon.get('price_coupon')
            error = coupon.get('error_coupon')
            order_pay.update(pay_price=new_price)
            
            #print(str(error))
            return render(request, 'payment.html',{'order': order, 'new_price': new_price, 'error': error})
        if 'button_pay' in request.POST:
            OrderBot(order_id=order_id, user_email=request.user.email, pay_price=new_price)
            return redirect('order', order.pk) 
    else:
        ## if pay
        
        return render(request, 'payment.html', {'order': order})
    return render(request, 'payment.html', {'order': order})
    

def payment_success(request):
    return render(request, 'payment_success.html', {})


def result(request, result_id):
    order_result = OrderResult.objects.filter(id=result_id).last()
    
    result = OrderResultItem.objects.filter(order_result=result_id).all()
    return render(request, 'result.html',{'result': result})