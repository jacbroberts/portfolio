from django.db import models
from django.utils import timezone
from django.db.models.functions import Lower

#supports dynamic navigation bar other than home
#supports several types of page templates: timeline, blogs
class Page(models.Model):
    TIMELINE = "TL"
    BLOG = "BG"
    SKILL = "SK"
    TYPE_CHOICES = {
        TIMELINE: "Timeline",
        BLOG: "Blog",
        SKILL: "Skill"
    }

    name = models.CharField(max_length=20,unique=True)
    description = models.CharField(max_length=250,blank=True)
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default=BLOG
    )

    def __str__(self):
        return self.name
    
    class Meta:
        constraints = [
            models.UniqueConstraint(Lower('name'),name='unique_page_case_insensitive')
        ]

class Entry(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.page.name}: {self.title}"

class TimeEntry(models.Model):
    entry = models.OneToOneField(Entry, on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=75)
    start_date = models.DateField()
    end_date = models.DateField()
    present = models.BooleanField(default=False)
    body = models.TextField()

    def __str__(self):
        return f"{self.entry.page.name}: {self.entry.title}"
    
    #todo: update end_date if present is selected

class Post(models.Model):
    entry = models.OneToOneField(Entry, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=75)
    posted = models.DateField(default=timezone.now)
    body = models.TextField()

    def __str__(self):
        return f"{self.page.name}: {self.title}"
    

class Skill(models.Model):
    name = models.CharField(max_length=30, unique=True)
    entry = models.ManyToManyField(Entry)
    hidden = models.BooleanField(default=False)
    #todo: add image field for logo

    class Meta:
        constraints = [
            models.UniqueConstraint(Lower('name'),name='unique_skill_case_insensitive')
        ]

    def __str__(self):
        return self.name