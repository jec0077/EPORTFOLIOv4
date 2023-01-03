from django.db import models


class ExperienceCard(models.Model):
    name_of_role = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    start_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20)
    description = models.TextField()

    # image_720x600 = models.ImageField()

    def __str__(self):
        return self.name_of_role


class ProjectCard(models.Model):
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    project_link = models.URLField()

    # image_720x600 = models.ImageField()

    def __str__(self):
        return self.project_name


class Contact(models.Model):
    message_sender_email = models.EmailField()
    message_subject = models.CharField(max_length=100)
    message_content = models.TextField()

    def __str__(self):
        return self.message_subject
