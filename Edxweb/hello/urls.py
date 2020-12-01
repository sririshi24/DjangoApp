from django.urls import path
from . import views

urlpatterns = [

	path("",views.index,name="index"),
	path("sayhello",views.say_hello,name="sayhello"),
	path("<str:name>",views.great,name="great")
	]

