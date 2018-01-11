from django import forms


from .models import Team_Meamber

class Team_MeamberForm(forms.ModelForm):
    class Meta:
        model = Team_Meamber
        fields = [
            "name",
            "role",
            "details",
            "phone_number",
            "email",
            "image"
            ]




