from django.shortcuts import render, redirect
from django.views.generic import View
from . import models
from . import forms


class ChatView(View):

    def get(self, request):
        form = forms.MessageForm()
        messages = models.Message.objects.all().order_by('sent')
        return render(request, 'Chat/chat.html', {
            'form': form,
            'messages': messages,
        })

    def post(self, request):
        form = forms.MessageForm(request.POST, request.FILES)
        if form.is_valid():
            text = form.cleaned_data['text']
            img = form.cleaned_data['image']
            message = models.Message.objects.create(author=request.user, text=text, image=img)
            return redirect('/chat#id_text')
        else:
            return redirect('/chat#id_text')
