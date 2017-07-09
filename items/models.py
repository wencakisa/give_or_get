from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Item(models.Model):
    PHONE_REGEX = r'^\+?1?\d{9,15}$'
    PHONE_REGEX_MESSAGE = 'Phone number must be entered in the following format: \'+999 9999 999\'.'

    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=1024, blank=False)

    phone_regex_validator = RegexValidator(regex=PHONE_REGEX, message=PHONE_REGEX_MESSAGE)
    phone_number = models.CharField(max_length=16, blank=True, validators=[phone_regex_validator])

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    added_on = models.DateField(auto_now_add=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-added_on']

    def __str__(self):
        return '{class_name} - "{item_name}" by {item_owner}'.format(
            class_name=self.__class__.__name__,
            item_name=self.name,
            item_owner=self.owner
        )


class Deal(models.Model):
    FREE = 'F'
    RENT = 'R'
    BUY = 'B'
    DEAL_STATUSES = (
        (FREE, 'Free'),
        (RENT, 'Rent'),
        (BUY, 'Buy')
    )

    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=1024, blank=False)

    item = models.ForeignKey('Item', on_delete=models.CASCADE)

    status = models.CharField(max_length=1, choices=DEAL_STATUSES, default=FREE)

    def __str__(self):
        return '{class_name} for {item}'.format(
            class_name=self.__class__.__name__,
            item=self.item
        )
