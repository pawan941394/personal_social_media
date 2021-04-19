from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, RegexValidator


# Create your models here.
class MYProfile(models.Model):
    name = models.CharField(max_length = 100)
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    age = models.IntegerField(default=18, validators=[MinValueValidator(18)])
    address = models.TextField(max_length=299, null=True,blank=True)
    status = models.CharField(max_length = 20, default="single", choices=(('single','single'), ('married','married'),('widow','widow'),('separated','separated'),('comited','comited')))
    gender = models.CharField(max_length = 20, default="female", choices=(('male','male'), ('female','female')))
    phone_no = models.CharField(validators = [RegexValidator("^0?[5-9]{1}\d{9}")], max_length=15,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    pic = models.ImageField(upload_to = "images\\", null=True)
    def __str__(self):
        return "%s" % self.user

class MYPost(models.Model):
    pic = models.ImageField(upload_to = "images\\", null=True)
    subject = models.CharField(max_length = 100)
    msg = models.TextField(null=True,blank=True)
    cr_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(to=MYProfile, on_delete=CASCADE, null=True)
    def __str__(self):
        return "%s" % self.subject




class PostComment(models.Model):
    post = models.ForeignKey(to=MYPost, on_delete=CASCADE)
    msg = models.TextField()
    commented_by = models.ForeignKey(to=MYProfile, on_delete=CASCADE)
    cr_date = models.DateTimeField(auto_now_add=True)
    flag = models.CharField(max_length = 20, null=True, blank=True ,choices=(('racist','racist'), ('abbusing','abbusing')))


    def __str__(self):
        return "%s" % self.msg
    
    
class PostLike(models.Model):
    post = models.ForeignKey(to=MYPost, on_delete=CASCADE)
    liked_by = models.ForeignKey(to=MYProfile, on_delete=CASCADE)
    cr_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "%s" % self.liked_by
    
    
    
class FollowUser(models.Model):
    profile = models.ForeignKey(to=MYProfile, on_delete=CASCADE, related_name="profile")
    followed_by = models.ForeignKey(to=MYProfile, on_delete=CASCADE ,related_name="followed_by")


    def __str__(self):
        return "%s is followed_by %s" % (self.profile,self.followed_by)
    
    
class contactinfo(models.Model):
    Cname = models.CharField(max_length=35)
    Cemail = models.EmailField(max_length=50)
    Cphone_no = models.CharField(max_length=15)
    Cmassage = models.CharField(max_length=5000)
    def __str__(self):
        return self.Cname


    
    

