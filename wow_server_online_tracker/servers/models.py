from django.db import models


class Server(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name="server name"
    )
    website_address = models.URLField(
        verbose_name="website address"
    )

    class Meta:
        app_label = "servers"


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

    class Meta:
        app_label = "servers"
