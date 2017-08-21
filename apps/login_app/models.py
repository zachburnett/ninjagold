from __future__ import unicode_literals
import bcrypt 
from django.db import models
import re 

# Create your models here.
class UserManager(models.Manager):
    def Regval(self, postdata):
        results ={'status': True, 'errors': []}
        if not re.match(r'(\w+[.|\w])*@(\w+[.])*\w+',postdata['email']):
            results['errors'].append('please use a valid email')
        if len(postdata['password']) < 5:
            results['errors'].append('your password msut be atleast 5 characters long!')
        if postdata['password'] != postdata['c_password']:
            results['errors'].append('your password doesnt match')
        if self.filter(email= postdata['email']):
            results['errors'].append('user already exsits')

        if len(results['errors']) >0:
            results['status'] = False
        return results

    def creator(self, postdata):
        hashed = bcrypt.hashpw(postdata['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(email = postdata['email'],
        password = hashed, total=0) 
        return user

    def loginval(self,postdata):
        results = {'status': True, 'errors': [], 'user': None}
        users = self.filter(email= postdata['email'])
        if len(users) <1:
            results['errors'].append('somethng went wrong')
        else:
             if bcrypt.checkpw(postdata['password'].encode(),users[0].password.encode()) == False:
                 results['errors'].append('password did not match ')
        if len(results['errors']) > 0 :
            results['status'] = False
        else:
            results['user'] = users[0]

        return results
    def show_total(self):
        print User.objects.total
        return self

class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    total = models.IntegerField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    objects = UserManager()
    def __repr__(self):
        return "<{}>".format(self.email)
