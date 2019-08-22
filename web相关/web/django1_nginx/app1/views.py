from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

import os

# Create your views here.
def demo(request):
    return render(request,'home.html')
def home(request):
    return render(request,'home.html')


def data1(request):
    return HttpResponse("abc data1 response")

def test1(request):
    return HttpResponse(request,'test1.html')


def upfile(request):
    if request.method == 'POST':
#        dir_path=os.path.dirname(os.path.abspath(file))
        #dir_path='/root/files/data/'
        dir_path='/var/www/files/data/'
#        dir_path='/var/www/django1_nginx/static/'
        print(dir_path)
        for file in request.FILES:
            data=request.FILES.get(file)
            file_path=os.path.join(dir_path,file)
            print(file_path)
            with open(file_path,'wb') as f:
                f.write(data.read())

    response = JsonResponse({"status":'39.104.218.125:80/files/data/'})
    return response
