from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("registerpage",views.registerpage, name="registerpage"),
    path("login",views.login, name="login"),
    path("felo",views.felo, name="felo"),
    path("mainpage",views.mainpage, name="mainpage"),
    path("success/<str:code>",views.success, name="success"),
    path("displaystud",views.displaystud, name="displaystud"),
    path("updatestudent/<str:studentid>",views.updatestudent, name="updatestudent"),
    path('updatestudent/save_updatestudent/<str:studentid>',views.save_updatestudent, name='save_updatestudent'),
    path("deletestudent/<str:studentid>",views.deletestudent, name="deletestudent"),
    path("displaybooking",views.displaybooking, name="displaybooking"),
    path("updatebooking/<str:id>",views.updatebooking, name="updatebooking"),
    path('updatebooking/save_updatebooking/<str:id>',views.save_updatebooking, name='save_updatebooking'),
    path("deletebooking/<str:id>",views.deletebooking, name="deletebooking"),
]