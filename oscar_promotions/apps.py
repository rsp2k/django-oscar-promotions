from django.urls import include, re_path
from django.utils.translation import gettext_lazy as _
from oscar.core.application import OscarConfig
from oscar.core.loading import get_class, get_model


class PromotionsConfig(OscarConfig):

    label = 'oscar_promotions'
    name = 'oscar_promotions'
    verbose_name = _("Promotions")

    namespace = 'promotions'

    def ready(self):
        super().ready()
        self.home_view = get_class('oscar_promotions.views', 'HomeView', module_prefix='oscar_promotions')
        self.record_click_view = get_class(
            'oscar_promotions.views', 'RecordClickView', module_prefix='oscar_promotions'
        )

    def get_urls(self):
        PagePromotion = get_model('oscar_promotions', 'PagePromotion')
        KeywordPromotion = get_model('oscar_promotions', 'KeywordPromotion')
        urls = [


            re_path(
                r'page-redirect/(?P<page_promotion_id>\d+)/$',
                self.record_click_view.as_view(model=PagePromotion),
                name='page-click',
            ),
            re_path(
                r'keyword-redirect/(?P<keyword_promotion_id>\d+)/$',
                self.record_click_view.as_view(model=KeywordPromotion),
                name='keyword-click',
            ),
            re_path(r'^$', self.home_view.as_view(), name='home'),
        ]
        return self.post_process_urls(urls)
