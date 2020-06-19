import django_tables2 as tables
from .models import *
import itertools

attr_right_text = {"th":{"class":"text-right"}, "td":{"class":"text-right"}}

class NplClientsTable(tables.Table):
    Balans = tables.Column(verbose_name="Остаток кредита", attrs=attr_right_text)
    class Meta:
        model = NplClients
        orderable = False
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-centered table-hover mb-0", "thead": {"class": "thead-dark"}}
        exclude = ('id',)

class ToxicCreditsTable(tables.Table):
    Balans = tables.Column(verbose_name="Остаток р/с 16377", attrs=attr_right_text)
    class Meta:
        model = ToxicCredits
        orderable = False
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-centered table-hover mb-0", "thead": {"class": "thead-dark"}}
        exclude = ('id',)

class OverdueCreditsTable(tables.Table):
    Balans = tables.Column(verbose_name="Остаток р/с 16377", attrs=attr_right_text)
    class Meta:
        model = OverdueCredits
        orderable = False
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-centered table-hover mb-0", "thead": {"class": "thead-dark"}}
        exclude = ('id',)
        
        

class ReportDataTable(tables.Table):
    class Meta:
        model = ReportData
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-centered mb-0", "thead": {"class": "thead-light"}}
        orderable = False
        fields = (
            'UNIQUE_CODE',
            'BORROWER', 
            'BRANCH_NAME',
            'LOAN_BALANCE',
            )
class OverallInfoTable(tables.Table):
    name        = tables.Column()
    old_value   = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    new_value   = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    difference  = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    percentage  = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    
    class Meta:
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-centered mb-0", "thead": {"class": "thead-light"}}
        orderable = False
    
    def set_column_title(self, _column_name="", _column_new_name="" ):
        self.base_columns[_column_name].verbose_name = _column_new_name 

class ByTermTable(tables.Table):
    name    = tables.Column()
    portfel = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    ration = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    npl     = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    toxic   = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    npl_toxic  = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    weight  = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    rezerv  = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    coating  = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})


    class Meta:
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-striped #table-bordered table-head-custom  table-overall"}
        orderable = False

class BySubjectTable(tables.Table):
    TITLE       = tables.Column()
    LOAN        = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    RATION      = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    NPL_LOAN    = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    TOX_LOAN    = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    TOX_NPL     = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    WEIGHT      = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    RESERVE     = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    COATING     = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})

    class Meta:
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-striped #table-bordered table-head-custom  table-overall"}
        orderable = False

class ByPercentageTable(tables.Table):
    TITLE       = tables.Column()
    ULL_LOAN    = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    ULL_PERCENT = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    ULS_LOAN    = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    ULS_PERCENT = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    FLL_LOAN    = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    FLL_PERCENT = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    FLS_LOAN    = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    FLS_PERCENT = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    
    class Meta:
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-striped #table-bordered table-head-custom  table-overall"}
        orderable = False

class ByPercentageULTable(tables.Table):
    TITLE       = tables.Column()
    T2_LOAN    = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    T2_PERCENT    = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    T5_LOAN    = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    T5_PERCENT    = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    T7_LOAN    = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    T7_PERCENT    = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    T10_LOAN    = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    T10_PERCENT    = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    T11_LOAN    = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    T11_PERCENT    = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    
    class Meta:
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-striped #table-bordered table-head-custom  table-overall"}
        orderable = False

class ByAverageULTable(tables.Table):
    TITLE       = tables.Column()
    UZS_AVERAGE    = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    USD_AVERAGE    = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    EUR_AVERAGE    = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    JPY_AVERAGE    = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    
    class Meta:
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-striped #table-bordered table-head-custom  table-overall"}
        orderable = False

class ByAverageFLTable(tables.Table):
    TITLE       = tables.Column()
    BALANS    = tables.Column(attrs={"th":{"class":"text-right"}, "td":{"class":"text-right"}})
    
    class Meta:
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-striped #table-bordered table-head-custom  table-overall"}
        orderable = False

class ContractListTable(tables.Table):
    class Meta:
        model = ReportData
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-centered mb-0", "thead": {"class": "thead-light"}}
        orderable = True
        fields = (
            'id',
            'NAME_CLIENT', 
            'DATE_DOGOVOR',
            'DATE_POGASH',
            'SUM_DOG_NOM',
            'VALUTE',
            'BRANCH',
            'TYPE_CLIENT',
            )