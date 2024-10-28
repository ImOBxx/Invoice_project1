from django.db import models


class Invoice(models.Model):
   
    Invoice_Number = models.CharField(max_length=20)
    Invoice_Date = models.DateField()
    Invoice_Time = models.TimeField(auto_now_add=True)
    Customer_Code = models.CharField(max_length=20)
    PO_Date = models.DateField()
    Sales_Executive = models.CharField(max_length=100)
    
  
    buyer_name = models.CharField(max_length=100)
    buyer_address = models.TextField()
    buyer_gst = models.CharField(max_length=15)
    buyer_pan = models.CharField(max_length=10)
    buyer_email = models.EmailField()
    buyer_mobile = models.CharField(max_length=15)
    
    seller_name = models.CharField(max_length=100)
    seller_address = models.TextField()
    seller_gst = models.CharField(max_length=15)
    seller_pan = models.CharField(max_length=10)
    seller_email = models.EmailField()
    seller_mobile = models.CharField(max_length=15)
    
  
    total_qty = models.PositiveIntegerField()
    amount_in_words = models.CharField(max_length=200)
    
   
    payment_terms = models.CharField(max_length=100)
    net_amount = models.DecimalField(max_digits=12, decimal_places=2)
    sgst = models.DecimalField(max_digits=12, decimal_places=2)
    cgst = models.DecimalField(max_digits=12, decimal_places=2)
    igst = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    gross_amount = models.DecimalField(max_digits=15, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=15, decimal_places=2)
    
   
    remarks = models.TextField(blank=True, null=True)
    qr_code_data = models.TextField(blank=True, null=True)  

    def __str__(self):
        return f"Invoice #{self.invoice_number}"
