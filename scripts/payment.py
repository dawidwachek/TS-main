from datetime import date
from promotions.models import Coupon


def Payment(price, user_email, order_id):

    payment_status = 'payment_accepted' #waiting_for_payment, payment_accepted, payment_failture
    

    return payment_status

def CheckingCoupon(user_email, coupon_name, base_price):
    is_active = False
    price_coupon = base_price
    type_coupon = ""
    error = ""

    coupon = Coupon.objects.filter(coupon_name=coupon_name).last()

    #negative type coupon
    if not coupon:
        error = "Coupon not exist [6]"
        return {'is_active':is_active, 'price_coupon':price_coupon,'type_coupon':type_coupon, "error_coupon": error}
    if coupon:
        if coupon.is_active == False:
            error = "coupon is not active [1]"
            return {'is_active':is_active, 'price_coupon':price_coupon,'type_coupon':type_coupon, "error_coupon": error}
        if coupon.max_uses_coupon != None:
            if coupon.uses_coupon >= coupon.max_uses_coupon:
                error = "the coupon is used up [2]"
                return {'is_active':is_active, 'price_coupon':price_coupon,'type_coupon':type_coupon, "error_coupon": error}
        
        if coupon.start_date_use != None:
            if date.today() < coupon.start_date_use:
                error = "coupon is not active [3]"
                return {'is_active':is_active, 'price_coupon':price_coupon,'type_coupon':type_coupon, "error_coupon": error}
        if coupon.end_date_use != None:
            if date.today() > coupon.end_date_use:
                error = "coupon is not active [4]"
                return {'is_active':is_active, 'price_coupon':price_coupon,'type_coupon':type_coupon, "error_coupon": error}


        #positive type coupon
        if coupon.zero_amount == True:
            price_coupon = 0
            return {'is_active':is_active, 'price_coupon':price_coupon,'type_coupon':type_coupon, "error_coupon": error}

        if coupon.assigment:
            if user_email == coupon.email_assignment:
                #here start type
                if coupon.type_coupon == "PE":
                    percent = 1 - (coupon.value_coupon/100)
                    price_coupon = base_price*percent
                if coupon.type_coupon == "AM":
                    price_coupon = base_price - coupon.value_coupon
                    print('with coupon'+str(price_coupon))

                print("price:" + str(price_coupon))
                if coupon.max_value_coupon > 0:
                    if (base_price - coupon.max_value_coupon) < price_coupon:
                        print('>' + str(price_coupon))
                        return {'is_active':is_active, 'price_coupon':price_coupon,'type_coupon':type_coupon, "error_coupon": error}
                    else:
                        price_coupon = base_price - coupon.max_value_coupon
                        print('<' + str(price_coupon))
                        return {'is_active':is_active, 'price_coupon':price_coupon,'type_coupon':type_coupon, "error_coupon": error}

                #here end type
            if user_email != coupon.email_assignment:
                error = "coupon is not for you [5]"
                return {'is_active':is_active, 'price_coupon':price_coupon,'type_coupon':type_coupon, "error_coupon": error}


# # 1. not active
# # 2. max uses coupon
# # 3. start date
# # 4. end date
# # 5. couopon for user
# # 6. not coupon


    return {'is_active':is_active, 'price_coupon':price_coupon,'type_coupon':type_coupon, "error_coupon": error}


