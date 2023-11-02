import stripe

from app_course.models import Course, Lesson
from app_payment.models import Payment
from config import settings


def create_product(obj: Payment):
	stripe.api_key = settings.STRIPE_API_KEY

	if obj.payment_type == 'remittance':
		if obj.course:
			product = Course.objects.get(pk=int(obj.course_id))
			response = stripe.Product.create(name=product.title)
		else:
			product = Lesson.objects.get(pk=obj.lesson_id)
			response = stripe.Product.create(name=product.name)
		return response.get('id')
	else:
		return None


def create_price(obj: Payment):
	stripe.api_key = settings.STRIPE_API_KEY
	product_id = create_product(obj)
	if product_id:
		response = stripe.Price.create(
			unit_amount=obj.amount,
			currency="usd",
			recurring={"interval": "month"},
			product=f"{product_id}",
		)
		return response.get('id')
	else:
		return None


def create_session(obj: Payment):
	stripe.api_key = settings.STRIPE_API_KEY
	price_id = create_price(obj)
	if price_id:
		response = stripe.checkout.Session.create(
			success_url="https://example.com/success",
			line_items=[
				{
					"price": f"{price_id}",
					"quantity": 1,
				},
			],
			mode="subscription",
		)
		return response["url"]
	return None
