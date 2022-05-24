from django.db import models

class Argument(models.Model):
    
    title = models.CharField(max_length=100)
    aim = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(to='Person', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self): 
        return self.title



class Meta:
    verbose_name = "Argument"
    verbose_name_plural = "Arguments"