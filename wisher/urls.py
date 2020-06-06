from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name ="home"),
    path("handlesignup",views.handlesignup,name="handlesignup"),
    path("handlelogin",views.handlelogin,name="handlelogin"),
    path("handlelogout",views.handlelogout,name="handlelogout"),
    path("about",views.about,name="about"),
    path("addbirthday",views.addbirthday,name = "addbirthday"),
    path("addtodb",views.addtodb,name = "addtodb"),
    path("remove",views.remove,name="remove"),
    path("update",views.update,name="update"),
    path("updatenow",views.updatenow,name="updatenow"),
    path("sendemail",views.sendemail,name="sendemail"),
]