from django.db import models

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length = 30)
	pub_date = models.DateTimeField()
	image = models.ImageField(upload_to = 'images/')
	body = models.TextField()

	def summary(self):
		return self.body[:100]