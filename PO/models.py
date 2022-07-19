from django.db import models
import datetime, uuid

# Create your models here.
class PO(models.Model): 
    p_uuid=models.UUIDField(primary_key = True, default = uuid.uuid4)
    p_no = models.CharField(max_length = 200,unique = True)
    p_date = models.DateTimeField()
    p_from_company = models.TextField()
    po_supplier = models.ForeignKey('masters.Party', on_delete=models.CASCADE)
    p_is_active = models.BooleanField()
    p_tva_percentage = models.IntegerField()

    def __str__(self) -> str:
        return self.p_no

    def show_all(self):
        return {
            "uuid" : self.p_uuid,
            "p_no" : self.p_no.upper(),
            "po_supplier" : self.po_supplier.show_all(),
            "p_date" : self.p_date,
            "p_from_company" : self.p_from_company,
            "p_tva_percentage" : self.p_tva_percentage,
            "p_is_active" : self.p_is_active,
        }        
    
class product(models.Model):
    p_uuid=models.UUIDField(primary_key = True, default = uuid.uuid4)
    po_number = models.ForeignKey('PO.PO', on_delete=models.CASCADE)
    p_date = models.DateTimeField()  
    p_followup = models.DateTimeField()  
    p_part_no = models.TextField()
    p_description = models.TextField()
    p_quote_ref = models.TextField()
    p_comments = models.TextField()
    p_received = models.BooleanField(default=False)    
    p_discount = models.IntegerField()
    p_quantity = models.IntegerField()
    p_base_price = models.FloatField()

    def __str__(self) -> str:
        return str(self.po_number) + " - " + self.p_description

    def show_all(self):
        return {
            "uuid" : self.p_uuid,
            "p_no" : self.po_number.upper(),
            "p_date" : self.p_date,
            "p_followup" : self.p_followup,
            "p_part_no" : self.p_part_no,
            "p_description" : self.p_description,
            "p_quote_ref" : self.p_quote_ref,
            "p_comments" : self.p_comments,
            "p_received" : self.p_received,
            "p_discount" : self.p_discount,
            "p_quantity" : self.p_quantity,
            "p_base_price" : self.p_base_price,
        }