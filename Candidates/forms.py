from django import forms

ROLES_CHOICES =[
    ('data_analyst','Data Analyst'),
    ('business_analyst','Business Analyst'),
    ('data_scientist','Data Scientist'),
    ('consultant','Consultant'),
    ('developer','Developer')
]

LOCATION_CHOICES =[
    ('within_US','Within USA'),
    ('internation','International'),
    ('mid_atlantic','Mid Atlantic'),
    ('midwest','Midwest'),
    ('northeast','Northeast'),
    ('pacific_northwest','Pacific Northwest'),
    ('south','South'),
    ('southeast','Southeast'),
    ('southwest','Southwest'),
    ('west','West'),
]

INDUSTRY_CHOICES =[
    ('automotive','Automotive'),
    ('consulting','Consulting'),
    ('consumer_products','Consumer Products'),
    ('energy','Energy'),
    ('entertainment','Entertainment'),
    ('financial_services','Financial Services'),
    ('healthcare','Healthcare'),
    ('manufacturing','Manufacturing'),
    ('non-profit','Non-For-Profit'),
    ('retail','Retail'),
    ('sports','Sports'),
    ('technology','Technology'),
    ('other','Other'),
]

SKILLS_CHOICES=[
    ('r','R'),
    ('python','Python'),
    ('sas','SAS'),
    ('sql','SQL'),
    ('plsql_tsql','PLSQL/TSQL'),
    ('hive','HIVE'),
    ('tableau','Tableau'),
    ('powerbi','PowerBI'),
    ('sasEM','SAS EM'),
    ('vba','VBA'),
    ('excel','Excel'),
    ('nosql','NoSQL'),
    ('django','Django'),
    ('gurobi','Gurobi'),
    ('cplex','CPLEX'),
    ('spark','Spark'),
    ('julia','Julia'),
    ('c','C/C++'),
    ('java','Java'),
    ('azure','Azure'),
    ('git','Git'),
    ('ms_project','MS Project'),
    ('aws','AWS'),
    ('google_cloud','Google Cloud'),
]

CERTIFICATION_CHOICES =[
    ('SAS_base_programmer','SAS Base Programmer'),
    ('SAS_statistical_business_analyst','SAS Statistical Business Analyst'),
    ('Oracle_SQL','Oracle SQL'),
    ('NVIDIA_deep_learning_with_NLP','NVIDIA deep learning with NLP'),
    ('Tableaucertification','Tableau'),
    ('INFORM_CAP_aCAP','INFORM CAP/aCAP'),
]

class CandidatePreferencesForm(forms.Form):
    keyword = forms.CharField(required=False)
    analytics_experience = forms.CharField(required=False, initial='0;60')
    professional_experience = forms.CharField(required=False, initial='0;120')
    roles = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple,choices=ROLES_CHOICES)
    location = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple,choices=LOCATION_CHOICES)
    industry = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple,choices=INDUSTRY_CHOICES)
    skills = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple,choices=SKILLS_CHOICES)
    certification = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple,choices=CERTIFICATION_CHOICES)
