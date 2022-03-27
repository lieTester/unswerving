from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib import messages
import re
from .forms import CreateUser, AddorUpdateQuestion, AddorUpdateArticle, UploadFile
from admin_portal.models import *
from admin_portal.templatetags.dash_bd_data import *


@login_required
def register_view(request):

    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register')
    else:
        print('3')
        form = CreateUser()

    context = {"form": form}
    return render(request, 'admin_portal/register.html', context)


def login_view(request):

    if request.session.get('logUser'):
        context = grabBasicToAll(request.session.get('logUser'))
        return render(request, 'admin_portal/main.html', context)
    else:
        if request.method == "POST":
            user = request.POST.get('username')
            passwd = request.POST.get('password')
            # print(passwd,'1')
            authUser = authenticate(request, username=user, password=passwd)
            if authUser is not None:
                login(request, authUser)
                request.session['logUser'] = user
                return redirect('login')
            else:
                return render(request, 'admin_portal/login.html')
        else:
            return render(request, 'admin_portal/login.html')


@login_required
def logout_view(request):
    del request.session['logUser']
    # logout(request)
    return redirect('login')


@login_required
def dashBD_QuestionsReview(request):
    context = filter_member_data(request.session.get('logUser'), "Qreview")
    if request.session.get('impomessage'):
        messages.success(request, request.session.get('impomessage'))
        del request.session['impomessage']
    return render(request, 'admin_portal/components/QuestionsReview.html', context)


@login_required
def dashBD_QuestionAddAlter(request, data):
    context = {}
    if data == request.session.get('logUser'):
        context = grab_for_Qform(request.session.get('logUser'))
        if request.method == 'POST':
            form = AddorUpdateQuestion(request.POST)
            try:
                Qshow = request.POST.get('Question_detail', '')
                clean = re.compile('<.*?>')
                Qshow = re.sub(clean, '', Qshow)
                if form.is_valid():
                    try:
                        Question_data.objects.get(Question_show=Qshow)
                        print("Question Exist")
                    except Exception as e:
                        form.save()
                        QshowEnter = Question_data.objects.get(
                            Question_show='?', Creater_Id=context["user"].id)
                        QshowEnter.Question_show = Qshow
                        QshowEnter.save()
                        # print('An exception occurred', e, QshowEnter) #.important in terms of error check
                        return redirect('QuestionsReview')
                else:
                    messages.error(request, 'Check fields carefully!')
                    # print('notvalid1') #.important in terms of error check
            except Exception as e:
                print('dashBD_Question1', e)

    elif (isinstance(data, int)):
        context = grab_for_Qform(request.session.get('logUser'), data)
        if request.method == 'POST':
            try:
                Qshow = request.POST.get('Question_detail', '')
                clean = re.compile('<.*?>')
                Qshow = re.sub(clean, '', Qshow)
                QshowEnter = Question_data.objects.get(
                    Question_Id=data)
                form = AddorUpdateQuestion(
                    request.POST or None, instance=QshowEnter)
                if form.is_valid():
                    try:
                        form.save()
                        QshowEnter.Question_show = Qshow
                        QshowEnter.save()
                        request.session['impomessage'] = 'Question update sucess!'
                        return redirect('QuestionsReview')
                    except Exception as e:
                        print('An exception occurred', e)
                else:
                    messages.error(request, 'Check fields carefully!')
                    # print('notvalid2')#.important in terms of error check
            except Exception as e:
                print('dashBD_Question2', e)

    return render(request, 'admin_portal/components/QuestionsAddAlter.html', context)


@login_required
def dashBD_ArticlesReview(request):
    context = filter_member_data(request.session.get('logUser'), "Areview")

    if request.session.get('impomessage'):
        messages.success(request, request.session.get('impomessage'))
        # messages.warning(request, request.session.get('impomessage'))
        # messages.error(request, request.session.get('impomessage'))
        # messages.info(request, request.session.get('impomessage'))
        del request.session['impomessage']
    return render(request, 'admin_portal/components/ArticlesReview.html', context)


@login_required
def dashBD_ArticleAddAlter(request, data):
    context = {}
    if data == request.session.get('logUser'):
        context = grab_for_Aform(request.session.get('logUser'))
        if request.method == 'POST':
            form = AddorUpdateArticle(request.POST)
            try:
                Ahead = request.POST.get('Article_Heading')
                if form.is_valid():
                    try:
                        Article_data.objects.get(Article_Heading=Ahead)
                        print("Article Exist")
                    except Exception as e:
                        form.save()
                        request.session['impomessage'] = 'Article add sucess!'
                        print('An exception occurred', e)
                        return redirect('ArticlesReview')
                else:
                    messages.error(request, 'Check fields carefully!')
                    print('notvalid 1')
            except Exception as e:
                print('dashBD_Article', e)

    elif (isinstance(data, int)):
        context = grab_for_Aform(request.session.get('logUser'), data)
        if request.method == 'POST':
            try:
                AheadEnter = Article_data.objects.get(
                    Article_Id=data)
                form = AddorUpdateArticle(
                    request.POST or None, instance=AheadEnter)
                if form.is_valid():
                    try:
                        form.save()
                        request.session['impomessage'] = 'Article update sucess!'
                        return redirect('ArticlesReview')
                    except Exception as e:
                        print('An exception occurred', e)
                else:
                    messages.error(request, 'Check fields carefully!')
                    print('notvalid 2')
            except Exception as e:
                print('dashBD_Article', e)
    return render(request, 'admin_portal/components/ArticlesAddAlter.html', context)


