from django.urls import path
from . import views, specific_comands, token_managing
urlpatterns = [
    path('users/create',token_managing.RegisterView.as_view()),
    path("users/login",token_managing.LoginView.as_view()),
    path("users/auth",token_managing.UserView.as_view()),
    path('users/refresh',token_managing.refresh_token),
    
    path("user/<id>",views.user_managing),
    path("job_title/<id>",views.job_title_managing),
    path("project/<id>",views.project_managing),
    path("task/<id>",views.task_managing),
    path("user_with_task/<id>",views.user_with_task_managing),

    path("all_job_titles", specific_comands.get_all_job_titles),
    path("all_user_task/<user_id>", specific_comands.get_all_user_task),
    path("task_for_project/<project_id>",specific_comands.get_all_task_for_project),
    path("users_in_project/<project_id>",specific_comands.get_members_of_project)
]