from django.db import models
import uuid
from django.conf import settings
from django.core.exceptions import ValidationError

class Conversation(models.Model):
    code = models.UUIDField(primary_key=True, default=uuid.uuid4)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="conversations")
    def clean(self):
        # Ensure the conversation has at least two participants
        if self.pk and self.participants.count() < 2:
            raise ValidationError("A conversation must have at least two participants.")

    def save(self):
        self.clean()
        super().save()
    def __str__(self):
        return str(self.code)




class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    conversation = models.ForeignKey(Conversation, related_name="messages", on_delete=models.CASCADE,null=True)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sent_messages",null=True)
    date = models.DateField(auto_now_add=True, null=True)
    time = models.TimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        if self.conversation:
            if self.author:
                if not self.conversation.participants.filter(id=self.author.id).exists():
                    raise ValidationError('Author should be part of the conversations participants')
        super().save(*args,**kwargs)
