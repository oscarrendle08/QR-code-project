



from django.shortcuts import render, redirect
from django.conf import settings
from qrcode import QRCode
import qrcode
from PIL import Image, ImageDraw
import os
import random
import string
from .models import QRCode as QRCodeModel
from .models import QRC
from io import BytesIO
import base64
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.urls import reverse
from django.core.files.storage import FileSystemStorage



def home(request):
    # Logic for home page
    return render(request, 'home.html')

def about(request):
    # Logic for about page
    return render(request, 'about.html')

# mywebsite/views.py


def qr_generation(request):
    if request.method == 'POST':
        # Get form data
        file_name = request.POST.get('file_name')
        qr_data = request.POST.get('qr_data')
        qr_format = request.POST.get('qr_format')
        fg_color = request.POST.get('fg_color')
        bg_color = request.POST.get('bg_color')

        # Generate QR code
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fg_color, back_color=bg_color)

        # Save QR code image
        file_extension = '.jpg' if qr_format == 'jpg' else '.png'
        file_path = 'static/{}{}'.format(file_name, file_extension)
        img.save(file_path)

        # Render template with QR code image path
        context = {'file_path': file_path, 'file_name': file_name, 'file_extension': file_extension}
        return render(request, 'qr_generation.html', context)

    return render(request, 'qr_generation.html')

def analytics(request):
    # Retrieve QR codes from database
    qr_codes = QRC.objects.all()

    # Render template with QR codes and analytics information
    context = {'qr_codes': qr_codes}
    return render(request, 'analytics.html', context)
