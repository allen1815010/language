from django.conf.urls import url
from init import views

urlpatterns = [
   url(r'^$', views.init, name='init'),
   url(r'^英文/$', views.英文, name='英文'),
   url(r'^物件導向/$', views.物件導向, name='物件導向'),
   url(r'^資料庫管理系統/$', views.資料庫管理系統, name='資料庫管理系統'),
   url(r'^電腦網路/$', views.電腦網路, name='電腦網路'),
   url(r'^創造力/$', views.創造力, name='創造力'),
   url(r'^電子商務/$', views.電子商務, name='電子商務'),
   url(r'^電腦動畫/$', views.電腦動畫, name='電腦動畫'),
   url(r'^應用統計學/$', views.應用統計學, name='應用統計學'),
   url(r'^作業研究概論/$', views.作業研究概論, name='作業研究概論'),
   url(r'^JavaScript程式設計/$', views.JavaScript程式設計, name='JavaScript程式設計'),
   url(r'^有氧舞蹈/$', views.有氧舞蹈, name='有氧舞蹈'),
   url(r'^桌球/$', views.桌球, name='桌球'),
   url(r'^高爾夫球/$', views.高爾夫球, name='高爾夫球'),
   url(r'^排球/$', views.排球, name='排球'),
   url(r'^網球/$', views.網球, name='網球'),
]