@login_required
def TopicSubjectCourse(request):
    context = grabBasicToAll(request.session.get('logUser'), 'CST')

    print(request.POST)
    try:
        if request.POST.get('addCourse'):
            form = AddCourse(request.POST)
            try:
                course = Courses_Exams.objects.get(Exam_Type=request.POST.get('Exam_Type'))
                form = AddCourse(request.POST or None, instance=course)
                messages.success(request, f'{request.POST.get("Exam_Type")} Course Succesfully Updated!')
            except Exception as e:
                print('An exception occurred',e)
                messages.success(request, f'In Courses {request.POST.get("Exam_Type")} Succefully Added!')
                
            if form.is_valid():
                form.save()
                return redirect('TopicSubjectCourse')
            else:
                context["Cform"] = AddCourse(request.POST)
                messages.error(request, 'In Course you did some error in Adding or updating')

        elif request.POST.get('addSubject'):
            form = AddSubject(request.POST)
            try:
                subject=Subjects_toStudy.objects.get(Subj_Type=request.POST.get('Subj_Type'))
                form = AddSubject(request.POST or None, instance=subject)
                messages.success(request, f'{request.POST.get("Subj_Type")} Subject Succesfully Updated!' )
            except Exception as e:
                print('An exception occurred',e)
                messages.success(request, f'In Subjects {request.POST.get("Subj_Type")} Succefully Added!')

            if form.is_valid():
                form.save()
            else:
                context["Sform"] = AddSubject(request.POST)
                messages.error(request, 'In subject you did some error in Adding or updating')

        elif request.POST.get('addTopic'):
            form = AddTopics(request.POST)
            try:
                topic=Topics_comes.objects.get(Topic_Type=request.POST.get('Topic_Type'))
                form = AddTopics(request.POST or None, instance=topic)
                messages.success(request, f'{request.POST.get("Topic_Type")} Topic Succesfully Updated!')
            except Exception as e:
                print('An exception occurred',e)
                messages.success(request, f'In Topics {request.POST.get("Topic_Type")} Succefully Added!')

            if form.is_valid():
                form.save()
            else:
                context["Cform"] = AddCourse(request.POST)
                messages.error(request, 'In Topic you did some error in Adding or updating')
                
        elif request.POST.get('update'):
            print(request.POST)
            context = grabBasicToAll(request.session.get('logUser'),request.POST.get('update'),request.POST.get('updateChoice'))

    except Exception as e:
        print('An exception occurred', e)

    return render(request, 'admin_portal/components/TopicSubjectCourse.html', context)


@login_required
def MembersData(request):
    spUser = User.objects.get(username=request.session.get('logUser'))
    users = User.objects.all()
    context = {"members": users, "user": spUser}
    if request.GET.get('getmember'):
        print(request.GET.get('getmember'))
        data = filter_member_data(request.GET.get('getmember'),
                                  "memberALL")
        context["member_ques"] = data["member_ques"]
        context["member_artcls"] = data["member_artcls"]
        context["member_subj"] = data["member_subj"]
        context["member_tpcs"] = data["member_tpcs"]

    return render(request, 'admin_portal/components/members.html', context)


@login_required
def UserUploads(request):

    if request.method == 'POST':
        form = UploadFile(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST.get('Image_Title')
            try:
                ImageUplaod.objects.get(Image_Title=title)
                messages.error(request, 'Title already Exist')
            except:
                form.save()
                messages.success(request, 'File upload sucess!')
                print('An exception occurred')
        else:
            print('not valid!')
    user = User.objects.get(username=request.session.get('logUser'))
    defaults = {"Creater_Id": user.id}
    context = {
        "userUploads": user.imageuplaod_set.all(),
        "UploadFile": UploadFile(initial=defaults)
    }
    return render(request, 'admin_portal/components/UserUploads.html', context)


@login_required
def All_cstptg(request):
    if request.method == 'GET':

        # Sending an success response
        # print

        try:
            data = ['nothing']
            user = User.objects.get(username=request.session.get('logUser'))
            if request.GET.get('data') == 'cstp':
                return JsonResponse({"data": course_subject_topic_all(), "user": user.id})
            if request.GET.get('data') == 'tg':
                return JsonResponse({"data": tag_all(), "user": user.id})
        except Exception as e:
            print('An exception occurred', e)
            return JsonResponse({"data": '', "user": user.id})
    else:
        return JsonResponse({"sucess": "Request method is not a GET"})
