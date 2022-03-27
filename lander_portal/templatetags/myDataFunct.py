from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import template
from ..models import *


register = template.Library()

# global use of below arrays in file
sb_topics = []
newarr = []
exams = Courses_Exams.objects.all()
subjects = Subjects_toStudy.objects.all()
articles = Article_data.objects.all()
topics = Topics_comes.objects.all()
tags = Tags_toMatch.objects.all()


def main_Data():
    return [exams, subjects, articles, topics,tags]


def main_subj_tp(sb_id):
    sbj = Subjects_toStudy.objects.get(Subj_Id=sb_id)
    # sb_topics.clear()
    # sb_topics.append(sbj.Topic_Id.all())
    # return sb_topics[0]
    return sbj.Topic_Id.all()


def excludeCourse(value):
    return exams.exclude(Exam_Type=value)


def excludeSubjects(value):
    newarr.clear()
    for item in value:
        # print(item)
        newarr.append(item)
    return subjects.exclude(Subj_Type__in=newarr)


def excludeTopics(*value):
    newarr.clear()
    try:
        for subjs in Courses_Exams.objects.get(Exam_Type=value[0]).Subj_Id.all():
            newsubj = Subjects_toStudy.objects.get(Subj_Type=subjs).Topic_Id.all()
            for topic in newsubj:
                if len(value) > 2 and value[2] == 'forQpage':
                    if topic not in newarr and value[1] != topic :
                        # print(value[1])
                        newarr.append(topic)
                else:
                    if topic not in newarr and topic not in value[1]:
                        newarr.append(topic)
    except Exception as e:
        print('An exception occurred',e)
        # print(newarr, '\n')
    return newarr


def excludeArticles(value, arr):
    pass


@register.filter(name='make_list')
def make_list(string):
    if '[' and ']' in string:
        data_list = string[1: (len(string) - 1)].split('(,)')
    else:
        data_list = string.split('(,)')
    return data_list


@register.filter(name='cut_first')
def cut_first(string):
    if len(string) > 2:
        data_list = string[:2]
    else:
        data_list = string
    return data_list
