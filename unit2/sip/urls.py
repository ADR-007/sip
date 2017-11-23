from django.conf.urls import url

from sip.views import SipView, SipWebhookView

urlpatterns = [
    url(r'^$', SipView.as_view(), name="sip"),
    url(r'^webhook$', SipWebhookView.as_view(), name="sipwebhook"),
]
