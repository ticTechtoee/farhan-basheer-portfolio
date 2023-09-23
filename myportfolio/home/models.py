from django.db import models

class Projects(models.Model):
    CATEGORY = [
        ('Web','Web Development'),
        ('Desktop','Desktop App Development')
    ]
    title = models.CharField(max_length = 40)
    description = models.TextField()
    category = models.CharField(max_length = 7, choices = CATEGORY)
    image_1 = models.ImageField(default='images/default.jpg', upload_to = 'images/') 
    image_2 = models.ImageField(default='images/default.jpg', upload_to = 'images/') 
    image_3 = models.ImageField(default='images/default.jpg', upload_to = 'images/') 
    client = models.CharField(max_length = 20)
    project_date = models.DateField()
    project_url = models.URLField()
    
    class Meta:
        verbose_name_plural = "Projects"
    def __str__(self):
        return self.title


