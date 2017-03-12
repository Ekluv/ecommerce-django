import random

from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import Q

import models, forms, mixins

# Create your views here.

class CategoryListView(ListView):
    model = models.Category
    template_name = 'products/product_list.html'


class CategoryDetail(DetailView):
    model = models.Category
    template_name = 'products/category_detail.html'

    def get_context_data(self, *args,**kwargs):
        context = super(CategoryDetail, self).get_context_data(*args, **kwargs)
        obj = self.get_object()
        product_set = obj.product_set.all()
        default_products = obj.default_category.all()
        products = (product_set | default_products).distinct()
        context['products'] = products
        return context


class VariationListView(mixins.StaffRequiredMixin, ListView):
    """
    """
    model = models.Variation
    template_name = 'products/variation_list.html'
    
    def get_queryset(self, *args, **kwargs):
        return models.Variation.objects.filter(product_id=self.kwargs.get('id'))

    def get_context_data(self, *args, **kwargs):
        context = super(VariationListView, self).get_context_data(*args, **kwargs)
        context['formset'] = forms.VariationInventoryFormSet(queryset=self.get_queryset())
        return context

    def post(self, request, *args, **kwargs):
        formset = forms.VariationInventoryFormSet(request.POST)
        print formset.is_valid()
        if formset.is_valid():
            # formset.save(commit=False)
            for form in formset:
                new_item = form.save(commit=False)
                if new_item.title:
                    new_item.product_id = self.kwargs.get('id')
                    new_item.save()
            messages.success(request, 'Success')
            return redirect('product_list')
        raise Http404


class ProductListView(ListView):
    """
    """
    model = models.Product
    template_name = 'products/product_list.html'
    
    def get_queryset(self, *args, **kwargs):
        queryset = super(ProductListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        if query:
            queryset = self.model.objects.filter(
                        Q(title__icontains=query)|
                        Q(description__icontains=query)
                        )
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        return context


class ProductDetailView(DetailView):
    """
    class based product detail view
    """
    model = models.Product
    pk_url_kwarg = 'id'
    template_name = 'products/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        obj = self.get_object()
        context['related_products'] = sorted(self.model.objects.get_related_products(obj)[:5], key= lambda x :random.random())
        return context
