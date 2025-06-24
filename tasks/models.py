from django.db import models

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    disc = models.TextField()
    created_at = models.DateTimeField()
    due_date = models.DateTimeField()
    complete_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending')  # 'Pending' or 'Complete'
    remark = models.CharField(max_length=20, default='on_time')  # on_time, before_time, after_time
    is_completed = models.BooleanField(default=False)  # Updated field

    def __str__(self):
        return self.title
