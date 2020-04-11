from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
# class Answer(models.IntegerChoices):
#     NO = 0, _("No")    
#     YES = 1, _("Yes")

#     __empty__ = _('')

class student(models.Model):
        
    class Answer(models.IntegerChoices):
        NO = 0, _("No")    
        YES = 1, _("Yes")

        __empty__ = _('')
    
    student_id = models.CharField(max_length = 25,unique=True)
    last_name = models.CharField(max_length = 30)
    first_name = models.CharField(max_length = 50)
    purdue_email = models.CharField(max_length = 120)
    linkedin = models.URLField(default ="")
    hired = models.IntegerField(choices=Answer.choices,default=0)
    picturelink = models.URLField(default ="")
    analytics_experience = models.IntegerField(default =0)
    total_professional_experience = models.IntegerField(default =0)
    #Roles Seeking
    data_analyst = models.IntegerField(choices=Answer.choices, default=0)
    business_analyst = models.IntegerField(choices=Answer.choices, default=0)
    data_scientist = models.IntegerField(choices=Answer.choices, default=0)
    consultant = models.IntegerField(choices=Answer.choices, default=0)
    developer = models.IntegerField(choices=Answer.choices, default=0)
    #Location
    within_US = models.IntegerField(choices=Answer.choices, default=0)
    international = models.IntegerField(choices=Answer.choices, default=0)
    mid_atlantic = models.IntegerField(choices=Answer.choices, default=0)
    midwest = models.IntegerField(choices=Answer.choices, default=0)
    northeast = models.IntegerField(choices=Answer.choices, default=0)
    pacific_northwest = models.IntegerField(choices=Answer.choices, default=0)
    south = models.IntegerField(choices=Answer.choices, default=0)
    southeast = models.IntegerField(choices=Answer.choices, default=0)
    southwest =models.IntegerField(choices=Answer.choices, default=0)
    west = models.IntegerField(choices=Answer.choices, default=0)
    #Industry 
    automotive = models.IntegerField(choices=Answer.choices, default=0)
    consulting = models.IntegerField(choices=Answer.choices, default=0)
    consumer_products = models.IntegerField(choices=Answer.choices, default=0)
    energy = models.IntegerField(choices=Answer.choices, default=0)
    entertainment = models.IntegerField(choices=Answer.choices, default=0)
    financial_services = models.IntegerField(choices=Answer.choices, default=0)
    healthcare = models.IntegerField(choices=Answer.choices, default=0)
    manufacturing = models.IntegerField(choices=Answer.choices, default=0)
    non_profit = models.IntegerField(choices=Answer.choices, default=0)
    retail = models.IntegerField(choices=Answer.choices, default=0)
    sports = models.IntegerField(choices=Answer.choices, default=0)
    technology = models.IntegerField(choices=Answer.choices, default=0)
    other = models.IntegerField(choices=Answer.choices, default=0)
    #Skills 
    r = models.IntegerField(choices=Answer.choices, default=0)
    python = models.IntegerField(choices=Answer.choices, default=0)
    sas = models.IntegerField(choices=Answer.choices, default=0)
    sql = models.IntegerField(choices=Answer.choices, default=0)
    plsql_tsql = models.IntegerField(choices=Answer.choices, default=0)
    hive = models.IntegerField(choices=Answer.choices, default=0)
    tableau = models.IntegerField(choices=Answer.choices, default=0)
    powerbi = models.IntegerField(choices=Answer.choices, default=0)
    sasEM = models.IntegerField(choices=Answer.choices, default=0)
    vba = models.IntegerField(choices=Answer.choices, default=0)
    excel = models.IntegerField(choices=Answer.choices, default=0)
    nosql = models.IntegerField(choices=Answer.choices, default=0)
    django = models.IntegerField(choices=Answer.choices, default=0)
    gurobi = models.IntegerField(choices=Answer.choices, default=0)
    cplex = models.IntegerField(choices=Answer.choices, default=0)
    spark = models.IntegerField(choices=Answer.choices, default=0)
    julia = models.IntegerField(choices=Answer.choices, default=0)
    c = models.IntegerField(choices=Answer.choices, default=0)
    java = models.IntegerField(choices=Answer.choices, default=0)
    azure = models.IntegerField(choices=Answer.choices, default=0)
    git = models.IntegerField(choices=Answer.choices, default=0)
    ms_project = models.IntegerField(choices=Answer.choices, default=0)
    aws = models.IntegerField(choices=Answer.choices, default=0)
    google_cloud = models.IntegerField(choices=Answer.choices, default=0)
    #Certification
    SAS_base_programmer = models.IntegerField(choices=Answer.choices, default=0)
    SAS_statistical_business_analyst =models.IntegerField(choices=Answer.choices, default=0)
    Oracle_SQL = models.IntegerField(choices=Answer.choices, default=0)
    NVIDIA_deep_learning_with_NLP =models.IntegerField(choices=Answer.choices, default=0)
    Tableaucertification =models.IntegerField(choices=Answer.choices, default=0)
    INFORM_CAP_aCAP = models.IntegerField(choices=Answer.choices, default=0)

    def __str__(self):
        return self.student_id
