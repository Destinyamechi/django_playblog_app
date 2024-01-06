from django.db import models
from customer.models import Customer
import uuid
from company.models import *
# Create your models here.

class Order(models.Model):
    ARMED = 'ARMED'
    UNARMED = 'UNARMED(BUT IN POSSESION OF OTHER PROTECTIVE EQUIPMENT)'
    status = [
        (ARMED, ('Armed')),
        (UNARMED,('Unarmed(But in Possesion of other protective equipment)'))
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE)
    mode = models.ForeignKey(Mode, on_delete=models.CASCADE)
    location = models.TextField(max_length = 700, null = True, blank = False)
    arms_choice = models.CharField(max_length=70, choices=status, default=UNARMED)

    def __str__(self):
        return f"{self.customer}|{self.order_id}"   



