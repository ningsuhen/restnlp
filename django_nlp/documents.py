# Create your models here.
from mongoengine import StringField
from mongoengine.document import Document
from mongoengine.fields import ListField, ReferenceField


# class Language(Document):
#     name = StringField(required=True)
#     abbr = StringField(max_length=2)


class Conversation(Document):
    messages = ListField(field=ReferenceField('Foo'))


class Speaker(Document):
    name = StringField()


class Message(Document):
    text = StringField(required=True)
    speaker = ReferenceField('Speaker')


class Sentence(Document):
    text = StringField(required=True)
    words = ListField(field=ReferenceField('Word'))


class Word(Document):
    text = StringField(required=True)
