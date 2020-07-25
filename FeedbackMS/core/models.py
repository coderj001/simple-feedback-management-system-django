from django.db import models
import uuid

SIR_NAME_CHOICES=(
	('Mr','Mr'),
	('Mrs','Mrs'),
	('Other','Other')
	)

DEPT_CHOICES=(
	('Mathematics','Mathematics'),
	('English','English'),
	('Physics','Physics'),
	('Computer','Computer'),
	('Chemistry','Chemistry'),
	('Electrical','Electrical'),
	)

class Teacher(models.Model):
	id=models.AutoField(primary_key=True,editable=False)
	sir_name=models.CharField(choices=SIR_NAME_CHOICES,max_length=5, verbose_name='Teacher Sir Name')
	first_name=models.CharField(max_length=255,blank=False,verbose_name='Teacher First Name')
	last_name=models.CharField(max_length=255,blank=True, verbose_name='Teacher Last Name')
	deperment=models.CharField(choices=DEPT_CHOICES,max_length=20)

	def __str__(self):
		if self.sir_name == 'Other':
			return "{} {}".format(self.first_name,self.last_name)
		else:
			return "{}. {} {}".format(self.sir_name,self.first_name,self.last_name)

RATING_CHOICES=(
	('Very Poor','Very Poor'),
	('Poor','Poor'),
	('Average','Average'),
	('Good','Good'),
	('Very Good','Very Good'),
	)

class FeedBack(models.Model):
	id=models.UUIDField(primary_key=True,default=uuid.uuid1,editable=False)
	name=models.CharField(max_length=500,blank=True)
	teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE)
	rating=models.CharField(choices=RATING_CHOICES,max_length=20,default='Average')
	date=models.DateTimeField(auto_now_add=True, editable=False)
	detail=models.TextField(blank=True)

	def __str__(self):
		return str(self.id)

