from django.shortcuts import render
from Candidates.models import student
from Candidates.forms import CandidatePreferencesForm
import re,math,copy
# from Candidates.filters import rolesseeking,location,Certification

# Create your views here.
def browsecandidates(request):
    #loading form and student list
    if request.GET != {} :
        dic = copy.deepcopy(request.GET)
        del dic['id_analytics_experience']
        del dic['id_professional_experience']

        id_list = []
        for k in dic: 
            id_list.append(k)

        form = CandidatePreferencesForm(request.GET)
        student_list = student.objects.all()
        #Experience Range Query
        analyst_exp_range = request.GET.get('id_analytics_experience')
        professional_exp_range = request.GET.get('id_professional_experience')
        
        #Roles Query
        data_analyst_query = request.GET.get('id_roles_0')
        business_analyst_query = request.GET.get('id_roles_1')
        data_scientist_query = request.GET.get('id_roles_2')
        consultant_query = request.GET.get('id_roles_3')
        developer_query = request.GET.get('id_roles_4')

        #Location Query
        within_US_query = request.GET.get('id_location_0')
        international_query = request.GET.get('id_location_1')
        mid_atlantic_query = request.GET.get('id_location_2')
        midwest_query = request.GET.get('id_location_3')
        northeast_query = request.GET.get('id_location_4')
        pacific_northwest_query = request.GET.get('id_location_5')
        south_query = request.GET.get('id_location_6')
        southeast_query = request.GET.get('id_location_7')
        southwest_query = request.GET.get('id_location_8')
        west_query = request.GET.get('id_location_9')

        #Industry Query
        automotive_query = request.GET.get('id_industry_0')
        consulting_query = request.GET.get('id_industry_1')
        consumer_products_query = request.GET.get('id_industry_2')
        energy_query = request.GET.get('id_industry_3')
        entertainment_query = request.GET.get('id_industry_4')
        financial_services_query = request.GET.get('id_industry_5')
        healthcare_query = request.GET.get('id_industry_6')
        manufacturing_query = request.GET.get('id_industry_7')
        non_profit_query = request.GET.get('id_industry_8')
        retail_query = request.GET.get('id_industry_9')
        sports_query = request.GET.get('id_industry_10')
        technology_query = request.GET.get('id_industry_11')
        other_query = request.GET.get('id_industry_12')

        #Skills Query
        r_query = request.GET.get('id_skills_0')
        python_query = request.GET.get('id_skills_1')
        sas_query = request.GET.get('id_skills_2')
        sql_query = request.GET.get('id_skills_3')
        plsqp_tsql_query = request.GET.get('id_skills_4')
        hive_query = request.GET.get('id_skills_5')
        tableau_query = request.GET.get('id_skills_6')
        powerbi_query = request.GET.get('id_skills_7')
        sasEM_query = request.GET.get('id_skills_8')
        vba_query = request.GET.get('id_skills_9')
        excel_query = request.GET.get('id_skills_10')
        nosql_query = request.GET.get('id_skills_11')
        django_query = request.GET.get('id_skills_12')
        gurobi_query = request.GET.get('id_skills_13')
        cplex_query = request.GET.get('id_skills_14')
        spark_query = request.GET.get('id_skills_15')
        julia_query = request.GET.get('id_skills_16')
        c_query = request.GET.get('id_skills_17')
        java_query = request.GET.get('id_skills_18')
        azure_query = request.GET.get('id_skills_19')
        git_query = request.GET.get('id_skills_20')
        ms_project_query = request.GET.get('id_skills_21')
        aws_query = request.GET.get('id_skills_22')
        google_cloud_query = request.GET.get('id_skills_23')

        #Certification Query
        SAS_base_programmer_query = request.GET.get('id_certification_0')
        SAS_statistical_business_analyst_query = request.GET.get('id_certification_1')
        Oracle_SQL_query = request.GET.get('id_certification_2')
        NVIDIA_deep_learning_with_NLP_query = request.GET.get('id_certification_3')
        Tableaucertification_query = request.GET.get('id_certification_4')
        INFORM_CAP_aCAP_query = request.GET.get('id_certification_5')

        #Filtering based on queries  #4/6 - consider using list and for loops 
        #Experience Ranges
        value = re.compile(r'(\d{1,2});(\d{1,3})') #Regex to find min and max value

        #Analyst
        if analyst_exp_range is not None:
            ana = value.search(analyst_exp_range)
            ana_minvalue = int(ana.group(1))
            ana_maxvalue = int(ana.group(2))
            student_list = student_list.filter(analytics_experience__lte=ana_maxvalue)
            student_list = student_list.filter(analytics_experience__gte=ana_minvalue)
            

        #Professional
        if analyst_exp_range is not None:
            prof = value.search(professional_exp_range)
            prof_minvalue = int(prof.group(1))
            prof_maxvalue = int(prof.group(2))
            student_list = student_list.filter(total_professional_experience__lte=prof_maxvalue)
            student_list = student_list.filter(total_professional_experience__gte=prof_minvalue)

        #Roles
        if data_analyst_query == 'on':
            student_list = student_list.filter(data_analyst=1) #Check if should be 1 or "yes"
        if business_analyst_query == 'on':
            student_list = student_list.filter(business_analyst=1)
        if data_scientist_query == 'on':
            student_list = student_list.filter(data_scientist=1)
        if consultant_query == 'on':
            student_list = student_list.filter(consultant=1)
        if developer_query == 'on':
            student_list = student_list.filter(developer=1)

        #Location
        if within_US_query == 'on':
            student_list = student_list.filter(within_US=1)
        if international_query == 'on':
            student_list = student_list.filter(international=1)
        if mid_atlantic_query == 'on':
            student_list = student_list.filter(mid_atlantic=1)
        if midwest_query == 'on':
            student_list = student_list.filter(midwest=1)
        if northeast_query == 'on':
            student_list = student_list.filter(northeast=1)
        if pacific_northwest_query == 'on':
            student_list = student_list.filter(pacific_northwest=1)
        if south_query == 'on':
            student_list = student_list.filter(south=1)
        if southeast_query == 'on':
            student_list = student_list.filter(southeast=1)
        if southwest_query == 'on':
            student_list = student_list.filter(southwest=1)
        if west_query == 'on':
            student_list = student_list.filter(west=1)

        #Industry
        if automotive_query == 'on':
            student_list = student_list.filter(automotive=1)
        if consulting_query == 'on':
            student_list = student_list.filter(consulting=1)
        if consumer_products_query == 'on':
            student_list = student_list.filter(consumer_products=1)
        if energy_query == 'on':
            student_list = student_list.filter(energy=1)
        if entertainment_query == 'on':
            student_list = student_list.filter(entertainment=1)
        if financial_services_query == 'on':
            student_list = student_list.filter(financial_services=1)
        if healthcare_query == 'on':
            student_list = student_list.filter(healthcare=1)
        if manufacturing_query == 'on':
            student_list = student_list.filter(manufacturing=1)
        if non_profit_query == 'on':
            student_list = student_list.filter(non_profit_query=1)
        if retail_query == 'on':
            student_list = student_list.filter(retail=1)                                                                
        if sports_query == 'on':
            student_list = student_list.filter(sports=1)   
        if technology_query == 'on':
            student_list = student_list.filter(technology=1)   
        if other_query == 'on':
            student_list = student_list.filter(other=1)                   
        #Skills
        if r_query == 'on':
            student_list = student_list.filter(r=1)
        if python_query == 'on':
            student_list = student_list.filter(python=1)
        if sas_query == 'on':
            student_list = student_list.filter(sas=1)
        if sql_query == 'on':
            student_list = student_list.filter(sql=1)
        if plsqp_tsql_query == 'on':
            student_list = student_list.filter(plsql_tsql=1)
        if hive_query == 'on':
            student_list = student_list.filter(hive=1)
        if tableau_query == 'on':
            student_list = student_list.filter(tableau=1)
        if powerbi_query == 'on':
            student_list = student_list.filter(powerbi=1)
        if sasEM_query == 'on':
            student_list = student_list.filter(sasEM=1)
        if vba_query == 'on':
            student_list = student_list.filter(vba=1)
        if excel_query == 'on':
            student_list = student_list.filter(excel=1)
        if nosql_query == 'on':
            student_list = student_list.filter(nosql=1)
        if django_query == 'on':
            student_list = student_list.filter(django=1)
        if gurobi_query == 'on':
            student_list = student_list.filter(gurobi=1)
        if cplex_query == 'on':
            student_list = student_list.filter(cplex=1)
        if spark_query == 'on':
            student_list = student_list.filter(spark=1)
        if julia_query == 'on':
            student_list = student_list.filter(julia=1)
        if c_query == 'on':
            student_list = student_list.filter(c=1)
        if java_query == 'on':
            student_list = student_list.filter(java=1)
        if azure_query == 'on':
            student_list = student_list.filter(azure=1)
        if git_query == 'on':
            student_list = student_list.filter(git=1)
        if ms_project_query == 'on':
            student_list = student_list.filter(ms_project=1)
        if aws_query == 'on':
            student_list = student_list.filter(aws=1)
        if google_cloud_query == 'on':
            student_list = student_list.filter(google_cloud=1)

        #Certification
        if SAS_base_programmer_query == 'on':
            student_list = student_list.filter(SAS_base_programmer=1) 
        if SAS_statistical_business_analyst_query == 'on':
            student_list = student_list.filter(SAS_statistical_business_analyst=1) 
        if Oracle_SQL_query == 'on':
            student_list = student_list.filter(Oracle_SQL=1) 
        if NVIDIA_deep_learning_with_NLP_query == 'on':
            student_list = student_list.filter(NVIDIA_deep_learning_with_NLP=1) 
        if Tableaucertification_query == 'on':
            student_list = student_list.filter(Tableaucertification=1) 
        if INFORM_CAP_aCAP_query == 'on':
            student_list = student_list.filter(INFORM_CAP_aCAP=1) 

        args ={'form':form,'studentlist':student_list, 'ana_minvalue':ana_minvalue, 
        'ana_maxvalue':ana_maxvalue, 'prof_minvalue':prof_minvalue, 'prof_maxvalue':prof_maxvalue,"id_list":id_list}

        return render(request, 'candidates/browse.html',args)

    else:
        form = CandidatePreferencesForm
        student_list = student.objects.all()
        ana_minvalue=0
        ana_maxvalue=60
        prof_minvalue=0
        prof_maxvalue=120
        id_list = []

        args ={'form':form,'studentlist':student_list, 'ana_minvalue':ana_minvalue, 
        'ana_maxvalue':ana_maxvalue, 'prof_minvalue':prof_minvalue, 'prof_maxvalue':prof_maxvalue, "id_list":id_list}
        return render(request, 'candidates/browse.html',args)

