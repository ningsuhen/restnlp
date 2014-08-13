from api import ConversationResource, SpeakerResource, MessageResource, SentenceResource, WordResource
from tastypie.api import Api
from django.conf.urls import patterns, include, url

v1_api = Api(api_name='v1')

v1_api.register(ConversationResource())
v1_api.register(SpeakerResource())
v1_api.register(MessageResource())
v1_api.register(SentenceResource())
v1_api.register(WordResource())

urlpatterns = patterns(
    '',
    url('', include(v1_api.urls)),
)
