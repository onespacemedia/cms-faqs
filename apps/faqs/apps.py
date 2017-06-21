from cms.models import PageBaseSearchAdapter
from django.apps import AppConfig
from watson import search as watson


class FaqsConfig(AppConfig):
    name = '{{ project_name }}.apps.faqs'
    verbose_name = 'FAQ'
    verbose_name_plural = 'FAQs'

    def ready(self):
        Faq = self.get_model('Faq')
        watson.register(Faq, adapter_cls=PageBaseSearchAdapter)
