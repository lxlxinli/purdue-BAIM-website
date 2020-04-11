from Candidates.models import student
import django_filters
from django import forms 

class experience(django_filters.FilterSet):
    class Meta:
        model = student
        fields = ['analytics_experience','total_professional_experience']

class rolesseeking(django_filters.FilterSet):
    class Meta:
        model = student
        fields = ['data_analyst','business_analyst','data_scientist','consultant','developer']

class location(django_filters.FilterSet):
    class Meta:
        model = student
        fields = ['within_US','international','mid_atlantic','midwest','northeast','pacific_northwest','south','southeast','southwest','west']

# class Certification(django_filters.FilterSet):
#     Certification = django_filters.ModelMultipleChoiceFilter(queryset=certification.objects.all()[1:],widget=forms.CheckboxSelectMultiple)
    
#     class Meta:
#         model = certification
#         fields = ["SAS_base_programmer","SAS_statistical_business_analyst",'Oracle_SQL','NVIDIA_deep_learning_with_NLP','Tableau','INFORM_CAP_aCAP']
