from django.shortcuts import render
from django.views import View
from store.models import Order


class Analysis(View):
    def get(self,request):
        labels = []
        data = []

        queryset = Order.objects.order_by('-price')[:5]
        for city in queryset:
            labels.append(city.price)
            data.append(city.quantity)

        return render(request, 'pie_chart.html', {
            'labels': labels,
            'data': data,
        })