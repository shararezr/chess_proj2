from django.db import models

class User(models.Model):
	username = models.CharField(max_length = 30)
	password = models.CharField(max_length = 30)
	email = models.EmailField(max_length = 30)
	check=models.BooleanField(default=False)
	key=models.CharField(max_length = 30,default='')

	def __str__(self):
		return self.username


