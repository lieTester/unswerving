from django.contrib.auth.models import User
from django import template
from ..forms import *
from admin_portal.models import *


Courses = Courses_Exams.objects.all()
Topics = Topics_comes.objects.all()
Tags = Tags_toMatch.objects.all()
Questions = Question_data.objects.all()
Articles = Article_data.objects.all()
Subjects = Subjects_toStudy.objects.all()


def grabBasicToAll(*data):
    user = User.objects.get(username=data[0])
    context = {
        "user": user,
        "Courses": Courses,
        "Topics": Topics,
        "Subjects": Subjects
    }

    if len(data) == 1:
        context["Articles"] = Articles
        context["Questions"] = Questions

    elif data[1] == 'CST':
        context["Cform"] = AddCourse()
        context["Sform"] = AddSubject()
        context["Tform"] = AddTopics()

    elif data[1] == 'Course':
        context["Sform"] = AddSubject()
        context["Tform"] = AddTopics()
        try:
            course = Courses_Exams.objects.get(Exam_Type=data[2])
            context["Cform"] = AddCourse(instance=course)
        except:
            print('An exception occurred')
            context["Cform"] = AddCourse()

    elif data[1] == 'Subject':
        context["Cform"] = AddCourse()
        context["Tform"] = AddTopics()
        try:
            subject = Subjects_toStudy.objects.get(Subj_Type=data[2])
            context["Sform"] = AddSubject(instance=subject)
        except:
            print('An exception occurred')
            context["Sform"] = AddSubject()

    elif data[1] == 'Topic':
        context["Cform"] = AddCourse()
        context["Sform"] = AddSubject()
        try:
            topic = Topics_comes.objects.get(Topic_Type=data[2])
            context["Tform"] = AddTopics(instance=topic)
        except:
            print('An exception occurred')
            context["Tform"] = AddTopics()

    return context


def grab_for_CST(*data):
    pass


def grab_for_Qform(*data):
    # print(len(data))
    if len(data) == 1:
        try:
            user = User.objects.get(username=data[0])
            Qform = AddorUpdateQuestion()
            context = {
                "user": user,
                "Qform": Qform,
                "Courses": Courses,
                "Topics": Topics,
            }
            return context
        except Exception as e:
            print('An exception occurred=>', e)
            context = {}
            return context
    elif len(data) == 2:
        try:
            user = User.objects.get(username=data[0])
            question = Question_data.objects.get(Question_Id=data[1])
            # print(question.Question_Id)
            defaults = {
                'Exam_Id': question.Exam_Id.all(),
                'Topic_Id': question.Topic_Id.all(),
                'Creater_Id': question.Creater_Id,
                'Question_detail': question.Question_detail,
                'Question_Options': question.Question_Options,
                'Question_Correct_Option': question.Question_Correct_Option,
                'Question_Ans_Explain': question.Question_Ans_Explain
            }
            Qform = AddorUpdateQuestion(initial=defaults)
            context = {
                "user": user,
                "Qform": Qform,
                "Courses": Courses,
                "Topics": Topics,
            }
            return context
        except Exception as e:
            print('An exception occurred=>', e)
            context = {}
            return context


def grab_for_Aform(*data):
    # print(len(data))
    if len(data) == 1:
        try:
            user = User.objects.get(username=data[0])
            Aform = AddorUpdateArticle()
            context = {
                "user": user,
                "Aform": Aform,
                "Tags": Tags,
            }
            return context
        except Exception as e:
            print('An exception occurred=>', e)
            context = {}
            return context
    elif len(data) == 2:
        try:
            user = User.objects.get(username=data[0])
            article = Article_data.objects.get(Article_Id=data[1])
            # print(article.Article_Id)
            defaults = {
                'Tag_Id': article.Tag_Id.all(),
                'Creater_Id': article.Creater_Id,
                'Article_Heading': article.Article_Heading,
                'Article_detail': article.Article_detail,
            }
            Aform = AddorUpdateArticle(initial=defaults)
            context = {
                "user": user,
                "Aform": Aform,
                "Tags": Tags,
            }
            return context
        except Exception as e:
            print('An exception occurred=>', e)
            context = {}
            return context


def tag_all():
    alltg = []
    tag = {}
    for item in Tags:
        tag[item.Tag_Type] = item.Tag_Id

    alltg.append(tag)
    # print(alltg)
    return alltg


def course_subject_topic_all():
    allcstp = []
    courses = {}
    subjects = {}
    topics = {}
    for item in Courses:
        courses[item.Exam_Type] = item.Exam_Id
    for item in Subjects:
        subjects[item.Subj_Type] = item.Subj_Id
    for item in Topics:
        topics[item.Topic_Type] = item.Topic_Id

    allcstp.append(courses)
    allcstp.append(topics)
    allcstp.append(subjects)
    return allcstp


def filter_member_data(*user):
    context = {}
    if user[1] == "Qreview":
        user = User.objects.get(username=user[0])
        member_ques = Question_data.objects.filter(Creater_Id=user.id)
        context["member_ques"] = member_ques.order_by('-Question_Add_Time')
        context["user"] = user
    elif user[1] == "Areview":
        user = User.objects.get(username=user[0])
        member_artcls = Article_data.objects.filter(Creater_Id=user.id)
        context["member_artcls"] = member_artcls.order_by('-Article_Add_Time')
        context["user"] = user
    elif user[1] == "memberALL":
        member_data = User.objects.get(id=user[0])
        member_ques = member_data.question_data_set.all().order_by('-Question_Add_Time')
        member_artcls = member_data.article_data_set.all().order_by('-Article_Add_Time')
        member_interestTopics = []
        # member_interestTopics = []
        member_interestSubjects = []

        for data in member_ques:
            for topics in data.Topic_Id.all():
                if topics not in member_interestTopics:
                    member_interestTopics.append(topics)

        for topic in member_interestTopics:
            for subject in topic.subjects_tostudy_set.all():
                if subject not in member_interestSubjects:
                    member_interestSubjects.append(subject)

        context["member_ques"] = member_ques
        context["member_artcls"] = member_artcls
        context["member_subj"] = member_interestSubjects
        context["member_tpcs"] = member_interestTopics

    return context


# ###############################################################################
# Filters code below
# ###############################################################################
register = template.Library()


@register.filter(name='align_manyField')
def align_manyField(alist):
    return len(alist)


def fetch_all():
    pass
