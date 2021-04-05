from django.urls import path
from api import views 

urlpatterns = [  
    path('result/', views.ResultList.as_view()),
    path('result/<int:pk>', views.ResultDetail.as_view()),
]