from django.views.generic import ListView, DetailView

from .models import Faq, Category


class FaqListView(ListView):
    model = Faq


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