from django.db import models

class QRCode(models.Model):
    data = models.CharField(max_length=255)
    foreground_color = models.CharField(max_length=7)
    background_color = models.CharField(max_length=7)

class QRC(models.Model):
    qr_code_image = models.ImageField(upload_to='qr_codes/')
    qr_data = models.CharField(max_length=255)
    scan_location = models.CharField(max_length=255)
    scan_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.qr_data