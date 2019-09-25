from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        email_match = User.objects.filter(email = postData['email'])
        if len(postData['email']) == 0:
            errors['email_blank'] = 'Please enter your email.'
        elif len(email_match) > 0:
            errors['email_invalid'] = 'That email exists in the database already.'
        if len(postData['firstname']) == 0:
            errors['first_name_blank'] = 'The first name field cannot be blank.'
        elif len(postData['firstname']) < 2:
            errors['first_name_short'] = 'The first name field must be at least 2 characters.'
        elif postData['firstname'].isalpha() == False:
            errors['first_name_alpha'] = 'The first name field must contain only letters.'
        if len(postData['lastname']) == 0:
            errors['last_name_blank'] = 'The last name field cannot be blank.'
        elif len(postData['lastname']) < 3:
            errors['last_name_short'] = 'The last name field must be at least 2 characters.'
        elif postData['lastname'].isalpha() == False:
            errors['last_name_alpha'] = 'The last name field must contain only letters.'
        if len(postData['password']) == 0:
            errors['pword_blank'] = 'The password field cannot be blank.'
        elif len(postData['password']) < 8:
            errors['pword_short'] = 'The password field must be at least eight characters.'
        if (postData['password'] != postData['passwordconfirm']):
            errors['pword_match_fail'] = 'Passwords do not match.'
        return errors

    def login_validator(self,postData):
        errors={}
        user_to_login = User.objects.filter(email = postData['loginEmail'])
        if len(user_to_login) == 0:
            errors['invalid'] = "Invalid login credentials."
        else:
            user_to_login = User.objects.get(email = postData['loginEmail'])
            if postData['loginPassword'] == user_to_login.password:
                print("Password accepted, logging in...")
            else:
                errors['invalid'] = "Invalid login credentials."
        return errors

    def job_validator(self,postData):
        errors={}
        if len(postData['location']) == 0:
            errors['need_location'] = 'A location must be provided!'
        if len(postData['title']) == 0:
            errors['need_title'] = 'A title must be provided!'
        if len(postData['desc']) == 0:
            errors['need_description'] = 'A description must be provided!'
        elif len(postData['desc']) < 3:
            errors['need_location'] = 'A description must consist of at least 3 characters!'
        elif len(postData['location']) < 3:
            errors['need_location'] = 'A location must consist of at least 3 characters!'
        elif len(postData['title']) < 3:
            errors['too_short'] = 'A title must consist of at least 3 characters!'
        
        return errors
    
    def edit_validator(self,postData):
        errors={}
        if len(postData['location']) == 0:
            errors['need_location'] = 'A location must be provided!'
        if len(postData['title']) == 0:
            errors['need_title'] = 'A title must be provided!'
        if len(postData['desc']) == 0:
            errors['need_description'] = 'A description must be provided!'
        elif len(postData['desc']) < 3:
            errors['need_location'] = 'A description must consist of at least 3 characters!'
        elif len(postData['location']) < 3:
            errors['need_location'] = 'A location must consist of at least 3 characters!'
        elif len(postData['title']) < 3:
            errors['too_short'] = 'A title must consist of at least 3 characters!'
        
        return errors
    
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()
    
class Job(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    worker = models.ForeignKey(User, related_name="jobs")
    created_at = models.DateField(auto_now_add=True)
    objects = UserManager()