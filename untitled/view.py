#from django.http import  HttpResponse
from django.shortcuts import  render     #返回一个网页给用户

def home(request):  #用户发出的请求
    return render(request,'home.html ')     #得到请求后返回一个网页给用户

def count(request):
    user_text = request.GET['text']
    total_count = len(user_text)

    #统计出现次数
    word_dict = {}  #创建空字典
    for word in user_text:
        if word not in word_dict:   #判断字是否在字典里面
            word_dict[word] = 1     #如果没有就将这个字放到字典中，键为字 值为 次数
        else:
            word_dict[word] += 1
    #排序
    sort_dict = sorted(word_dict.items(),key=lambda w:w[1],reverse = True )
    return render(request, 'count.html',
                  {'tongji':total_count,
                   'text':user_text,
                   'sort':sort_dict}) #使用字典，将值传到html中


def about(request):  #用户发出的请求
    return render(request,'about.html')