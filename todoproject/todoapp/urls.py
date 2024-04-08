from.import views
from django.urls import path,include

urlpatterns = [
        path('', views.add,name="add"),

        path('delete/<int:taskid>/', views.delete,name="delete"),
        path('update/<int:id>/', views.update,name="update"),
        path('ahome/', views.Tasklistview.as_view(),name="ahome"),
        path('adetail/<int:pk>/', views.Taskdetailview.as_view(), name="adetail"),
        path('aupdate/<int:pk>/', views.TaskUpdatView.as_view(), name="aupdate"),
        path('adelete/<int:pk>/', views.Taskdeleteview.as_view(), name="adelete"),

]