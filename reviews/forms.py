from django import forms
from . import models


class CreateReviewForm(forms.ModelForm):
    Accuracy = forms.IntegerField(max_value=5, min_value=1)
    Communication = forms.IntegerField(max_value=5, min_value=1)
    Cleanliness = forms.IntegerField(max_value=5, min_value=1)
    Location = forms.IntegerField(max_value=5, min_value=1)
    Check_in = forms.IntegerField(max_value=5, min_value=1)
    Value = forms.IntegerField(max_value=5, min_value=1)
    class Meta:
        model = models.Review
        fields = (
            "review",
            "Accuracy",
            "Communication",
            "Cleanliness",
            "Location",
            "Check_in",
            "Value",
        )

    def save(self):
        review = super().save(commit=False)
        return review
