from django.shortcuts import render, redirect, get_object_or_404


class ObjectDetailMixin:
    model = None
    template = None
    context = {}

    def get(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        self.context = {
            self.model.__name__.lower(): obj,
        }
        return render(request, self.template, self.context)

class ObjectEditMixin:
    model_form = None
    template = None
    context = {}

    def get(self, request, pk):
        pass

    def post(self, request, pk):
        pass

class ObjectCreateMixin:
    model_form = None
    template = None
    context = {}

    def get(self, request, pk):
        pass

    def post(self, request, pk):
        pass
