from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate,login

class PersonaLoginView(View):

    def post(self,request,*args,**kwargs):
        print('ASSERTION',request.POST.get('assertion'))
        user = authenticate(assertion=request.POST.get('assertion'))
        if user is not None:
            login(request,user)
            print("persona login", user, user.is_authenticated())

        return HttpResponse(user.username)
