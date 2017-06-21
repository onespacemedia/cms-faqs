from cms.models import PageBaseSearchAdapter
from django.apps import AppConfig
from watson import search as watson


class FaqsConfig(AppConfig):
    name = 'FAQs'

    def ready(self):
        Faq = self.get_model('Faq')
        watson.register(Faq, adapter_cls=PageBaseSearchAdapter)
