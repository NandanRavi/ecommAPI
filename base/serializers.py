from rest_framework import serializers
from .models import Customer, Product, Order, OrderItem

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'contact_number']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'weight']


    def validate_weight(self, value):
        if value <= 0 or value > 25:
            raise serializers.ValidationError("Weight should not be greater than 25kg")
        return value


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    order_item = OrderItemSerializer(many=True, source='order_items')
    order_number = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = ['customer', 'order_number', 'address', 'order_date', 'order_item']

    def create(self, data):
        order_items_data = data.pop('order_items', None)
        if not order_items_data:
            raise serializers.ValidationError({"order_item": "Order contain atleast one item"})

        order = Order.objects.create(**data)
        for item_data in order_items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order

    def update(self, instance, data):
        order_items_data = data.pop('order_items', None)
        instance.address = data.get('address', instance.address)
        instance.save()

        if order_items_data:
            OrderItem.objects.filter(order=instance).delete()
            for item_data in order_items_data:
                OrderItem.objects.create(order=instance, **item_data)
        return instance
