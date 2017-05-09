import watson
from cms.apps.pages.models import ContentBase
from cms.models import HtmlField, PageBase, SearchMetaBase
from django.db import models


class Faqs(ContentBase):
    # The heading that the admin places this content under.
    classifier = 'apps'

    # The urlconf used to power this content's views.
    urlconf = '{{ project_name }}.apps.faqs.urls'

    standfirst = models.TextField(
        blank=True,
        null=True
    )

    per_page = models.IntegerField(
        'faqs per page',
        default=5,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'FAQs'
        verbose_name_plural = 'FAQs'

    def __unicode__(self):
        return self.page.title


class Category(PageBase):
    content_primary = HtmlField(
        'primary content',
        blank=True
    )

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'categeory'
        verbose_name_plural = 'categories'


class Faq(SearchMetaBase):
    page = models.ForeignKey(
        Faqs
    )

    question = models.CharField(
        max_length=256
    )

    answer = HtmlField()

    categories = models.ManyToManyField(
        Category,
        blank=True,
    )

    slug = models.CharField(
        max_length=256,
        unique=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    def __unicode__(self):
        return self.question

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
        ordering = ['order', 'id', 'question']

    def get_absolute_url(self):
        return self.page.page.reverse('faq', kwargs={
            'slug': self.slug,
        })

    # Workaround CMS bug
    @property
    def title(self):
        return self.question

watson.register(Faq)
