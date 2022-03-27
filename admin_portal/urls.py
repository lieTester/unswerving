from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    path('QuestionsReview/', views.dashBD_QuestionsReview, name='QuestionsReview'),
    path('QuestionAddAlter/<int:data>', views.dashBD_QuestionAddAlter,
         name='QuestionAddAlter'),
    path('QuestionAddAlter/<data>', views.dashBD_QuestionAddAlter,
         name='QuestionAddAlter'),

    path('ArticlesReview/', views.dashBD_ArticlesReview, name='ArticlesReview'),
    path('ArticleAddAlter/<int:data>', views.dashBD_ArticleAddAlter,name='ArticleAddAlter'),
    path('ArticleAddAlter/<data>', views.dashBD_ArticleAddAlter,name='ArticleAddAlter'),

    path('TopicSubjectCourse', views.TopicSubjectCourse,name='TopicSubjectCourse'),
    path('MembersData', views.MembersData, name='MembersData'),
    path('UserUploads', views.UserUploads, name='UserUploads'),
    path('Courses_Topics_Tags_all/', views.All_cstptg, name='Courses_Topics_Tags_all'),

    path('', views.login_view, name='login'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
