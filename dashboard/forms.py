from django.forms import ModelForm

from models import Client, Order, Product


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'