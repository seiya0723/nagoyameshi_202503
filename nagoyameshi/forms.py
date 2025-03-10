from django import forms
from .models import Review, Favorite, Reservation

# forms.py 投稿されたデータの検証

# レビュー
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [ "restaurant", "user", "content" ]

class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = [ "restaurant", "user" ]

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [ "restaurant", "user", "datetime", "headcount" ]
        