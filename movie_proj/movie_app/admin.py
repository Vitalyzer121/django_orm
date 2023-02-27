from django.contrib import admin
from .models import Movie, Director, Actor, DressingRoom
from django.db.models import QuerySet

admin.site.register(Director)
admin.site.register(Actor)
#admin.site.register(DressingRoom)

@admin.register(DressingRoom)
class DressingRoom(admin.ModelAdmin):
    list_display = ['floor', 'number', 'actor']


class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('от 40 до 59', 'Средний'),
            ('от 60 до 79', 'Высокий'),
            ('>=80', 'Высочайший'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value()=='40':
            return queryset.filter(rating__lt=40)
        elif self.value()=='от 40 до 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        elif self.value()=='от 60 до 79':
            return queryset.filter(rating__gte=60).filter(rating__lt=80)
        elif self.value()=='80':
            return queryset.filter(rating__gt=80)
        return queryset



@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    #field = оставляет толко прописанные поля
    #exclude = исключает прописанные поля
    #readonly_fields = запрещает редактировать поле
    prepopulated_fields = {'slug':('name', )}
    list_display = ['name', 'rating', 'director', 'budget', 'rating_status']
    list_editable = ['rating', 'director', 'budget']
    ordering = ['rating']
    list_per_page = 5
    filter_horizontal = ['actors']
    actions = ['set_dollars', 'set_euro']
    search_fields = ['name']
    list_filter = ['name', 'currency', RatingFilter]

    @admin.display(ordering = 'rating', description='Статус')
    def rating_status(self, mov : Movie):
        if mov.rating < 50:
            return 'Зачем это смотреть?!'
        if mov.rating < 70:
            return 'Разок можно глянуть'
        if mov.rating <= 85:
            return 'Зачет'
        return 'Топ'

    @admin.action(description='Установить валюту в доллар')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)

    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.USD)
        self.message_user(
            request,
            f'Было обновлено {count_updated} записей'
        )




