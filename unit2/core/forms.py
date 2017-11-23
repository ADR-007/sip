from django.forms import Form


class ProductEditForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['owner', 'views_count']