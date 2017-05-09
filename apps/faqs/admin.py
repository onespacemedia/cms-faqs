from cms.admin import PageBaseAdmin, SearchMetaBaseAdmin
from django.contrib import admin

from .models import Category, Faq


@admin.register(Faq)
class FaqAdmin(SearchMetaBaseAdmin):
    prepopulated_fields = {'slug': ('question',)}
    filter_horizontal = ['categories']

    fieldsets = (
        (None, {
            'fields': ['page', 'question', 'slug', 'answer', 'categories', 'order']
        }),
        SearchMetaBaseAdmin.PUBLICATION_FIELDS,
        SearchMetaBaseAdmin.SEO_FIELDS,
    )


@admin.register(Category)
class CategoryAdmin(PageBaseAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }

    fieldsets = (
        PageBaseAdmin.TITLE_FIELDS,
        ('Content', {
            'fields': ['content_primary']
        }),
        PageBaseAdmin.PUBLICATION_FIELDS,
        PageBaseAdmin.NAVIGATION_FIELDS,
        PageBaseAdmin.SEO_FIELDS,
    )
