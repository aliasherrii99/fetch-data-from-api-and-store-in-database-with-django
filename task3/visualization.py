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
list_of_fund_type2 = sorted(list_of_fund_type, reverse=True)
list_of_asset_under_maangement2 = []
for i in list_of_fund_type2:
    list_of_asset_under_maangement2.append(list_of_asset_under_maangement[list_of_fund_type.index(i)])

name_from_fund_type = {
    4: 'در اوراق بهادار با درآمد ثابت',
    5: 'در اوراق بهادار مبتنی بر سپرده کالایی',
    6: 'در سهام',
    7: 'مختلط',
    11: 'اختصاصی بازارگردانی',
    12: 'جسورانه',
    13: 'پروژه‌ای',
    14: 'زمین و ساختمان',
    16: 'خصوصی',
    17: 'صندوق در صندوق',
    18: 'املاک و مستغلات',
    21: 'در سهام-بخشی',
    22: 'در سهام-سهامی اهرمی',
    23: 'در سهام-شاخصی',
    24: 'با تضمین اصل مبلغ سرمایه گذاری',
    25: 'بازنشستگی تکمیلی'
}
list_of_fund_type3 = []
for i in list_of_fund_type2:
    list_of_fund_type3.append(name_from_fund_type[i])

# def show():
#     # print(list(zip(list_of_fund_type, list_of_asset_under_maangement)))
#     print(list(zip(list_of_fund_type2, list_of_asset_under_maangement2)))

# py manage.py shell
# from task3.visualization import show