from django.shortcuts import render, redirect
from .models import Invoice
from .forms import InvoiceForm
import qrcode
from io import BytesIO
import base64
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_detail', invoice_id=form.instance.id)
    else:
        form = InvoiceForm()
    return render(request, 'invoice_final/create_invoice.html', {'form': form})

def invoice_detail(request, invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    
   
    qr = qrcode.make(invoice.qr_code_data or "https://example.com")  
    qr_image = BytesIO()
    qr.save(qr_image, format="PNG")
    qr_image.seek(0)
    qr_code_base64 = base64.b64encode(qr_image.getvalue()).decode("utf-8")
    
    return render(request, 'invoice_final/invoice_detail.html', {'invoice': invoice, 'qr_code_base64': qr_code_base64})

def home(request):
    return render(request, 'invoice_final/home.html')



from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('create_invoice')  # Redirect to the invoice form after login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'home.html')

# views.py
@login_required
def dashboard(request):
    return render(request, 'invoice_final/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('home')

