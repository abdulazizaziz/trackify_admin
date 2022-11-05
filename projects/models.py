from django.db import models

# Create your models here.
class Project(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now=True)
    idol = models.CharField(max_length=100)
    clicks = models.IntegerField(default=0)
    presses = models.IntegerField(default=0)

    class Meta:
        db_table = 'project'


class ScreenShot(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name='screenshots')
    screenshot = models.ImageField(upload_to='screenshots')
    
    class Meta:
        db_table = 'screenshots'


class TimeSheet(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name='timesheets')
    status = models.IntegerField(default=0)

    class Meta:
        db_table = 'timesheet'
