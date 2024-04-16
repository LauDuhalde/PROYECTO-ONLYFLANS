from django.db import models
from django.utils.text import slugify
import uuid

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(unique=True, blank=True)
    is_private = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Generar el slug automáticamente si no está definido
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(self,*args,**kwargs)
        #super(Flan, self).save(*args, **kwargs) #generado

    def __str__(self):
        return self.name
    
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
    
    def __str__(self):
        return self.customer_name