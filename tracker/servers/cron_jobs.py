from charts.models import Series

from django_cron import CronJobBase, Schedule


class SeriesCronJob(CronJobBase):
    RUN_EVERY_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = "servers.cron.HttpSeriesCronJob"

    def do(self):
        for series in Series.objects.all():
            series.create_next_value()
