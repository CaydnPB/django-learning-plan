from django.db import models

class ProjectBoardIssue(models.Model):
    BOARD_CHOICES = [
        (0, 'Board 0'),
        (1, 'Board 1'),
        (2, 'Board 2'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')
    board_number = models.IntegerField(choices=BOARD_CHOICES, default=0)

    def __str__(self):
        return self.title