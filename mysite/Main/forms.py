from django import forms

from .models import Post

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
            "image_4",
            "image_5",
            "location_details",
            "size_of_land",
            "price",
            "features",

        ]
        