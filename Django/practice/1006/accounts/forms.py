from django.contrib.auth.forms import UserCreationForm
# from .models import User
from django.contrib.auth import get_user_model 

class CustomUserCreationform(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ("username", )
# get함수를 호출해라, 직접 참조하지 않도록