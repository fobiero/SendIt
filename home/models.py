from django.db import models

class Customer(models.Model):
    # id = models.AutoField(primary_key=True)
    LOCATION_CHOICES = (('Nairobi', 'Nairobi'), ('Mombasa', 'Mombasa'), ('Kisumu', 'Kisumu'), ('Embu', 'Embu'), ('Nakuru', 'Nakuru'))
    pickup_location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    destination_location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    sender_contact = models.CharField(max_length=200)
    receipient_name = models.CharField(max_length=200)
    receipient_contact = models.CharField(max_length=200)
    PACKAGE_CHOICES = (('Small', 'Small'), ('Large', 'Large'))
    parcel_package = models.CharField(max_length=100, choices=PACKAGE_CHOICES)
    
    def __str_(self):
        return self.first_name + ' ' + self.last_name

class Sender(models.Model):
    sender_name = models.CharField(max_length=200)

    def __str_(self):
        return self

class newdestination(models.Model):
    LOCATION_CHOICES = (('N', 'Nairobi'), ('M', 'Mombasa'), ('K', 'Kisumu'), ('E', 'Embu'), ('N', 'Nakuru'))
    new_location = models.CharField(max_length=1, choices=LOCATION_CHOICES)

    def __str_(self):
        return self


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Product(models.Model):

    PACKAGE_CHOICES = (('Small', 'Small'),('Large', 'Large'))

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    prodName = models.CharField(max_length=255, choices=PACKAGE_CHOICES)


# Customer
# Order
# Destination
# SingleOrder
# Cost 


# Customer -->  Order
# Order -- > Destination
# Customer --> Destination 
# Cost -- > Destination 