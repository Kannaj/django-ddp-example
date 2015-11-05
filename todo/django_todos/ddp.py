from dddp.api import API,DDP, Collection, Publication
from .models import Task1


class TaskCollection(Collection):
    model = Task1


class TaskPub(Publication):
    queries = [
        Task1.objects.all(),
    ]

API.register([
    TaskCollection,
    TaskPub,
])
