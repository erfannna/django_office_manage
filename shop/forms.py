from django import forms
from .models import ProductBuyOrder, ProductStockroomOrder, Note
from jalali_date_new.fields import JalaliDateField, JalaliDateTimeField
from jalali_date_new.widgets import AdminJalaliDateWidget, AdminJalaliTimeWidget,\
									AdminJalaliDateTimeWidget


REQUEST_STATUS = [
    ("تمام موارد", "تمام موارد"),
    ("بررسی نشده", "بررسی نشده"),
    ("بررسی بیشتر", "بررسی بیشتر"),
    ("موافقت شده", "موافقت شده"),
    ("رد شده", "رد شده")
]


class ProductBuyForm(forms.ModelForm):

    class Meta:
        model = ProductBuyOrder
        fields = ('name', 'brand', 'count', 'order_type', 'description')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "formTextBox",
                'id': "name",
                'maxlength': "150",
                'placeholder': "نام کالا",
                'required': "true"
            }),
            'brand': forms.TextInput(attrs={
                'class': "formTextBox",
                'id': "brand",
                'maxlength': "50",
                'placeholder': "برند",
                'required': "true"
            }),
            'count': forms.NumberInput(attrs={
                'class': "formTextBox",
                'id': "count",
                'placeholder': "تعداد",
            }),
            'order_type': forms.Select(attrs={
                'class': "formTextBox",
                'id': "order_type",
                'placeholder': "نوع سفارش",
            }),
            'description': forms.Textarea(attrs={
                'class': "formTextBox",
                'id': "description",
                'placeholder': "توضیحات",
                'maxlength': "250"
            })
        }


class ProductBuyReviewForm(forms.ModelForm):

    class Meta:
        model = ProductBuyOrder
        fields = ('status', 'completed')
        widgets = {
            'completed': forms.CheckboxInput(attrs={
                'class': "formTextBox",
                'id': "completed",
            }),
            'status': forms.Select(attrs={
                'class': "formTextBox",
                'id': "status",
            })
        }


class ProductStockForm(forms.ModelForm):

    class Meta:
        model = ProductStockroomOrder
        fields = ('name', 'brand', 'count', 'order_type', 'description')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "formTextBox",
                'id': "name",
                'maxlength': "150",
                'placeholder': "نام کالا",
                'required': "true"
            }),
            'brand': forms.TextInput(attrs={
                'class': "formTextBox",
                'id': "brand",
                'maxlength': "50",
                'placeholder': "برند",
                'required': "true"
            }),
            'count': forms.NumberInput(attrs={
                'class': "formTextBox",
                'id': "count",
                'placeholder': "تعداد",
            }),
            'order_type': forms.Select(attrs={
                'class': "formTextBox",
                'id': "order_type",
                'placeholder': "نوع سفارش",
            }),
            'description': forms.Textarea(attrs={
                'class': "formTextBox",
                'id': "description",
                'placeholder': "توضیحات",
                'maxlength': "250"
            })
        }


class ProductStockReviewForm(forms.ModelForm):

    class Meta:
        model = ProductStockroomOrder
        fields = ('status', 'completed')
        widgets = {
            'completed': forms.CheckboxInput(attrs={
                'class': "formTextBox",
                'id': "completed",
            }),
            'status': forms.Select(attrs={
                'class': "formTextBox",
                'id': "status",
            })
        }


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={
                'class': "formTextBox",
                'id': "text",
                'placeholder': "یادداشت خود را بنویسید...",
                'maxlength': "250"
            })
        }


class SearchForm(forms.Form):

    start_date = JalaliDateTimeField(label="تاریخ شروع",
                                     widget=AdminJalaliDateWidget)
    start_date.widget.attrs.update({'class': 'formTextBox'})
    start_date.widget.attrs.update({'placeholder': 'تاریخ شروع'})

    end_date = JalaliDateTimeField(label="تاریخ پایان",
                                   widget=AdminJalaliDateWidget)
    end_date.widget.attrs.update({'class': 'formTextBox'})
    end_date.widget.attrs.update({'placeholder': 'تاریخ پایان'})

    status = forms.CharField(widget=forms.Select(attrs={
        'class': "formTextBox",
        'id': "status",
    }, choices=REQUEST_STATUS), label="وضعیت")