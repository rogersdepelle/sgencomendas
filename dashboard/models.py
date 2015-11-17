from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=45, unique=True)
    description = models.TextField()
    #image = models.ImageField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    minimum_quantity = models.IntegerField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=60)
    cpf = models.CharField(max_length=14, unique=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    adress = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Order(models.Model):

    STATUS = (
        (0, 'Cancelada'),
        (1, 'Registrada'),
        (2, 'Preparando'),
        (3, 'Pronta Para Entrega'),
        (4, 'Aguardando Pagamento'),
        (5, 'Finalizada'),
    )

    client = models.ForeignKey('Client')
    product = models.ForeignKey('Product')
    quantity = models.IntegerField()
    delivery = models.DateField()
    status = models.IntegerField(choices=STATUS)

    def get_value(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.client.name + " - " + self.product.name

    def __unicode__(self):
        return self.client.name + " - " + self.product.name
