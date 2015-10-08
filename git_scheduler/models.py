from django.db import models

from git.models import Push, Repository, Branch
from task_manager.models import Task, ScheduledTask


class RegisteredTask(models.Model):
    repository = models.ForeignKey(Repository)
    branch = models.ForeignKey(Branch, null=True, blank=True)
    task = models.ForeignKey(Task)
    user = models.CharField(max_length=32)
    assign_on_push = models.BooleanField(default=False)
    submit_status = models.BooleanField(default=False)
    working_directory = models.TextField()

    def __unicode__(self):
        name = u"Task on %s" % (self.repository, )
        if self.branch is not None:
            name += u"/%s" % (self.branch, )
        name += u": Executing '%s' as user '%s'" % (self.task, self.user)
        return name


class TaskToPush(models.Model):
    task = models.ForeignKey(ScheduledTask)
    push = models.ForeignKey(Push)


class GitHubAccessToken(models.Model):
    token = models.CharField(max_length=40)
    repositories = models.ManyToManyField(Repository)
    submit_status = models.BooleanField(default=False)