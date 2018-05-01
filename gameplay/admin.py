from django.contrib import admin

from .models import Game, Move

# admin.site.register(Game)
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    #DATA display on TABLE GRID Formate
    list_display = ('id', 'first_player', 'second_player', 'status')
    #editable fiels STATUS,
    list_editable = ('status', )

admin.site.register(Move)
