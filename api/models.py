from django.db import models



# Create your models here.
# DAYS_OF_WEEK = (
#     (0, 'Monday'),
#     (1, 'Tuesday'),
#     (2, 'Wednesday'),
#     (3, 'Thursday'),
#     (4, 'Friday'),
#     (5, 'Saturday'),
#     (6, 'Sunday'),
# )

STATUS_CODE= (
    (200, 'OK'),
    (201, 'CREATED'),
    (400, 'FAILED'),

)

class Task(models.Model):
    slack_name = models.CharField(max_length=100)
    current_day = models.CharField(max_length=100)
    track = models.CharField(max_length=100)
    utc_time= models.DateTimeField(auto_now_add=True)
    track= models.CharField(max_length=100)
    github_file_url = models.URLField(max_length=200)
    github_repo_url = models.URLField(max_length=200)
    status= models.IntegerField(choices=STATUS_CODE, max_length=20, default=200)


    def __str__(self):
        return self.slack_name







