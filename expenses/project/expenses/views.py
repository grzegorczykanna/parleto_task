from django.views.generic.list import ListView

from .forms import ExpenseSearchForm, ExpenseSearchFormDate, ExpenseSearchFormSort
from .models import Expense, Category
from .reports import summary_per_category
from .reports import summary_per_year_month
from .reports import number_of_exp_per_category
from .reports import total_amount_spent
import datetime

class ExpenseListView(ListView):
    model = Expense
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        form = ExpenseSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name', '').strip()
            if name:
                queryset = queryset.filter(name__icontains=name)

        formDateStart = ExpenseSearchFormDate(self.request.GET)
        if formDateStart.is_valid():
            dateStart = self.request.GET.get("datestart")
            if dateStart:
                year = dateStart.split("-")[0]
                month = dateStart.split("-")[1]
                day = dateStart.split("-")[2]
                queryset = queryset.filter(date__gt=datetime.date(int(year), int(month), int(day)))
           
        formDateEnd = ExpenseSearchFormDate(self.request.GET)
        if formDateStart.is_valid():
            dateEnd = self.request.GET.get("endstart")
            if dateEnd:
                year = dateEnd.split("-")[0]
                month = dateEnd.split("-")[1]
                day = dateEnd.split("-")[2]
                queryset = queryset.filter(date__lt=datetime.date(int(year), int(month), int(day)))
        
        formSortByCat = ExpenseSearchFormSort(self.request.GET)
        if formDateStart.is_valid():
            sortByCat = self.request.GET.get("sortbycat")
            if sortByCat == "ASC":
                queryset = queryset.order_by('category')   
            if sortByCat == "DESC":
                queryset = queryset.order_by('category').reverse()   

        return super().get_context_data(
            form=form,
            formDateStart=formDateStart,
            formDateEnd=formDateEnd,
            formSortByCat=formSortByCat,
            object_list=queryset,
            summary_per_category=summary_per_category(queryset),
            number_of_exp_per_category = number_of_exp_per_category(queryset),
            total_amount_spent = total_amount_spent(queryset),
            summary_per_year_month=summary_per_year_month(queryset),
            **kwargs)

class CategoryListView(ListView):
    model = Category
    paginate_by = 5
