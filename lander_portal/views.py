
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import *
from lander_portal.templatetags.myDataFunct import *

main_data_list = main_Data()


def home_view(request):

    context = {
        "courses": main_data_list[0],
        "subjects": main_data_list[1],
        "articles": main_data_list[2].order_by('-Article_Add_Time')[:5],
    }
    return render(request, "lander_portal/home.html", context)


def course_view(request, course):
    try:
        if (course):
            # from here we are getting subjects of course whose data we use in template

            course = Courses_Exams.objects.get(Exam_Type=course)
            course_subjs = course.Subj_Id.all()

            try:
                subjreq = request.GET.get('subjreq')
                curnt_sbj = Subjects_toStudy.objects.get(Subj_Id=subjreq)
                subj_topics = curnt_sbj.Topic_Id.all()
            except:
                curnt_sbj = Subjects_toStudy.objects.get(
                    Subj_Id=course_subjs[0].Subj_Id)
                subj_topics = curnt_sbj.Topic_Id.all()

    except Exception as e:
        course = curnt_sbj = course_subjs = subj_topics = ''
        print('An exception occurred course_view\n', e, course)
        return redirect('404notFound')

    context = {
        "courses": excludeCourse(course),
        "subjects": main_data_list[1],
        "course_name": course,
        "course_subjs": course_subjs,
        "curnt_sbj": curnt_sbj,
        "subj_topics": subj_topics,
        "articles": main_data_list[2].order_by('-Article_Add_Time')[:6],
        "related_topics": excludeTopics(course, subj_topics),
    }
    return render(request, "lander_portal/components/course.html", context)


def subject_view(request, subject):

    # pass

    try:
        curnt_sbj = Subjects_toStudy.objects.get(Subj_Type=subject)
        subj_topics = main_subj_tp(curnt_sbj.Subj_Id)
        # curnt_subj_id = course_subjs[0].Subj_Id

        # so senario is somthing like that we are fetching by default 1st topic qutions,
        # but when other topic click on page then we fetch that topic questions.
        try:
            topic_question = request.GET.get('topic_question')
            # print(topic_question, "topicID",request.GET.get('quespage'))
            topic = Topics_comes.objects.get(Topic_Id=topic_question)
            all_quetions = Question_data.objects.filter(
                Topic_Id=topic_question)
        except:
            topic = subj_topics[0]
            all_quetions = Question_data.objects.filter(
                Topic_Id=topic.Topic_Id)

        try:
            # and here we are fetching the next page of quetions
            # and calculated some errors accordingly if occur we maintain
            # website stablity
            question_page = Paginator(all_quetions, 1)

            try:
                quespage = request.GET.get('quespage')
                print(quespage)
                qustn_page = question_page.page(quespage)
            except EmptyPage:
                qustn_page = question_page.page(question_page.num_pages)
            except:
                qustn_page = question_page.page(1)
                print('default')
        except:
            print('An exception occurred')
            # return redirect('404notFound')

    except:
        subj_topics = subj_name = qustn_page = curnt_sbj = topic = ''
        print('An exception occurred subject_view')

    context = {
        "courses": main_data_list[0],
        "subjects": main_data_list[1].exclude(Subj_Type=subject),
        "subj_topics": subj_topics,
        "questions": qustn_page,
        "subj_name": curnt_sbj,
        "topicpage": topic,
        "articles": main_data_list[2].order_by('-Article_Add_Time')[:6],
    }
    return render(request, "lander_portal/components/subject.html", context)


def question_view(request, course, subject, topic_question):
    # pass
    try:
        topic = Topics_comes.objects.get(Topic_Type=topic_question)
        curnt_sbj = Subjects_toStudy.objects.get(Subj_Type=subject)
        course = Courses_Exams.objects.get(Exam_Type=course)
        # print(topic.Topic_Id, topic.Topic_Type)

        all_quetions_filter = topic.question_data_set.filter(
            Exam_Id=course.Exam_Id)
        question_page = Paginator(all_quetions_filter, 1)
        try:
            quespage = request.GET.get('quespage')
            qustn_page = question_page.page(quespage)
        except PageNotAnInteger:
            qustn_page = question_page.page(1)
        except EmptyPage:
            qustn_page = question_page.page(question_page.num_pages)

    except:
        topic = qustn_page = ''
        print('An exception occurred question_view')

    print(qustn_page)
    context = {
        "courses": main_data_list[0],
        "subjects": main_data_list[1],
        "topic": topic,
        "course_name": course,
        "curnt_sbj": curnt_sbj,
        "questions": qustn_page,
        "articles": main_data_list[2].order_by('-Article_Add_Time')[:6],
        "related_topics": excludeTopics(course, topic, 'forQpage'),
    }
    return render(request, "lander_portal/components/questions.html", context)


