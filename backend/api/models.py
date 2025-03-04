from django.db import models
from utils import *
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone




# Create your models here.
class UserProfile(AbstractUser):
    submissions = models.ManyToManyField('Tool', related_name='submitted_by', blank=True) # Users can submit multiple tools
    
    def __str__(self):
        return self.username
    
    
    
class Bookmark(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    tool = models.ForeignKey('Tool', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user
  
  
  
class Category(models.Model):
    name = models.CharField(
        max_length=20,
        unique=True,
        choices=CategoryTypeChoices.choices()
    )
    
    def __str__(self):
        return self.name
    
    
    
class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
      
    def __str__(self):
        return self.name
     


class Tool(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    website = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    pricing = models.CharField(
        max_length=20,
        choices=PricingTypeChoices.choices()
    )
    tags = models.ManyToManyField(Tag, related_name="tools")
    strengths = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    weaknesses = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    is_featured = models.BooleanField(default=False)  # Tracks featured status
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"name: {self.name} - type: {self.category}"
    
    
    

class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    ratings = models.PositiveSmallIntegerField(
        choices=[(i, i) for i in range(1, 6)]
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.user} - {self.tool.name}"
    



class ToolSuggestion(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # User suggesting the tool
    tool_name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    website = models.URLField()
    category = models.ForeignKey(
        Category, 
        choices=CategoryTypeChoices.choices(), 
        on_delete=models.CASCADE
    )
    pricing = models.CharField(
        max_length=20,
        choices= PricingTypeChoices.choices()
    )
    status = models.CharField(
        max_length=20,
        choices=ToolSubmissionStatusChoices.choices(),
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"user: {self.user} - name: {self.tool_name} - status: {self.status}"
    
    
class Subscription(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    plan = models.CharField(
        max_length = 20,
        choices = SubscriptionTypeChoices
    )
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    
    
    def is_active(self):
        if self.end_date is None or self.end_date > timezone.now():
            self.tool.is_featured = True  #Mark tool as featured
            self.tool.save()
            return True
        self.tool.is_featured = False # Unmark tool when subscription expires
        self.tool.save()
        return False