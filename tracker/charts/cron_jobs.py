from .models import HttpSeries

from django_cron import CronJobBase, Schedule


class SeriesCronJob(CronJobBase):
    RUN_EVERY_MINUTES = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINUTES)
    code = "servers.cron.HttpSeriesCronJob"

    def do(self):
        for series in HttpSeries.objects.all():
            series.create_next_value()
