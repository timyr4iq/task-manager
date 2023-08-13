from django.contrib.auth.models import AbstractUser
from django.db import models


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="workers"
    )

    class Meta:
        ordering = ["username"]


class Task(models.Model):
    PRIORITY_CHOICES = (
        ("URGENT", "Urgent"),
        ("HIGH", "High"),
        ("MEDIUM", "Medium"),
        ("LOW", "Low"),
        ("TRIVIAL", "Trivial"),
    )

    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    deadline = models.DateTimeField()
    is_completed = models.BooleanField()
    priority = models.CharField(
        max_length=7,
        choices=PRIORITY_CHOICES,
        default="MEDIUM"
    )
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    assignees = models.ManyToManyField(Worker, related_name="tasks")

    class Meta:
        ordering = ["deadline"]

    def __str__(self):
        return f"{self.name}: {self.description}, deadline: {self.deadline}"
