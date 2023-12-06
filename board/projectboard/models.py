from django.db import models

class ProjectBoardIssue(models.Model):
    PROJECT_CHOICES = [
        (1, 'Project 1'),
        (2, 'Project 2'),
        (3, 'Project 3'),
    ]

    BOARD_CHOICES = [
        (1, 'Board 1'),
        (2, 'Board 2'),
        (3, 'Board 3'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')
    project_number = models.IntegerField(choices=PROJECT_CHOICES, default=0)
    board_number = models.IntegerField(choices=BOARD_CHOICES, default=0)

    def __str__(self):
        return self.title