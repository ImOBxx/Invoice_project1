from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'  
        widgets = {
            'invoice_date': forms.DateInput(attrs={'type': 'date'}),
            'po_date': forms.DateInput(attrs={'type': 'date'}),
            'remarks': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'invoice_number': 'Invoice Number ',
            'invoice_date': 'Invoice Date ',
            'customer_code': 'Customer Code ',
            'po_date': 'Purchase Order Date ',
            'sales_executive': 'Sales Executive ',

            # Buyer Information
            'buyer_name': 'Buyer Name ',
            'buyer_address': 'Buyer Address ',
            'buyer_gst': 'Buyer GSTIN Number ',
            'buyer_pan': 'Buyer PAN Number ',
            'buyer_email': 'Buyer Email ID ',
            'buyer_mobile': 'Buyer Mobile Number ',
            'payment_terms' : 'Payment Method ',

            # Seller Information
            'seller_name': 'Seller Name ',
            'seller_address': 'Seller Address ',
            'seller_gst': 'Seller GSTIN ',
            'seller_pan': 'Seller PAN Number ',
            'seller_email': 'Seller Email ID ',
            'seller_mobile': 'Seller Mobile Number ',

            # Product and Payment Details
            'total_qty': 'Total Quantity ',
            'net_amount': 'Net Amount (₹) ',
            'sgst': 'SGST (₹) ',
            'cgst': 'CGST (₹) ',
            'igst': 'IGST (₹) ',
            'gross_amount': 'Gross Amount ',
            'discount': 'Discount (₹) ',
            'total_amount': 'Total Amount (₹) ',
            'amount_in_words': 'Amount in Words ',
            

            # Additional Information
            'remarks': 'Remarks ',
            'qr_code_data': 'QR Code Data ',
        }