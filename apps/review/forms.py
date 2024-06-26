from django import forms
from apps.shop.models import ProductModel, ProductStatusType
from .models import ReviewModel


class SubmitReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = ['product', 'rate', 'description']
        error_messages = {
            'description': {'required': 'فیلد توضیحات اجباری است'},
        }

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get('product')
        try:
            ProductModel.objects.get(id=product.id, status=ProductStatusType.publish.value)
        except ProductModel.DoesNotExist:
            raise forms.ValidationError("این محصول وجود ندارد")
        return cleaned_data
