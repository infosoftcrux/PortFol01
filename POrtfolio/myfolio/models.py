from django.db import models

# Create your models here.
class About (models.Model):
    user_id = models.AutoField
    user_First_name = models.CharField(max_length = 50)
    user_Second_name = models.CharField(max_length = 50)
    user_Title = models.CharField(max_length = 150)
    user_Birthdate = models.DateField()
    user_highest_degree = models.CharField(max_length = 50)
    user_Experience = models.CharField(max_length = 30)
    Titles_you_want_to_show_in_animated_text_and_each_seprate_by_comma = models.CharField(max_length = 1000)
    user_Phone_No = models.CharField(max_length = 10)
    user_Email = models.EmailField(max_length = 254)
    user_Address = models.CharField(max_length = 1200)
    freelancer_status_choice = [('Available','Available'),('Not Available','Not Available'),]
    user_Freelancer_status = models.CharField(max_length = 13, choices = freelancer_status_choice, default = 'Available')
    user_About_Desc = models.CharField(max_length = 20000)
    user_image = models.ImageField(upload_to = 'myfolio/images')
    user_cv_link = models.FileField(upload_to='myfolio/uploads/%Y/%m/%d/',default = '#')

    def __str__(self):
        return self.user_First_name
    

class Skills (models.Model):
    user_Skill_name = models.CharField(max_length = 50)
    user_skill_knows_in_percententage = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.user_Skill_name
    
class Education (models.Model):
    Highest_education_name = models.CharField(max_length = 300)
    Highest_education_year = models.CharField(max_length = 200 )
    Highest_education_college = models.CharField(max_length = 600)
    Highest_education_desc = models.CharField(max_length = 1500)

    lowest_education_name = models.CharField(max_length = 300)
    lowest_education_year = models.CharField(max_length = 200 )
    lowest_education_college = models.CharField(max_length = 600)
    lowest_education_desc = models.CharField(max_length = 1500)

    def __str__(self):
       return self.Highest_education_name
    
class Others_education(models.Model):
    others_education_name = models.CharField(max_length = 300)
    others_education_year = models.CharField(max_length = 200 )
    others_education_college = models.CharField(max_length = 600)
    others_education_desc = models.CharField(max_length = 1500)

    def __str__(self):
        return self.others_education_name
    
class Experience(models.Model) :
    Experience_name = models.CharField(max_length = 300)
    year_duration = models.CharField(max_length = 200 )
    compony= models.CharField(max_length = 600)
    Desc_about_Experience= models.CharField(max_length = 1500)
    
class Projects (models.Model):
    project_name= models.CharField(max_length = 500)
    project_catagory_name = models.CharField(max_length = 150)
    project_description = models.CharField(max_length = 20000)
    project_image = models.ImageField(upload_to = 'myfolio/images/projects')
    project_youTubevideo_link = models.URLField( blank = True ,default = '#')
    
    def __str__(self):
        return self.project_name
    
class Contact (models.Model):
    name = models.CharField(max_length = 200)
    email_Id = models.EmailField(max_length = 254)
    subject = models.CharField(max_length = 200)
    message = models.CharField(max_length = 5000)
    
    def __str__(self):
        return self.name
    
class Social_links (models.Model):
        kaggle_link = models.URLField( blank = True )
        github_link = models.URLField( blank = True )
        linkdin_link = models.URLField( blank = True )
        twitter_link = models.URLField( blank = True )
        facbook_link = models.URLField( blank = True )