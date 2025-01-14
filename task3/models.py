from django.db import models


class Fp_data(models.Model):
    reg_no = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    rank_of_12_month = models.FloatField(null=True, blank=True)
    rank_of_24_month = models.FloatField(null=True, blank=True)
    rank_of_36_month = models.FloatField(null=True, blank=True)
    rank_of_48_month = models.FloatField(null=True, blank=True)
    rank_of_60_month = models.FloatField(null=True, blank=True)
    rank_last_update = models.DateTimeField(null=True, blank=True)
    fund_type = models.IntegerField(null=True, blank=True)
    type_of_invest = models.CharField(max_length=255, null=True, blank=True)
    fund_size = models.BigIntegerField(null=True, blank=True)
    initiation_date = models.DateTimeField(null=True, blank=True)
    daily_efficiency = models.FloatField(null=True, blank=True)
    weekly_efficiency = models.FloatField(null=True, blank=True)
    monthly_efficiency = models.FloatField(null=True, blank=True)
    quarterly_efficiency = models.FloatField(null=True, blank=True)
    six_month_efficiency = models.FloatField(null=True, blank=True)
    annual_efficiency = models.FloatField(null=True, blank=True)
    statistical_nav = models.FloatField(null=True, blank=True)
    efficiency = models.FloatField(null=True, blank=True)
    cancel_nav = models.FloatField(null=True, blank=True)
    issue_nav = models.FloatField(null=True, blank=True)
    dividend_interval_period = models.BigIntegerField(null=True, blank=True)
    guaranteed_earning_rate = models.FloatField(null=True, blank=True)
    data = models.TextField(null=True, blank=True)
    net_asset = models.BigIntegerField(null=True, blank=True)
    estimated_earning_rate = models.FloatField(null=True, blank=True)
    invested_units = models.BigIntegerField(null=True, blank=True)
    articles_of_association_link = models.URLField(null=True, blank=True)
    prospectus_link = models.URLField(null=True, blank=True)
    website_address = models.URLField(null=True, blank=True)
    manager = models.CharField(max_length=255)
    manager_seo_register_no = models.BigIntegerField(null=True, blank=True)
    guarantor_seo_register_no = models.BigIntegerField(null=True, blank=True)
    auditor = models.CharField(max_length=255, null=True, blank=True)
    custodian = models.CharField(max_length=255, null=True, blank=True)
    guarantor = models.CharField(max_length=255, null=True, blank=True)
    beta = models.FloatField(null=True, blank=True)
    alpha = models.FloatField(null=True, blank=True)
    is_completed = models.BooleanField(null=True, blank=True)
    five_best = models.FloatField(null=True, blank=True)
    stock = models.FloatField(null=True, blank=True)
    bond = models.FloatField(null=True, blank=True)
    other = models.FloatField(null=True, blank=True)
    cash = models.FloatField(null=True, blank=True)
    deposit = models.FloatField(null=True, blank=True)
    fund_unit = models.FloatField(null=True, blank=True)
    commodity = models.FloatField(null=True, blank=True)
    fund_publisher = models.BigIntegerField(null=True, blank=True)
    small_symbol_name = models.CharField(max_length=255, null=True, blank=True)
    ins_code = models.CharField(max_length=255, null=True, blank=True)
    fund_watch = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Fp_data'
