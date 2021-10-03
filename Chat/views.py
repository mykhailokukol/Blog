from django.shortcuts import render, redirect
from django.views.generic import View
# from django.core.exceptions import
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
            try:
                message = models.Message.objects.create(author=request.user, text=text, image=img, anonymous_author=request.session.session_key)
            except ValueError:
                message = models.Message.objects.create(anonymous_author=request.session.session_key, text=text, image=img)
            return redirect('/chat#id_text')
        else:
            return redirect('/chat#id_text')

class MessageEditView(View):

    def get(self, request, pk):
        edit_form = forms.MessageForm()
        messages = models.Message.objects.all().order_by('sent')
        return render(request, 'Chat/chat.html', {
            'edit_form': edit_form,
            'messages': messages,
            'pk': pk,
        })

    def post(self, request, pk):

        edit_form = forms.MessageForm(request.POST, request.FILES)
        if edit_form.is_valid():
            text = edit_form.cleaned_data['text']
            img = edit_form.cleaned_data['image']
            message = models.Message.objects.get(pk=pk)
            message.text = text
            message.image = img
            message.save()
            return redirect('/chat#id_text')
        else:
            return redirect('/chat#id_text')
