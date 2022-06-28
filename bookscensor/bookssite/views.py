from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.list import ListView, View
from django.views.generic.edit import FormMixin, UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView, SingleObjectMixin
from .models import Book, Review
from .forms import ReviewForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = "bookssite/index.html"


class BookDetailView(FormMixin, DetailView):
    model = Book
    template_name = "bookssite/book_detail.html"
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['review_list'] = Review.objects.filter(book=self.get_object())

        return context

    def get_success_url(self):
        return reverse('book_detail', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            obj = form.save(commit=False)
            obj.book = self.object
            obj.user = request.user
            obj.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']

        return super().form_valid(form)


class ReviewUpdate(UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['review', 'rating']
    template_name = "bookssite/review_update.html"

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.user:
            return True
        return False

    def get_success_url(self):
        return reverse('book_detail', kwargs={'pk': self.object.book.id})


class ReviewDelete(UserPassesTestMixin, DeleteView):
    model = Review
    success_url = reverse_lazy('index')

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.user:
            return True
        return False


class BookAdd(CreateView):
    model = Book
    fields = '__all__'
    template_name = "bookssite/add_book.html"
    success_url = '/'