def topics_view(request, topic):

    question_page = Paginator(Question_data.objects.filter(
        Topic_Id=topic).order_by('-Question_Add_Time'), 2)

    try:
        quespage = request.GET.get('quespage')
        qustn_page = question_page.page(quespage)
    except PageNotAnInteger:
        qustn_page = question_page.page(1)
    except EmptyPage:
        qustn_page = question_page.page(question_page.num_pages)

    context = {
        "courses": main_data_list[0],
        "subjects": main_data_list[1],
        "questions": qustn_page,
        "curnt_topic": Topics_comes.objects.get(Topic_Id=topic),
        "topics": main_data_list[3].exclude(Topic_Id=topic),
        "articles": main_data_list[2].order_by('-Article_Add_Time')[:6],
    }
    return render(request, "lander_portal/components/topics.html", context)


def articel_view(request, article):
    article = Article_data.objects.get(Article_Id=article)

    context = {
        "courses": main_data_list[0],
        "subjects": main_data_list[1],
        "article": article,
        "topics": main_data_list[3],
        "tags": main_data_list[4].order_by('-Tag_Add_Time'),
        "articles": main_data_list[2].order_by('-Article_Add_Time')[:6],
    }
    return render(request, "lander_portal/components/article.html", context)


def articlesAlltags_view(request):

    context = {
        "courses": main_data_list[0],
        "subjects": main_data_list[1],
        "topics": main_data_list[3],
        "tags": main_data_list[4].order_by('-Tag_Add_Time')
    }

    article_page = ''
    if request.GET.get('relatedto'):
        allreleted = Article_data.objects.filter(
            Tag_Id=request.GET.get('relatedto'))
        print(allreleted)
        article_page = Paginator(allreleted.order_by(
            '-Article_Add_Time').order_by('-Article_Add_Time'), 2)
    else:
        article_page = Paginator(
            main_data_list[2].order_by('-Article_Add_Time'), 2)

    try:
        articlepage = request.GET.get('artclpage')
        article_page = article_page.page(articlepage)
    except PageNotAnInteger:
        article_page = article_page.page(1)
    except EmptyPage:
        article_page = article_page.page(article_page.num_pages)

    context["articles"] = article_page

    return render(request, "lander_portal/components/articlesAlltags.html", context)


def aboutus_view(request):
    context = {
        "courses": main_data_list[0],
        "subjects": main_data_list[1],
    }
    return render(request, "lander_portal/aboutus.html", context)


def notFound(request):
    context = {
        "courses": main_data_list[0],
        "subjects": main_data_list[1],
    }
    return render(request, "lander_portal/404NOTFound.html", context)


# use below view to some other ajax query
def update_sbj_tp_view(request):
    if request.method == 'GET':
        # Sending an success response
        topics = main_subj_tp(request.GET['subj_id'])
        data = []
        return JsonResponse({"data": data})
    else:
        return JsonResponse({"sucess": "Request method is not a GET"})


# exam2 = Courses_Exams.objects.get(Exam_Type="UPSC")
    # course_subjs2 = exam.Subj_Id.all()
    # print(exam1, course_subjs1)
    # for item in course_subjs:
    #     print(Subjects_toStudy.objects.get(Subj_Type=item).Topic_Id.all())

#


####################################################################
# a basic code ve use before for ajax to change topic without refresh

# del request.session['current_sbj_id']
# request.session['current_sbj_id'] = request.GET['subj_id']
# for topic in topics:
#     item = {
#         "id": topic.Topic_Id,
#         "name": topic.Topic_Type,
#     }
#     data.append(item)
