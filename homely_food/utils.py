import requests
import stripe

url = "https://supersent.in/api/send-email/"

def send_mail(to,subject,content):
    data = {
        "subject":subject,
        "to_email":to,
        "context":{
            "message":content
        },
        "api_key":"25a36e7d3c7f4e3" # change this if needed
    }
    res = requests.post(url=url,headers={},json=data)
    print("Response of Sending Email : ",res.text,"\n")

STRIPE_PUBLIC_KEY = '' # change this
STRIPE_SECRET_KEY = '' # change this

def create_stripe_payment_link(amount,order_id):
    stripe.api_key = STRIPE_SECRET_KEY
    try:
        payment_link = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'inr',
                        'product_data': {
                            'name': 'YUMMY ORDER',
                        },
                        'unit_amount': int(amount*100),  # Amount in cents
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url= "http://127.0.0.1:8000/orders/place-order?order_id="+str(order_id)
            
        )
        return payment_link.url
    except stripe.error.StripeError as e:
        msg = f"🚫 PAYMENT LINK GENERATION FAILED -> {e}"
        return None