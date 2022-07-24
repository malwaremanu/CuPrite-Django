from django.db import models
import datetime, uuid

# Create your models here.
class Party(models.Model): 
    p_uuid=models.UUIDField(primary_key = True, default = uuid.uuid4)
    p_name = models.TextField()
    p_address_1 = models.TextField(blank=True)
    p_address_2 = models.TextField(blank=True)
    p_author = models.CharField(max_length=100, default="System")
    p_date = models.DateTimeField(default=datetime.datetime.now())
    
    p_id_rccm = models.CharField(max_length=100, blank=True)
    p_id_id = models.CharField(max_length=100, blank=True)
    p_id_tva = models.CharField(max_length=100, blank=True)
    p_id_nif = models.CharField(max_length=100, blank=True)

    p_cp_1_name = models.CharField(max_length=100, blank=True)
    p_cp_1_phone = models.CharField(max_length=100, blank=True)
    p_cp_1_email = models.CharField(max_length=100, blank=True)

    p_cp_2_name = models.CharField(max_length=100, blank=True)
    p_cp_2_phone = models.CharField(max_length=100, blank=True)
    p_cp_2_email = models.CharField(max_length=100, blank=True)

    p_contacts_email = models.CharField(max_length=100, blank=True)
    p_contacts_phone = models.CharField(max_length=100, blank=True)
    p_contacts_fax = models.CharField(max_length=100, blank=True)
    p_contacts_website = models.CharField(max_length=100, blank=True)

    p_is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.p_name

    def __repr__(self) -> str:
        return self.p_name +" : "+ str(self.p_uuid)

    def show_all(self):
        return {
            "p_uuid" : self.p_uuid,
            "p_name" : self.p_name,
            "p_address_1" : self.p_address_1,
            "p_address_2" : self.p_address_2,

            "p_author" : self.p_author,
            "p_date" : self.p_date,
            
            "p_id_rccm" : self.p_id_rccm,
            "p_id_id" : self.p_id_id,
            "p_id_tva" : self.p_id_tva,
            "p_id_nif" : self.p_id_nif,
            
            "p_cp_1_name" : self.p_cp_1_name,
            "p_cp_1_phone" : self.p_cp_1_phone,
            "p_cp_1_email" : self.p_cp_1_email,

            "p_cp_2_name" : self.p_cp_2_name,
            "p_cp_2_phone" : self.p_cp_2_phone,
            "p_cp_2_email" : self.p_cp_2_email,

            "p_contacts_email" : self.p_contacts_email,
            "p_contacts_phone" : self.p_contacts_phone,
            "p_contacts_fax" : self.p_contacts_fax,
            "p_contacts_website" : self.p_contacts_website,

            "p_is_active" : self.p_is_active
        }