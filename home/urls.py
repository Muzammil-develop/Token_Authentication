from django.urls import path
from home import views

urlpatterns = [
    path ('view' ,views.Factory_view.as_view() , name='Factory_view' ),
    path ('<int:pk>' , views.Factory_detail.as_view() , name='Factory_detail' ),
]
