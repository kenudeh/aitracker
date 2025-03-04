from enum import Enum


# Enum for Tools type
class CategoryTypeChoices(Enum):
    CODE_GENERATORS = "code_genenerators"
    CODE_ANALYSIS_AND_REVIEW = 'code_analysis_and_review'
    DESIGN_AND_ARCHITECTURE = 'design_and_architecture'
    TESTING_AND_DEBUGGING = "testing_and_debugging"
    DOCUMENTATION = 'documentation'
  
    
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name.replace("_", " ").capitalize()) for key in cls]


#Enum for Pricing 
class PricingTypeChoices(Enum):
    FREE = 'free'
    PAID = 'paid'
    FREEMIUM = 'freemium'
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name.capitalize()) for key in cls ]
    


# Enum for ToolSuggestion
class ToolSubmissionStatusChoices(Enum):
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name.capitalize()) for key in cls ]
    
    
class SubscriptionTypeChoices(Enum):
    BASIC = 'basic'
    PREMIUM = 'premium'
    GOLD = 'gold'
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name.capitalize()) for key in cls ]