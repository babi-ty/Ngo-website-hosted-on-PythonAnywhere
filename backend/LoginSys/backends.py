from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

class EmailOrUsernameBackend(ModelBackend):
    """
    This is a custom authentication backend. 
    It allows users to log in with either their username or their email address.
    """
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        Overrides the authenticate method to allow login with email or username.
        """
        # The 'username' variable passed in parameter can be email or username
        if username is None:
            username = kwargs.get(User.USERNAME_FIELD)
            
        try:
            # Try to find a user matching either the username or email (case-insensitive)
            user = User.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
            
        except User.DoesNotExist:
            # No user found with that username or email
            return None
        
        except User.MultipleObjectsReturned:
            # This is rare, but could happen if two users have the same
            # case-insensitive username or email. We'll just fail.
            return None

        # Check the password and if the user is active
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        
        # Password was wrong
        return None

    def get_user(self, user_id):
        """
        Overrides the get_user method to allow Django to retrieve the user
        object for the session.
        """
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
            
        return user if self.user_can_authenticate(user) else None