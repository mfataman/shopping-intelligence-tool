from mongoengine import Document, StringField, FloatField, URLField, DateTimeField
from datetime import datetime

class Product(Document):
    product_name = StringField(required=True)
    sku = StringField(required=True, unique=True)
    price = FloatField(required=True)
    retailer = StringField(required=True)
    url = URLField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'indexes': ['sku'],
        'strict': False,
        'collection': 'products'
    }