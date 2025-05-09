from django.urls import path
from financial.views import admission_fee
from financial.views import yearly_fee

urlpatterns = [
    path('fee/',admission_fee),
    path('money/',yearly_fee),
]    