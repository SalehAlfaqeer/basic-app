from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100, blank='false', null='false')
    email = models.EmailField(blank='false', null='false')
    age = models.IntegerField(blank='false', null='false')
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    # ↓↓↓↓ Reuse ID ↓↓↓↓
    def save(self, *args, **kwargs):
        if self.pk is None:
            # This is a new object, so set the id to the next available value
            max_id = Student.objects.aggregate(models.Max('id'))['id__max']
            self.id = max_id + 1 if max_id is not None else 1
        else:
            # This is an existing object, so update it instead of creating a new one
            super().save(*args, **kwargs)
            return

        super().save(*args, **kwargs)