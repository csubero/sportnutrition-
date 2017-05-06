from django.forms import ModelForm

from backend.models import Image


class ImageForm(ModelForm):
	class Meta:
		model = Image

		fields = ['file', ]
