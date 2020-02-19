import sys
import os

import django

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_DIR not in sys.path:
    sys.path.append(PROJECT_DIR)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj.settings")
django.setup()

import django.apps
from django.db.models import ImageField
# from django.db.models import FileField

image_name = '/data/shop/media/sample.jpg'


for model in django.apps.apps.get_models():
    for field in model._meta.get_fields():
        # if isinstance(field, ImageField) or isinstance(field, FileField):
        if isinstance(field, ImageField):
            model_file_field = str(field).split('.')[-1]
            for obj in model.objects.all():
                getattr(obj, model_file_field).save(
                    image_name,
                    open(image_name, 'rb')
                )
                obj.save()
