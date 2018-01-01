from django import forms


from .models import Team_Meamber

class Team_MeamberForm(forms.ModelForm):
    class Meta:
        model = Team_Meamber
        fields = [
            "members_name",
            "members_role",
            "members_details",
            "members_phone_number",
            "members_email",
            "members_image"
            ]
