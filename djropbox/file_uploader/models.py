from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from djropbox.user.models import BoxUser


class Folder(MPTTModel):
    parent = TreeForeignKey('self', related_name='children', null=True, blank=True, db_index=True,
                            on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    creator = models.ForeignKey(BoxUser, on_delete=models.CASCADE)


    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

class NewFile(models.Model):
    folder = TreeForeignKey(Folder, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    document = models.FileField(upload_to='documents/')
    time_created = models.DateTimeField(auto_now_add=True)