__author__ = 'lundberg'

from django.contrib import admin
from apps.event.models import Country, Event, Entity, DailyEventAggregation
from apps.event.models import EduroamEvent, EduroamRealm, DailyEduroamEventAggregation


class CountryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Country, CountryAdmin)


class EventAdmin(admin.ModelAdmin):
    date_hierarchy = 'ts'
    list_display = ('ts', 'origin', 'rp', 'protocol')
    list_filter = ('protocol', 'origin', 'rp')

admin.site.register(Event, EventAdmin)


class DailyEventAggregationAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('date', 'origin_name', 'rp_name', 'num_events', 'protocol')
    list_filter = ('protocol',)

admin.site.register(DailyEventAggregation, DailyEventAggregationAdmin)


class EntityAdmin(admin.ModelAdmin):
    pass

admin.site.register(Entity, EntityAdmin)


class EduroamEventAdmin(admin.ModelAdmin):
    date_hierarchy = 'ts'
    list_display = ('ts', 'realm', 'visited_country', 'visited_institution', 'calling_station_id', )
    list_filter = ('successful',)

admin.site.register(EduroamEvent, EduroamEventAdmin)


class DailyEduroamEventAggregationAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ('date', 'realm_country', 'realm', 'visited_country', 'visited_institution', 'calling_station_id')
    list_filter = ('realm_country', 'visited_country',)

admin.site.register(DailyEduroamEventAggregation, DailyEduroamEventAggregationAdmin)


class EduroamRealmAdmin(admin.ModelAdmin):
    list_display = ('realm', 'name', 'country')
    list_filter = ('country',)

admin.site.register(EduroamRealm, EduroamRealmAdmin)