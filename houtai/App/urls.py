import App.views

from django.urls import path

urlpatterns = [
    # path('<str:module>/',App.views.SysView.as_view()),
    # path('notices/<str:module>/', App.views.NoticesView.as_view()),
    # path('check/<str:module>/', App.views.CheckLogsView.as_view()),
    # path('vaccinate/<str:module>/', App.views.VaccinateLogsView.as_view()),
    # path('abnormity<str:module>/', App.views.AbnormityLogsView.as_view()),
    # path('statistics<str:module>/', App.views.StatisticsLogsView.as_view()),
    # path('users/<str:module>/', App.views.UsersView.as_view()),
    path('<str:module>/',App.views.SysView.as_view()),
    path('duishou/<str:module>/', App.views.duishou.as_view()),

    path('keshihua/<str:module>/',App.views.keshihua.as_view()),


]