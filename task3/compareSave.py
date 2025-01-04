from task3.models import Fp_data
import requests
import json
from task3.fetchSave import DataV

fp_url = "https://fund.fipiran.ir/api/v1/fund/fundcompare"


# 1 return data from api
def fetch_data_from_api(url):
    response = requests.get(url)
    return json.loads(response.text)


# 2 return validated data from API
def validated_data_from_api():
    my_data = fetch_data_from_api(fp_url)
    data_api = [DataV.model_validate(item) for item in my_data['items']]
    return data_api


# 3 return list of regno in api
def regno_in_api():
    list_regno = []
    for i in validated_data_from_api():
        list_regno.append(i.reg_no)
    return list_regno


# 4 return list of regno in DB
def regno_in_db():
    regno_list = Fp_data.objects.values_list('reg_no', flat=True)
    return list(regno_list)


list_of_regno_in_api = regno_in_api()
list_of_regno_in_db = regno_in_db()


# 5 return list of regno not in db
def regno_not_db():
    list_not_in_db = []
    for i in list_of_regno_in_api:
        if i in list_of_regno_in_db:
            pass
        else:
            list_not_in_db.append(i)
    return list_not_in_db


list_regno_not_in_db = regno_not_db()
validated_data = validated_data_from_api()


# 6 return rows to be added
def new_rows():
    rows_be_add = []
    for i in validated_data:
        if i.reg_no in list_regno_not_in_db:
            rows_be_add.append(i)
    return rows_be_add


rows_be_add_to_db = new_rows()


# 7 add new data to DB
def save_new_data_to_db():
    for item in rows_be_add_to_db:
        Fp_data.objects.create(
            reg_no=item.reg_no,
            name=item.name,
            rank_of_12_month=item.rank_of_12_month,
            rank_of_24_month=item.rank_of_24_month,
            rank_of_36_month=item.rank_of_36_month,
            rank_of_48_month=item.rank_of_48_month,
            rank_of_60_month=item.rank_of_60_month,
            rank_last_update=item.rank_last_update,
            fund_type=item.fund_type,
            type_of_invest=item.type_of_invest,
            fund_size=item.fund_size,
            initiation_date=item.initiation_date,
            daily_efficiency=item.daily_efficiency,
            weekly_efficiency=item.weekly_efficiency,
            monthly_efficiency=item.monthly_efficiency,
            quarterly_efficiency=item.quarterly_efficiency,
            six_month_efficiency=item.six_month_efficiency,
            annual_efficiency=item.annual_efficiency,
            statistical_nav=item.statistical_nav,
            efficiency=item.efficiency,
            cancel_nav=item.cancel_nav,
            issue_nav=item.issue_nav,
            dividend_interval_period=item.dividend_interval_period,
            guaranteed_earning_rate=item.guaranteed_earning_rate,
            data=item.data,
            net_asset=item.net_asset,
            estimated_earning_rate=item.estimated_earning_rate,
            invested_units=item.invested_units,
            articles_of_association_link=item.articles_of_association_link,
            prospectus_link=item.prospectus_link,
            website_address=item.website_address,
            manager=item.manager,
            manager_seo_register_no=item.manager_seo_register_no,
            guarantor_seo_register_no=item.guarantor_seo_register_no,
            auditor=item.auditor,
            custodian=item.custodian,
            guarantor=item.guarantor,
            beta=item.beta,
            alpha=item.alpha,
            is_completed=item.is_completed,
            five_best=item.five_best,
            stock=item.stock,
            bond=item.bond,
            other=item.other,
            cash=item.cash,
            deposit=item.deposit,
            fund_unit=item.fund_unit,
            commodity=item.commodity,
            fund_publisher=item.fund_publisher,
            small_symbol_name=item.small_symbol_name,
            ins_code=item.ins_code,
            fund_watch=item.fund_watch,
        )
