from django.urls import path, include, reverse
from django.conf import settings
from django.conf.urls.static import static
from . import views

course_pattern = ([
    path('', views.course_view, name='course'),
    path('<subject>/<topic_question>/',views.question_view, name='topic-questions'),
])

urlpatterns = [
    path('aboutus/', views.aboutus_view, name='aboutus'),
    path('notfound/', views.notFound,name='404notFound'),

    path('subject/<subject>/', views.subject_view, name='subject'),
    path('article/<article>', views.articel_view, name='article'),
    path('allarticles/', views.articlesAlltags_view, name='allarticles'),
    path('topics/<topic>', views.topics_view, name='topics'),

    path('upd_sbj_tp/', views.update_sbj_tp_view, name='upd_sbj_tp'),
    path('<course>/', include(course_pattern)),
    path('', views.home_view, name='home'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
