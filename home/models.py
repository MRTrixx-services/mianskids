from django.db import models

class AdmissionEnquiry(models.Model):
    PROGRAM_CHOICES = [
        ('Day Care', 'Day Care'),
        ('Play Group', 'Play Group'),
        ('Pre-KG', 'Pre-KG'),
        ('Junior KG (LKG)', 'Junior KG (LKG)'),
        ('Senior KG (UKG)', 'Senior KG (UKG)'),
        ('General Enquiry', 'General Enquiry'),
    ]
    parent_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    child_name = models.CharField(max_length=100, blank=True)
    child_age = models.CharField(max_length=20, blank=True)
    program = models.CharField(max_length=50, choices=PROGRAM_CHOICES, blank=True)
    message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Admission Enquiry'
        verbose_name_plural = 'Admission Enquiries'

    def __str__(self):
        return f"{self.parent_name} – {self.program} ({self.submitted_at.strftime('%d %b %Y')})"
