from django.contrib.auth.base_user import BaseUserManager
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password) #to encrypt the password before saving it to database
        user.save()
        return user
    def create_superuser(self, email, password=None,**extra_fields):#creating superusers
        extra_fields.setdefault("is_staff", True)#setting is staff as true by default
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)#setting is superuser as true by
        print (extra_fields["is_staff"])
        print ("super")
        user = self.create_user(email, password,**extra_fields)
        return user
    
