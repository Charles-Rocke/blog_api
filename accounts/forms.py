from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# forms here
# Create a user
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("name",) # attribute of 'CustomUser' model
        
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields
        