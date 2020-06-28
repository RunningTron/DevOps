import os

from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from web import settings
from django.http import FileResponse
# Create your views here.

class Index(View):
    def get(self,request):
        return render(request,template_name="index.html")
    def post(self,request):
        print(request.POST)

        return HttpResponse("app.index.post")

class UploadImg(View):
    def get(self,request):
        return redirect("app01:index")
    def post(self,request):
        print(request.POST)
        print("file",request.FILES)
        cover = request.FILES.get('img_name')  # 获取文件对象
        print(cover,cover.__dict__)
        with open(os.path.join(settings.STATICFILES_DIRS[0],cover.name),"wb")as f:
            for chunk in cover.chunks():
                f.write(chunk)
        return redirect("app01:index")
    # 文件信息保存到数据库 自动就会将文件上传到我们配置的uploadfiles文件夹中

class Download(View):
    def get(self,request):
        file = open(os.path.join(settings.STATICFILES_DIRS[0], "image","1.png"), "rb")
        print(file)
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="1.png"'
        return response
    def post(self,request):
        return HttpResponse(request,"Download.pass")


class Base(View):
    def get(self,request):
        return render(request,"base.html")