def achievements(request):
    list = ['1','2','3','4','5','6']
    words = ['Apples','Orange','Pear']
    args={'list':list,'words':words}
    return render(request, 'candidates/achievements.html',args)

def programdetails(request):
    args={}
    return render(request, 'candidates/programdetails.html',args)












# Code For testing things only
def browse(request):
#     student_list = student.objects.all() #add order by last name
#     # certification_list = certification.objects.all()[1:]
#     rolesfilter = rolesseeking(request.GET, queryset=student_list)
#     locationfilter = location(request.GET,queryset=student_list)
#     certificationfilter = Certification(request.GET,queryset=certification_list)
    form = CandidatePreferencesForm(request.GET)
    student_list = student.objects.all()
    data_analyst_query = request.GET.get('id_roles_0')
    business_analyst_query = request.GET.get('id_roles_1')
    data_scientist_query = request.GET.get('id_roles_2')
    consultant_query = request.GET.get('id_roles_3')
    developer_query = request.GET.get('id_roles_4')
    analyst_exp_range = request.GET.get('id_analytics_experience')
    professional_exp_range = request.GET.get('id_professional_experience')

    ana_minvalue=0
    ana_maxvalue=60
    prof_minvalue=0
    prof_maxvalue=120

    #Filtering based on queries  #4/6 - consider using list and for loops 
    #Experience Ranges
    value = re.compile(r'(\d{1,2});(\d{1,3})') #Regex to find min and max value

    #Analyst
    if analyst_exp_range is not None:
        ana = value.search(analyst_exp_range)
        ana_minvalue = int(ana.group(1))
        ana_maxvalue = int(ana.group(2))
        student_list = student_list.filter(analytics_experience__lte=ana_maxvalue)
        student_list = student_list.filter(analytics_experience__gte=ana_minvalue)
        

    #Professional
    if analyst_exp_range is not None:
        prof = value.search(professional_exp_range)
        prof_minvalue = int(prof.group(1))
        prof_maxvalue = int(prof.group(2))
        student_list = student_list.filter(total_professional_experience__lte=prof_maxvalue)
        student_list = student_list.filter(total_professional_experience__gte=prof_minvalue)



    if data_analyst_query == 'on':
        student_list = student_list.filter(data_analyst=1) 
    
    if business_analyst_query == 'on':
        student_list = student_list.filter(business_analyst=1)

    if data_scientist_query == 'on':
        student_list = student_list.filter(data_scientist=1)

    if consultant_query == 'on':
        student_list = student_list.filter(consultant=1)

    if developer_query == 'on':
        student_list = student_list.filter(developer=1)

    args ={'form':form,'studentlist':student_list, 'ana_minvalue':ana_minvalue, 
        'ana_maxvalue':ana_maxvalue, 'prof_minvalue':prof_minvalue, 'prof_maxvalue':prof_maxvalue  }

    return render(request,'candidates/browsecandidates.html',args)