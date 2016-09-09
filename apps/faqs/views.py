from django.views.generic import DetailView, ListView

from .models import Category, Faq


class FaqListView(ListView):
    model = Faq

    def get_paginate_by(self, queryset):
        return self.request.pages.current.content.per_page


class FaqView(DetailView):
    model = Faq
    slug_field = 'url_title'
    slug_url_kwarg = 'faq_title'


class FaqCategoryListView(ListView):
    model = Category


class FaqCategoryView(DetailView):
    model = Category
    slug_field = 'url_title'
    slug_url_kwarg = 'category_title'
