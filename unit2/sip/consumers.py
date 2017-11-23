from channels.auth import channel_session_user_from_http
from channels.channel import Group
from django.db.models.base import ModelBase
from django.db.models.signals import post_save
from django.dispatch import receiver
import json

from accounts.models import User
from sip.models import SipState


@receiver(post_save, sender=SipState)
def state_changed(sender: ModelBase, instance: SipState, **kwargs):
    Group(str(instance.username)).send({'text': json.dumps({'state': instance.last_state})})


@channel_session_user_from_http
def ws_connect(message):
    message.reply_channel.send({"accept": True})
    Group(message.user.username).add(message.reply_channel)
    send_user_state(message.user)


@channel_session_user_from_http
def ws_disconnect(message):
    Group(message.user.username).discard(message.reply_channel)


def send_user_state(user: User):
    sip_account = SipState.objects.filter(username=user.username).first()
    if sip_account:
        Group(user.username).send({'text': json.dumps({'state': sip_account.last_state})})
    else:
        Group(user.username).send({'text': json.dumps({'state': 'N/A'})})
