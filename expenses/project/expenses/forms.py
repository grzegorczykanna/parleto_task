from django import forms
from .models import Expense

class ExpenseSearchForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False

class ExpenseSearchFormDate(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('date',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].required = False

class ExpenseSearchFormSort(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('category',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].required = False

