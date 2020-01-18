from django import forms
from . import models


class CreateReviewForm(forms.ModelForm):

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
