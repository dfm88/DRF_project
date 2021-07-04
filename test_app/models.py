from django.db import models
from django.utils import timezone

# Create your models here.


class TestModel(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True, blank=True,
                            error_messages={
                                "null": "this field cannot be null"
                            }
                            )
    description = models.TextField()
    phone_number = models.PositiveIntegerField()
    is_live = models.BooleanField(default=False)
    amount = models.FloatField()
    # campo settato come non Editable, non lo vedremo nell'Admin
    extra_name = models.CharField(
        max_length=250, editable=False, default="null", null=True, blank=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} - created at: {self.created_at.strftime(' %H: %M: %S')}"

    class Meta:
        ordering = ("-created_at",)

    # facciamo override del metodo *save* impostando il parametro extra_name prima di fare save()
    def save(self, *args, **kwargs):
        self.extra_name = f'{self.name} - {self.phone_number}'
        super().save(*args, **kwargs)


class ModelX(models.Model):
    test_content = models.ForeignKey(
        "TestModel", on_delete=models.CASCADE, related_name="test_content")
    mileage = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.test_content.name} - {self.mileage}"

    class Meta:
        ordering = ("-created_at",)
