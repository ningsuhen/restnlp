from tastypie.resources import ModelResource
from documents import Conversation, Message, Sentence, Speaker, Word
from tastypie_mongoengine import resources
from tastypie import authorization


class ConversationResource(resources.MongoEngineResource):
    class Meta:
        queryset = Conversation.objects.all()
        resource_name = 'conversations'
        allowed_methods = ('get', 'post', 'put', 'delete')
        authorization = authorization.Authorization()


class SpeakerResource(resources.MongoEngineResource):
    class Meta:
        queryset = Speaker.objects.all()
        resource_name = 'speakers'
        allowed_methods = ('get', 'post', 'put', 'delete')
        authorization = authorization.Authorization()


class MessageResource(resources.MongoEngineResource):
    class Meta:
        queryset = Message.objects.all()
        resource_name = 'messages'
        allowed_methods = ('get', 'post', 'put', 'delete')
        authorization = authorization.Authorization()


class SentenceResource(resources.MongoEngineResource):
    class Meta:
        queryset = Sentence.objects.all()
        resource_name = 'sentences'
        allowed_methods = ('get', 'post', 'put', 'delete')
        authorization = authorization.Authorization()


class WordResource(resources.MongoEngineResource):
    class Meta:
        queryset = Word.objects.all()
        resource_name = 'words'
        allowed_methods = ('get', 'post', 'put', 'delete')
        authorization = authorization.Authorization()
