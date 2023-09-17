from django.shortcuts import get_list_or_404, render ,redirect
from django.views.generic import View


class BlogListView(View):
    def get(self,request,*args, **kwargs):
        context={}
        return render (request,'blog_list.html',context)