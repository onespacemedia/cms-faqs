from cms.admin import PageBaseAdmin, SearchMetaBaseAdmin
from suit.admin import SortableModelAdmin
from django.contrib import admin

from .models import Category, Faq


@admin.register(Faq)
class FaqAdmin(SearchMetaBaseAdmin, SortableModelAdmin):
    prepopulated_fields = {'slug': ('question',)}
    filter_horizontal = ['categories']

    fieldsets = (
        (None, {
            'fields': ['page', 'question', 'slug', 'answer', 'categories']
        }),
        SearchMetaBaseAdmin.PUBLICATION_FIELDS,
        SearchMetaBaseAdmin.SEO_FIELDS,
    )
    def get_form(self, request, obj=None, **kwargs):
        form = super(FaqAdmin, self).get_form(request, obj, **kwargs)
        try:
            form.base_fields['page'].initial = Faq.objects.all()[0]
        except IndexError:
            pass
        return form


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
