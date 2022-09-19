from django.db import models
import datetime, uuid
from masters.models import Party

class Order(models.Model): 
    #p_uuid=models.UUIDField(primary_key = True, default = uuid.uuid4)
    po_no = models.AutoField(primary_key=True)
    po_date = models.DateField()
    po_party = models.ForeignKey(Party, on_delete=models.CASCADE)
