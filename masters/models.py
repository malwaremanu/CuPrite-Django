from django.db import models
import datetime, uuid

# Create your models here.
class Party(models.Model): 
    p_uuid=models.UUIDField(primary_key = True, default = uuid.uuid4)
    p_name = models.TextField()
    p_address = models.TextField()
    p_author = models.TextField()
    p_email = models.TextField()
    p_date = models.DateTimeField(default=datetime.datetime.now())
    p_company = models.TextField()
    p_is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.p_name

    def show_all(self):
        return {
            "p_uuid" : self.p_uuid,
            "p_name" : self.p_name,
            "p_email" : self.p_email.lower(),
            "p_address" : self.p_address,
            "p_author" : self.p_author,
            "p_date" : self.p_date,
            "p_company" : self.p_company,
            "p_is_active" : self.p_is_active
        }
        
        