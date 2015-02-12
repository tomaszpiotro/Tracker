from servers.models import HttpSeries

from django_cron import CronJobBase, Schedule


class HttpSeriesCronJob(CronJobBase):
    RUN_EVERY_MINS = 2
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = "servers.cron.HttpSeriesCronJob"

    def do(self):
        for series in HttpSeries.objects.all():
            series.create_next_value()
