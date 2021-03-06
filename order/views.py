import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import Order


def get_orders_list(request):
    orders_list = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders_list})


def retrieve(request, id):
    order = Order.objects.get(id=id)
    return render(request, 'order.html', {'order': order})


def create(request):
    data = json.loads(request.body)
    new_order = Order.objects.create(**data)
    return HttpResponse(f'{request.method} method activated! Added new order where id={new_order.id}.')


def delete(request):
    data = json.loads(request.body)
    try:
        order = Order.objects.get(id=data['id'])
        order.delete()
        return HttpResponse(f'{request.method} method activated! Deleted order where id={data["id"]}.')
    except Order.DoesNotExist:
        return HttpResponse(f'Sorry, but order where id={data["id"]} does not exist')


def update(request):
    data = json.loads(request.body)
    try:
        order = Order.objects.get(id=data['id'])
        for key in data.keys():
            if key in order.__dict__.keys():
                order.__dict__[key] = data[key]
        order.save()
        return HttpResponse(f'{request.method} method activated! The order #{order.id} was updated"')
    except Order.DoesNotExist:
        return HttpResponse(f'Sorry, but order where id={data["id"]} does not exist')
