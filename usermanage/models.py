import uuid
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="created at")
    updated_at = models.DateTimeField(default=timezone.now, verbose_name="updated at")

    class Meta:
        abstract = True

class OtherUser(User, BaseModel):
    phone_number = models.CharField(max_length=100, null=False, blank=True)
    status = models.ForeignKey("State", on_delete=models.CASCADE, null=True, blank=True)
    corporate = models.ForeignKey("Corporate", on_delete=models.CASCADE, null=True, blank=True)

    # def __str__(self):
    #     return "%s" % self.id

class GenericBaseModel(BaseModel):
    name = models.CharField(max_length=200, null=False, default=True)
    description = models.TextField(max_length=200, null=False)

    class Meta:
        abstract = True

class Corporate(GenericBaseModel):
    alias = models.CharField(max_length=100, unique=True, null=False, blank=False)
    status = models.ForeignKey("State",on_delete=CASCADE, null=True, blank=True)

    def save(self, **kwargs):
        super().save(**kwargs)
#
class State(GenericBaseModel):
    # state_choices = [
    #     ('active', 'Active'),
    #     ('disabled', 'disabled'),
    #     ('pending approval', 'Pending Approval'),
    #     ('inactive', 'Inactive')
    # ]
    # status = models.CharField(max_length=200, choices=state_choices, default=True)
    def __str__(self):
        return "%s - %s" % (self.name, self.created_at)
