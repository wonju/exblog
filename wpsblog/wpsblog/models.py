from django.db import models
from django.core.urlresolvers import reverse


class Post(models.Model):
    title = models.CharField(
        max_length=120,
    )
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "post-detail",
            kwargus={
                "post_id": sefl.id,
            }
        )
