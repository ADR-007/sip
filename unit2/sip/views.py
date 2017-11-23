import json

import channels.handler
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from sip.models import SipState


class SipView(TemplateView):
    template_name = 'sip.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return render(request, self.template_name, context)


class SipWebhookView(TemplateView):
    template_name = 'sip.html'

    def post(self, request: channels.handler.AsgiRequest, *args, **kwargs):
        username = json.loads(request.body)['username']
        state = json.loads(request.body)['state']

        sip_state = SipState.objects.filter(username=username).first()
        if sip_state:
            sip_state.last_state = state
            sip_state.save()
        else:
            SipState(username=username, last_state=state).save()

        return HttpResponse(json.dumps({'message': 'Ok'}), content_type="application/json")
