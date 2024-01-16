from collections import OrderedDict

from django.db.models import Sum, Value, Count
from django.db.models.functions import Coalesce
from django.db.models.functions import TruncMonth

def summary_per_category(queryset):
    return OrderedDict(sorted(
        queryset
        .annotate(category_name=Coalesce('category__name', Value('-')))
        .order_by()
        .values('category_name')
        .annotate(s=Sum('amount'))
        .values_list('category_name', 's')
    ))

def number_of_exp_per_category(queryset):
    return OrderedDict(sorted(
        queryset
        .annotate(category_name=Coalesce('category__name', Value('-')))
        .order_by()
        .values('category_name')
        .annotate(s=Count('amount'))
        .values_list('category_name', 's')
    ))

def total_amount_spent(queryset):
    return queryset.aggregate(Sum('amount'))

def summary_per_year_month(queryset):
    year_month = TruncMonth('date')
    return OrderedDict(sorted(
        queryset
        .annotate(date__name=Coalesce('date', Value('-')))
        .order_by()
        .values('date__year')
        .annotate(s=Sum('amount'))
        .values_list(year_month, 's')
    ))