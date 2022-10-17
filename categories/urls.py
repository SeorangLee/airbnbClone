from django.urls import path
from . import views

urlpatterns = [
  path("", views.CategoryViewSet.as_view(
    {
      "get" :"list",
      "post" :"create",
    }
  )),
  path("<int:pk>", views.CategoryViewSet.as_view( 
    # pk를 받는 애들은 get, post, delete 연결시켜주는 함수 이름이 다르다 
    {
      'get' : 'retrieve',
      'put' : 'partial_update',
      'delete' : "destroy",
    }
  )),
]