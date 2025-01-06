from django.shortcuts import render
from task3.visualization import list_of_fund_type3, list_of_asset_under_maangement2


# Create your views here.
def fund_type_view(request):
    fund_data = zip(list_of_fund_type3, list_of_asset_under_maangement2)
    return render(request, 'fund.html', {'fund_data': fund_data})