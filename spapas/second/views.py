from django.shortcuts import render
from django.http import HttpResponse
import json

class JsonCustomClassView:
    def get_header(self,):
        return self.header if self.header else ""
    def get_context(self,):
        return self.context if self.context else []

    @classmethod
    def as_view(cls,*args,**kwargs):
        def view(request,):
            instance = cls(**kwargs)
            return HttpResponse(json.dumps{
                'header':instance.get_header(),
                'context':instance.get_context()
            })
        return view