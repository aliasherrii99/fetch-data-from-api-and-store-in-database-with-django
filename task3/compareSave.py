from task3.models import Fp_data
import requests
import json
from task3.fetchSave import DataV
from prefect import task, flow

fp_url = "https://fund.fipiran.ir/api/v1/fund/fundcompare"


# 1 return data from api
@task
def fetch_data_from_api(url):
    response = requests.get(url)
    return json.loads(response.text)


# 2 return validated data from API
@task
def validated_data_from_api(my_data):
    data_api = []
    for item in my_data["items"]:
        validated_item = DataV.model_validate(item)
        data_api.append(validated_item)
    return data_api


# 3 return list of regno in api
@task
def regno_in_api(valid_data):
    list_regno = []
    for i in valid_data:
        list_regno.append(i.reg_no)
    return list_regno


# 4 return list of regno in DB
@task
def regno_in_db():
    regno_list = Fp_data.objects.values_list("reg_no", flat=True)
    return list(regno_list)


# 5 return list of regno not in db
@task
def regno_not_in_db(regno_api, regno_db):
    result = []
    for regno in regno_api:
        if regno not in regno_db:
            result.append(regno)
    return result


# 6 return rows to be added
@task
def new_rows(valid_data, regno_not_in_db):
    result = []
    for item in valid_data:
        if item.reg_no in regno_not_in_db:
            result.append(item)
    return result


# 7 add new data to DB
@task
def save_new_data_to_db(rows_be_add_to_db):
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


# run ETL cycle
@flow
def etl_flow():
    # fetch data from api
    api_data = fetch_data_from_api(fp_url)

    # validate data
    valid_data = validated_data_from_api(api_data)

    # regno in db and api
    regno_api = regno_in_api(valid_data)
    regno_db = regno_in_db()

    # regno in api and not in db
    regno_miising = regno_not_in_db(regno_api, regno_db)

    # find rows be added
    rows_to_add = new_rows(valid_data, regno_miising)

    # save in db
    save_new_data_to_db(rows_to_add)
