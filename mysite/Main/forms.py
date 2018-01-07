from django import forms

from .models import Post,Gallery

class PostForm(forms.ModelForm):
    image = forms.ImageField(label='A must')
    # image_2 = forms.ImageField(label='A must')
    # image_3 = forms.ImageField(label='A must')
    # image_4 = forms.ImageField(label='A must')
    # image_5 = forms.ImageField(label='A must')
    class Meta:
        model = Post
        fields = [
            "title",
            "description",
            "image",
            "image_2",
            "image_3",
            "location_details",
            "size_of_land",
            "price",
            "features",

        ]
        
class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = [
            'image_title',
            'image_description',
            'gallery_image'
            ]