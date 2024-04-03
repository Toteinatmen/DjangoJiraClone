
from rest_framework.decorators import api_view

from .models import User, JobTitle, Project, Task, UserWithTask
from .serializer import UsersSerializer, JobTitleSerializer, ProjectSerializer, TaskSerializer, UserWithTaskSerializer
from .basic_comands import db_get
from .token_managing import UserView


@api_view(['GET', 'POST', 'DELETE'])
def get_all_job_titles(request):

    job_title = JobTitle.objects.all()
    if request.method == 'GET':
        return db_get(job_title, JobTitleSerializer, JobTitle)


@api_view(['GET'])
def get_all_user_task(request, user_id):
    user_with_task = UserWithTask.objects.all().filter(user_id=user_id)
    if request.method == 'GET':
        return db_get(user_with_task, UserWithTaskSerializer, UserWithTask)


@api_view(['GET'])
def get_all_task_for_project(request,project_id):
    if request.method == 'GET':
        task_for_project = Task.objects.all().filter(project_id=project_id)
        return db_get(task_for_project, TaskSerializer, Task)


@api_view(['GET'])
def check_auth(request):
    r = UserView().get(request)
    if r.data['message'] == 'Ты аутетифицирован':
        return True
    else:
        return False

@api_view(['GET'])
def get_members_of_project(request, project_id):
    if request.method == 'GET':
        uwt = UserWithTask.objects.all().filter(project_id=project_id)
        u = []
        for i in uwt:
            u.append(User.objects.get(id=i.id))
        return db_get(u,UsersSerializer,User)