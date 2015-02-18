from django.db import models


class Server(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name="server name"
    )
    website_address = models.URLField(
        verbose_name="website address"
    )


class Realm(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name="realm name"
    )
    server = models.ForeignKey(
        Server,
        verbose_name="server",
        related_name="realms"
    )
