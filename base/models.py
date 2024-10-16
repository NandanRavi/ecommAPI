from django.db import models
# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    contact_number = models.CharField(max_length=12)
    username = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.name
    
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=10, unique=True, editable=False)
    address = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
            self.order_number = f"ORD{self.pk:05d}"
            self.save(update_fields=['order_number'])
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.order.order_number
    