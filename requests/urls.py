from django.urls import re_path, path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.index),
    path('category', views.category),
    path('homepage', views.HomePage),
    path('location', views.location),
    path('ADinfo', views.ADinfo),
    path('more', views.more),
    path('comment', views.comment),
    path('receive_comments', views.show_comment),
    path('search_data', views.Search_data),
    path('addscore', views.getHighScore),
    path('test', views.test),
    path('userData', views.userData),
    path('Buy', views.Buy),
    path('submit_buy', views.submit_buy),
    path('getNotif', views.get_notif),
    path('register', views.register_user),
    path('check_registered', views.check_user_exists),
    path('check_user_exist', views.check_username_exists),
    path('get_profile', views.return_name),
    path('video_award', views.video_award),
    path('games', views.games),
    path('game_page', views.game_page),
    path('Turnover', views.turnover_Dj),
    path('notification', views.notifs),
    path('set_rate', views.submit_rate),
    path('submit_new_ad', views.submit_new_ad),
    # path('invite',views.invite)
    path('add_to_event',views.add_to_event),
    # Hafez's changes ------
    path('admin/', admin.site.urls),
    path('quiz/', views.index, name='index'),
    re_path(r'^quiz/(?P<username>[\w.@+-]+)/(?P<quiz_id>[0-9]+)/$', views.detail, name='detail'),
    re_path(r'^quiz/(?P<username>[\w.@+-]+)/(?P<quiz_id>[0-9]+)/(?P<quest_id>[0-9]+)/(?P<previous_answer>[0-9]+)/$',
            views.question, name='question'),
    re_path(r'^quiz/(?P<username>[\w.@+-]+)/(?P<quiz_id>[0-9]+)/(?P<quest_id>[0-9]+)/(?P<previous_answer>[0-9]+)/score/$',
            views.question, name='score'),
    path('get_user_events',views.get_user_events),
    path('get_seller_data', views.get_seller_data),
    path('remove_seller_code', views.remove_seller_code)
]
