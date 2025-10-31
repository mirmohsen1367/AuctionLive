from django.contrib import admin
from django import forms
from django.utils import timezone
from .models import AuctionItem

class AuctionItemForm(forms.ModelForm):
    class Meta:
        model = AuctionItem
        fields = "__all__"

    def clean_ends_at(self):
        if self.cleaned_data["ends_at"] < timezone.now():
            raise forms.ValidationError("No valid ends_at")
        return self.cleaned_data["ends_at"]

@admin.register(AuctionItem)
class AuctionItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "current_price", "ends_at", "winner")
    form = AuctionItemForm
