from django import forms

from .models import Subscribe,Testimony

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ["email","name"]

    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data.get("email")
        print(email)
        qs = Subscribe.objects.filter(email__iexact=email)
        if qs.exists():
            print('exists')
            raise forms.ValidationError("Sorry This Email is Already Subscribed.. ")
        return email




class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = [
            "title",
            "testimony",
            "image"
        ]
        