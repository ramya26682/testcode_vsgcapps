from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser 
from django.utils.translation import gettext_lazy
from django.core.validators import MaxValueValidator
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Applicant_details(models.Model):
    App_FirstName=models.CharField(max_length=128)
    App_MiddleName=models.CharField(max_length=128,blank=True)
    App_LastName=models.CharField(max_length=128,blank=True)
    dob = models.DateField(max_length=10,blank=True,null=True)
    place_of_birth=models.CharField(max_length=128,blank=True)
    citizen=[
             ('US citizen','US citizen'),
             ('Permanent Resident','Permanent Resident'),
             ('Student Visa','Student Visa')
         ]
    Citizenship=models.CharField(max_length=50,choices=citizen,default="US citizen",null=True,blank=True)
    Describe_type_and_status_if_visa_option_is_checked=models.CharField(max_length=264,default="",blank=True)
    visa_expiration=models.DateField(max_length=10,blank=True,null=True)
    gender=[
             ('Male','Male'),
             ('Female','Female'),
             ('Other','Other')
         ]

    Gender=models.CharField(max_length=100,choices=gender,default="Male",blank=True)
    Ethnicity=models.CharField(max_length=256,blank=True)
    Mailing_Address=models.CharField(max_length=256,blank=True)
    Mailing_City=models.CharField(max_length=128,blank=True)
    Mailing_State=models.CharField(max_length=128,blank=True)
    Mailing_Zip_Code=models.CharField(max_length=128,blank=True)
    Current_phone=models.CharField(max_length=13,blank=True)
    Permanent_Home_Address=models.CharField(max_length=256,blank=True)
    Permanent_City=models.CharField(max_length=128,blank=True)
    Permanent_State=models.CharField(max_length=128,blank=True)
    Permanent_Zip_Code=models.CharField(max_length=128,blank=True)
    Permanent_Home_phone=models.CharField(max_length=13,blank=True)
    Email= models.EmailField(max_length=254,blank=True)
    clg_or_univ_Enrolled=models.CharField(max_length=128,blank=True)
    Major_Field=models.CharField(max_length=128,blank=True)
    Degree=[
             ("Master's","Master's"),
             ("Doctorate","Doctorate")
         ]
    Degree_objective=models.CharField(max_length=128,blank=True,choices=Degree,default="")
    Expected_Graduation=models.DateField(max_length=20,blank=True,null=True)
    Ref1_Name=models.CharField(max_length=128,blank=True)
    Ref1_Title=models.CharField(max_length=128,blank=True)
    Ref1_Dept=models.CharField(max_length=128,blank=True)
    Ref1_Inst=models.CharField(max_length=128,blank=True)
    Ref1_Phone=models.CharField(max_length=70,blank=True)
    Ref2_Name=models.CharField(max_length=128,blank=True)
    Ref2_Title=models.CharField(max_length=128,blank=True)
    Ref2_Dept=models.CharField(max_length=128,blank=True)
    Ref2_Inst=models.CharField(max_length=128,blank=True)
    Ref2_Phone=models.CharField(blank=True,max_length=128)
    clg_or_univ_1=models.CharField(max_length=128,blank=True)
    Location_1=models.CharField(max_length=128,blank=True)
    Major_1=models.CharField(max_length=128,blank=True)
    Dates_Attended_1=models.CharField(max_length=128,blank=True,null=True)
    GPA_1=models.CharField(max_length=128,blank=True)
    Degree_1=models.CharField(max_length=128,blank=True)
    degree_expected_1=models.CharField(max_length=128,blank=True,null=True)
    clg_or_univ_2=models.CharField(max_length=128,blank=True)
    Location_2=models.CharField(max_length=128,blank=True)
    Major_2=models.CharField(max_length=128,blank=True)
    Dates_Attended_2=models.CharField(max_length=128,blank=True,null=True)
    GPA_2=models.CharField(max_length=128,blank=True)
    Degree_2=models.CharField(max_length=128,blank=True)
    degree_expected_2=models.CharField(max_length=128,blank=True,null=True)
    clg_or_univ_3=models.CharField(max_length=128,blank=True)
    Location_3=models.CharField(max_length=128,blank=True)
    Major_3=models.CharField(max_length=128,blank=True)
    Dates_Attended_3=models.CharField(max_length=10,blank=True,null=True)
    GPA_3=models.CharField(max_length=128,blank=True)
    Degree_3=models.CharField(max_length=128,blank=True)
    degree_expected_3=models.CharField(max_length=128,blank=True,null=True)
    clg_or_univ_4=models.CharField(max_length=128,blank=True)
    Location_4=models.CharField(max_length=128,blank=True)
    Major_4=models.CharField(max_length=128,blank=True)
    Dates_Attended_4=models.CharField(max_length=128,blank=True,null=True)
    GPA_4=models.CharField(max_length=128,blank=True)
    Degree_4=models.CharField(max_length=128,blank=True)
    degree_expected_4=models.CharField(max_length=128,blank=True,null=True)
    clg_or_univ_5=models.CharField(max_length=128,blank=True)
    Location_5=models.CharField(max_length=128,blank=True)
    Major_5=models.CharField(max_length=128,blank=True)
    Dates_Attended_5=models.CharField(max_length=128,blank=True,null=True)
    GPA_5=models.CharField(max_length=128,blank=True)
    Degree_5=models.CharField(max_length=128,blank=True)
    degree_expected_5=models.CharField(max_length=128,blank=True,null=True)
    clg_or_univ_6=models.CharField(max_length=128,blank=True)
    Location_6=models.CharField(max_length=128,blank=True)
    Major_6=models.CharField(max_length=128,blank=True)
    Dates_Attended_6=models.CharField(max_length=128,blank=True,null=True)
    GPA_6=models.CharField(max_length=128,blank=True)
    Degree_6=models.CharField(max_length=128,blank=True)
    degree_expected_6=models.CharField(max_length=128,blank=True,null=True)
    clg_or_univ_7=models.CharField(max_length=128,blank=True)
    Location_7=models.CharField(max_length=128,blank=True)
    Major_7=models.CharField(max_length=128,blank=True)
    Dates_Attended_7=models.CharField(max_length=10,blank=True,null=True)
    GPA_7=models.CharField(max_length=128,blank=True)
    Degree_7=models.CharField(max_length=128,blank=True)
    degree_expected_7=models.CharField(max_length=10,blank=True,null=True)
    Interruptions_of_schooling=models.CharField(max_length=264,default="",blank=True)
    Emp1_Name=models.CharField(max_length=128,blank=True)
    Emp1_Location=models.CharField(max_length=128,blank=True)
    Emp1_Dates=models.CharField(max_length=128,blank=True)
    Emp1_Nature_of_work=models.CharField(max_length=128,blank=True)
    Emp2_Name=models.CharField(max_length=128,blank=True)
    Emp2_Location=models.CharField(max_length=128,blank=True)
    Emp2_Dates=models.CharField(max_length=128,blank=True)
    Emp2_Nature_of_work=models.CharField(max_length=128,blank=True)
    Emp3_Name=models.CharField(max_length=128,blank=True)
    Emp3_Location=models.CharField(max_length=128,blank=True)
    Emp3_Dates=models.CharField(max_length=128,blank=True)
    Emp3_Nature_of_work=models.CharField(max_length=128,blank=True)
    Emp4_Name=models.CharField(max_length=128,blank=True)
    Emp4_Location=models.CharField(max_length=128,blank=True)
    Emp4_Dates=models.CharField(max_length=128,blank=True)
    Emp4_Nature_of_work=models.CharField(max_length=128,blank=True)
    Prof_exp_Notes=models.CharField(max_length=128,blank=True)
    Award1_Name=models.CharField(max_length=128,blank=True)
    Award1_Date=models.CharField(max_length=128,blank=True)
    Award1_Description=models.CharField(max_length=128,blank=True)
    Award2_Name=models.CharField(max_length=128,blank=True)
    Award2_Date=models.CharField(max_length=128,blank=True)
    Award2_Description=models.CharField(max_length=128,blank=True)
    Award3_Name=models.CharField(max_length=128,blank=True)
    Award3_Date=models.CharField(max_length=128,blank=True)
    Award3_Description=models.CharField(max_length=128,blank=True)
    Award4_Name=models.CharField(max_length=128,blank=True)
    Award4_Date=models.CharField(max_length=128,blank=True)
    Award4_Description=models.CharField(max_length=128,blank=True)
    Award5_Name=models.CharField(max_length=128,blank=True)
    Award5_Date=models.CharField(max_length=128,blank=True)
    Award5_Description=models.CharField(max_length=128,blank=True)
    Award6_Name=models.CharField(max_length=128,blank=True)
    Award6_Date=models.CharField(max_length=128,blank=True)
    Award6_Description=models.CharField(max_length=128,blank=True)
    Awards_Notes=models.CharField(max_length=128,blank=True)
    Carrer_goals=models.TextField(max_length=512,blank=True)
    Title_of_reserach_project=models.CharField(max_length=128,blank=True)
    Ref3_Name=models.CharField(max_length=128,blank=True)
    Ref3_Title=models.CharField(max_length=128,blank=True)
    Ref3_Inst=models.CharField(max_length=128,blank=True)
    Ref3_Phone=models.CharField(max_length=128,blank=True)
    Upload=models.FileField(max_length=256,upload_to='media/upload',null=True)


    RADIOS = [
    ('Evaluation Saved','Save for later submission'),
    ('Evaluation Completed','Final submission'),
    ('Approved','Application Approved'),
    ('Rejected','Application Rejected'),
    ]
    stat=models.CharField(
         max_length=25,
         choices=RADIOS,
         default="",
    )
    cheque_no = models.CharField(max_length=9,unique=True)
    # cheque_no = models.CharField(validators=[RegexValidator(regex='^.{9}$', message='Length has to be 9 numbers', code='nomatch')],max_length=128,unique=True)


