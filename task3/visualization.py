from task3.models import Fp_data
from django.db.models import Sum

distinct_fund_type = Fp_data.objects.values('fund_type').distinct()


# return fund type and total asset under management
def fund_type_total():

    list1 = []
    list2 = []

    for i in distinct_fund_type:
        list1.append(i['fund_type'])

    for j in list1:
        list2.append(Fp_data.objects.filter(fund_type=j).aggregate(Sum('net_asset'))['net_asset__sum'])

    return list1, list2


list_of_fund_type, list_of_asset_under_maangement = fund_type_total()[0], fund_type_total()[1]
