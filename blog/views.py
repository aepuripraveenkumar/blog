from django.views import generic

from .models import Category, Entry


class BaseEntryView(object):
    date_field = 'pub_date'
    model = Entry


class BaseCategoryView(object):
    model = Category


class EntryArchiveIndex(BaseEntryView, generic.ArchiveIndexView):
    pass


class EntryArchiveYear(BaseEntryView, generic.YearArchiveView):
    make_object_list = True


class EntryArchiveMonth(BaseEntryView, generic.MonthArchiveView):
    pass


class EntryArchiveDay(BaseEntryView, generic.DayArchiveView):
    pass


class EntryDetail(BaseEntryView, generic.DateDetailView):
    pass


class CategoryList(BaseCategoryView, generic.ListView):
    pass


class CategoryDetail(BaseCategoryView, generic.DetailView):
    pass