class Faculty_details(models.Model):
    Applicant_details = models.ForeignKey('Applicant_details', on_delete=models.DO_NOTHING)
    Ref1_Email=models.EmailField(max_length=70,blank=True)
    Ref2_Email=models.EmailField(max_length=70,blank=True)
    Ref3_Email=models.CharField(max_length=128,blank=True)


class Recommendation_fields_details(models.Model):
    Applicant_details = models.ForeignKey('Applicant_details', on_delete=models.DO_NOTHING)
    In_what_capacity_do_you_know_the_applicant=models.CharField(max_length=256)
    How_Long_have_you_known_the_applicant=models.CharField(max_length=128)
    major_field=[
             ('Below Average','Below Average'),
             ('Average','Average'),
             ('Above Average','Above Average'),
             ('Outstanding','Outstanding'),

         ]

    Knowledge_of_major_field=models.CharField(max_length=100,choices=major_field,default="")
    Research_skills=models.CharField(max_length=100,choices=major_field,default="")
    Problem_solving_skills=models.CharField(max_length=100,choices=major_field,default="")
    Creativity=models.CharField(max_length=100,choices=major_field,default="")
    Leadership=models.CharField(max_length=100,choices=major_field,default="")
    Written_communication=models.CharField(max_length=100,choices=major_field,default="")
    Oral_communication=models.CharField(max_length=100,choices=major_field,default="")
    Comment_on_the_ability_of_the_applicant=models.CharField(max_length=512)
    Add_other_comments_to_the_evaluation=models.CharField(max_length=256,blank=True)
    Signed_letter_of_reference=models.FileField(max_length=256,upload_to='media/upload',blank=True)
    faculty_num=models.CharField(max_length=10)


