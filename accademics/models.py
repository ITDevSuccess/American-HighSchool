from django.db import models
from price import models as mdl
from Web.utils import BaseModel, ImageModel


# Create your models here.
class Academic(BaseModel):
    value = models.ForeignKey(mdl.Level, on_delete=models.CASCADE, null=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Les academies au sein de l'AHS"

    def __str__(self):
        return self.value
