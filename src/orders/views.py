from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.list import ListView
from django.contrib import messages
from django.views.generic.edit import FormView, CreateView
from django.core.urlresolvers import reverse

from .forms import AddressForm, UserAddressForm
from .models import UserAddress, UserCheckout, Order
from products.mixins import LoginRequiredMixin


class UserAddressCreateView(CreateView):
    form_class = UserAddressForm
    template_name = 'forms.html'
    
    def get_success_url(self):
        return reverse('cart_checkout')

    def get_user_checkout(self):
        user_checkout_id = self.request.session['user_checkout_id']
        return UserCheckout.objects.get(id=user_checkout_id)

    def form_valid(self, form, *args, **kwargs):
        form.instance.user = self.get_user_checkout()
        return super(UserAddressCreateView, self).form_valid(form, *args, **kwargs)


class AddressFormView(FormView):
    form_class = AddressForm
    template_name = 'orders/address_select.html'

    def dispatch(self, request, *args, **kwargs):
        b_address, s_address = self.get_address()
        if not (b_address.exists() and s_address.exists()):
            messages.success(self.request, 'Please add an address before continuing')
            return redirect('add_address')
        return super(AddressFormView, self).dispatch(request, *args, **kwargs)

    def get_address(self, *args, **kwargs):
        user_checkout  = self.request.session['user_checkout_id']
        b_address = UserAddress.objects.filter(
            type=UserAddress.BILLING, user_id=user_checkout)
        s_address = UserAddress.objects.filter(
            type=UserAddress.SHIPPING, user_id=user_checkout)
        return b_address, s_address

    def get_form(self):
        form = super(AddressFormView, self).get_form()
        b_address, s_address = self.get_address()
        form.fields['billing_address'].queryset = b_address
        form.fields['shipping_address'].queryset = s_address
        return form

    def form_valid(self, form, *args, **kwargs):
        billing_address = form.cleaned_data['billing_address']
        shipping_address = form.cleaned_data['shipping_address']
        self.request.session['billing_address_id'] = billing_address.id
        self.request.session['shipping_address_id'] = shipping_address.id
        return super(AddressFormView, self).form_valid(form, *args, **kwargs)

    def get_success_url(self):
        return reverse('cart_checkout')


class ConfirmOrderView(View):
    def post(self, request):
        order = Order.objects.get(id=request.session['order_id'])
        if request.POST.get('complete_order'):
            order.complete_order()
            del request.session['order_id']
            del request.session['cart_id']
            del request.session['cart_count']
        return redirect('/')


class OrdersList(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/orders_list.html'

    def get_queryset(self):
        return Order.objects.filter(user__user=self.request.user)