class FacultyAdvisor_fields(models.Model):
    Applicant_details = models.ForeignKey('Applicant_details', on_delete=models.DO_NOTHING)
    proposed = [
    ('Yes','Yes'),
    ('No','No'),
    ]
    Have_you_examined_the_applicant_proposed_researchplan = models.CharField(
         max_length=25,
         choices=proposed,
         default="",
    )
    Do_you_consider_the_applicant_research_plan_reasonable=models.CharField(
         max_length=25,
         choices=proposed,
    )
    If_no_please_comment_1=models.CharField(max_length=128,blank=True)
    Research_within_the_time_frame_indicated=models.CharField(
         max_length=25,
         choices=proposed,
         default="",
    )
    If_no_please_comment_2=models.CharField(max_length=128,blank=True)
    Will_the_applicant_receive_academic_credit_this_work = models.CharField(
         max_length=25,
         choices=proposed,
         default="",
    )
    If_yes_please_indicate_the_nature_of_this_academic_credit=models.CharField(max_length=128,blank=True)
    Work_of_the_applicant_on_this_project= models.CharField(max_length=256,blank=True)
    Applicant_receives_this_research_award = models.CharField(
         max_length=25,
         choices=proposed,
         default="",
    )

    Upload_your_reference_commitment_letter_signed = models.FileField(max_length=256,upload_to='media/upload',blank=True)
    faculty_num=models.CharField(max_length=10,default="")

class user_profile_details(models.Model):
    eval_id=models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name='polls')
    Applicant_details = models.ForeignKey('Applicant_details', on_delete=models.DO_NOTHING)
    RANKING = [
    ('5','5 – Outstanding'),
    ('4.5','4.5'),
    ('4','4 – Very Good'),
    ('3.5','3.5'),
    ('3','3 – Good'),
    ('2.5','2.5'),
    ('2','2 – Poor'),
    ('1.5','1.5'),
    ('1','1 – Not worthy of funding')

    ]
    ranking=models.CharField(
         max_length=25,
         choices=RANKING,default="0",
    )
    RADIOS = [
    ('Evaluation Saved','Save for later submission'),
    ('Evaluation Completed','Final submission'),

    ]
    stat=models.CharField(
         max_length=25,
         choices=RADIOS,
    )


