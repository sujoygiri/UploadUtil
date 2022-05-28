from django.db import models
import uuid

class File(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(blank=False, null=False)
    
    def __str__(self):
        return self.file.name

    def delete(self, using= None, keep_parents= False):
        self.file.storage.delete(self.file.name)
        super().delete(using, keep_parents)