from django.db import models
from django.contrib.auth.models import User

class Subjects(models.Model):
	SUBJECT_OPTIONS = (
		('A', 'Applied Arts'),
		('C', 'Chinese'),
		('FI', 'Fine Arts'),
		('FR', 'French'),
		('H', 'Hebrew'),
		('I', 'Italian'),
		('M', 'Math'),
		('SC', 'Science'),
		('SO', 'Social Studies'),
		('SP', 'Spanish'),
		('T', 'TPI'),
	)
	subject = models.CharField(max_length=2, choice=SUBJECT_OPTIONS, unique=True)
	
class Titles(models.Model):
	TITLE_OPTIONS = (
		('', 'Art Through Ages 14th ed')
		('', 'Tonal Harmony')
		('', 'Soc: Down to Earth Appr')
		('', 'Give Me Liberty! An American History 3 ed')
		('', 'City of Big Shoulders')
		('', 'Thinking About Psych')
		('', 'Hist of Western Soc')
		('', 'Economics- Concepts/Choices')
		('', 'Economics-17th ed ')
		('', 'Psych-Myers')
		('', 'Chemistry-Zumdahl')
		('', 'Environ Sci')
		('', 'Bio/ Prentice Hall')
		('', 'Stiff-paperback')
		('', 'Algebra I')
		('', 'Alg/Trig Func classic ed')
		('', 'Geom Enjoy/Challenge')
		('', 'Geom Concept/ Skills')
		('', 'Precalculus 6th ed ')
		('', 'Stats:Modeling World')
		('', 'Java Concepts ')
		('', 'Algebra 2')
		('', 'Discrete Math Appl ')
		('', 'Geom-Prentice Hall')
		('', 'Calculus/ Graphical, Numeric')
		('', 'Multivariable Calculus ')
		('', 'History Alive US-Modern')
		('', 'Keys to Learning')
		('', 'History Alive-Am Ideals')
		#begin at spansih
		('', '')
		('', '')
		('', '')
		('', '')
	)
	name = models.CharField(max_length=, choice=TITLE_OPTIONS, unique=True)
	isbn = models.IntegerField(unique=True)
	subject = models.ForeignKey(Subjects)

class Listings(models.Model):
	seller = models.ForeignKey(UserProfile)
	book = models.ForeignKey(Titles)
	price = models.IntegerField()
	

	

