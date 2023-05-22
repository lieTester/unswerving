from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator, validate_image_file_extension
from django.db import models
from ckeditor.fields import RichTextField
# import uuid
# Create your models here.

# no of tags comes under subjects


class Tags_toMatch(models.Model):
    Tag_Id = models.AutoField(primary_key=True)
    Tag_Type = models.CharField(max_length=100)
    Tag_Add_Time = models.DateField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.Tag_Type

# no of topic comes under subjects


class Topics_comes(models.Model):
    Topic_Id = models.AutoField(primary_key=True)
    Topic_Type = models.CharField(max_length=100)
    Topic_slug = models.SlugField(max_length=200)
    Topic_Desc=RichTextField(default='Add Topic Description')
    Topic_Add_Time = models.DateField(auto_now_add=True, auto_now=False)
    Topic_Update_Time = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.Topic_Type


# the subjrcts comes under the courses
class Subjects_toStudy(models.Model):
    Subj_Id = models.AutoField(primary_key=True)
    Subj_Type = models.CharField(max_length=100)
    Topic_Id = models.ManyToManyField(Topics_comes)
    Subj_Desc=RichTextField(default='Add Subject Description')
    Subj_Add_Time = models.DateField(auto_now_add=True, auto_now=False)
    Subj_Update_Time = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.Subj_Type


# the class model related to the no of courses we having
file_validate = ['svg', 'blp', 'bmp', 'dib', 'bufr', 'cur', 'pcx', 'dcx', 'dds', 'ps', 'eps', 'fit', 'fits', 'fli', 'flc', 'ftc', 'ftu', 'gbr', 'gif', 'grib', 'h5', 'hdf', 'png', 'apng', 'jp2', 'j2k', 'jpc', 'jpf', 'jpx', 'j2c', 'icns', 'ico', 'im',
                 'iim', 'tif', 'tiff', 'jfif', 'jpe', 'jpg', 'jpeg', 'mpg', 'mpeg', 'mpo', 'msp', 'palm', 'pcd', 'pdf', 'pxr', 'pbm', 'pgm', 'ppm', ' pnm', 'psd', 'bw', 'rgb', 'rgba', 'sgi', 'ras', ' tga', 'icb', 'vda', 'vst', 'webp', 'wmf', 'emf', 'xbm', 'xpm']


class Courses_Exams(models.Model):
    Exam_Id = models.AutoField(primary_key=True)
    Subj_Id = models.ManyToManyField(Subjects_toStudy)
    Exam_Type = models.CharField(max_length=100)
    Exam_Image = models.FileField(upload_to='course/',
                                  validators=[FileExtensionValidator(allowed_extensions=file_validate)], default="/learn-2.svg")
    Exam_shortForm = models.CharField(max_length=100, default=" ")
    Exam_Desc = RichTextField(default='Add Course Description')
    Exam_Add_Time = models.DateField(auto_now_add=True, auto_now=False)
    Exam_Update_Time = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.Exam_Type


# quetions we have related to multiple topics comes under diffrent courses
class Question_data(models.Model):
    Question_Id = models.AutoField(primary_key=True)
    Topic_Id = models.ManyToManyField(Topics_comes)
    Exam_Id = models.ManyToManyField(Courses_Exams)
    Creater_Id = models.ForeignKey(User, on_delete=models.CASCADE)
    Question_show = models.CharField(max_length=1000, default='?')
    Question_detail = RichTextField()
    Question_Options = models.CharField(max_length=100)
    Question_Correct_Option = models.CharField(max_length=50)
    Question_Ans_Explain = RichTextField()
    Question_Add_Time = models.DateField(auto_now_add=True, auto_now=False)
    Question_Update_Time = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.Question_show


def user_directory_path(instance, filename):

    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'article/user_{0}/{1}'.format(instance.Creater_Id.username, filename)


class ImageUplaod(models.Model):
    Image_Id = models.AutoField(primary_key=True)
    Creater_Id = models.ForeignKey(User, on_delete=models.CASCADE)
    Image_Title = models.CharField(max_length=1000, default='')
    Image_Name = models.ImageField(upload_to=user_directory_path)

    def __str__(self):
        return self.Image_Title


class Article_data(models.Model):
    Article_Id = models.AutoField(primary_key=True)
    Tag_Id = models.ManyToManyField(Tags_toMatch)
    Creater_Id = models.ForeignKey(User, on_delete=models.CASCADE)
    Article_Heading = models.CharField(max_length=4000, default=' ')
    Article_detail = RichTextField()
    Article_Add_Time = models.DateField(auto_now_add=True, auto_now=False)
    Article_Update_Time = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.Article_Heading
