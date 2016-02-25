import time

from celery import task
from celery.task import Task

from .models import Item, BatchWork


class AddTask(Task):
    """
    ``celery.task.Task`` クラスを継承して定義する｡

    """
    def run(self, *args, **kwargs):
        arg = args

        items = Item.objects.all()[:100]

        batch_cnt = items.count()

        for item in items:
            BatchWork(name=item.name, date=item.date).save()

