from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Order, Fill


class IndexView(generic.ListView):
    template_name = 'currencies/index.html'
    context_object_name = 'latest_order_list'

    def get_queryset(self):
        """
        Return the last five published orders (not including those set to be
        published in the future).
        """
        return Order.objects.filter(
            time__lte=timezone.now()
        ).order_by('-time')[:5]


class DetailView(generic.DetailView):
    model = Order
    template_name = 'currencies/detail.html'

    def get_queryset(self):
        """
        Excludes any orders that aren't published yet.
        """
        return Order.objects.filter(time__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Order
    template_name = 'currencies/results.html'


def units(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    try:
        selected_fill = order.fill_set.get(pk=request.POST['fill'])
    except (KeyError, Fill.DoesNotExist):
        # Re-display the order voting form.
        return render(request, 'currencies/detail.html', {
            'order': order,
            'error_message': "You didn't select an order fill type.",
        })
    else:
        selected_fill.units += 100000
        selected_fill.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('currencies:results', args=(order.id,)))
