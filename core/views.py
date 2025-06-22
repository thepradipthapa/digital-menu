from django.shortcuts import render
from .froms import QRCodeForm
import qrcode,os
from django.conf import settings

# Create your views here.
def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():

            # Process the form data 
            vendor_name = form.cleaned_data['vendor_name']
            url = form.cleaned_data['url']
            print(vendor_name, url)

            # generate the QR code
            qr = qrcode.make(url)
            filename = vendor_name.replace(" ", "_").lower()+ '_menu_qr_by_digital_menu.png'
            file_path = os.path.join(settings.MEDIA_ROOT, filename)
            qr.save(file_path)

            # Create Image URL
            qr_url = os.path.join(settings.MEDIA_URL,filename)

            context = {
                'vendor_name': vendor_name,
                'qr_url': qr_url, 
                'filename': filename
            }
            return render(request, 'core/qr_code.html', context)
    else:
        form = QRCodeForm()

        context = {
            'form': form,
        }
        return render(request, 'core/generate_qr_code.html', context)