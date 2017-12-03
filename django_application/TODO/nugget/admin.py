from django.contrib import admin

# Register your models here.
from .models import Profile, Nugget, NuggetAttribute, Inventory, Item, Friend, Battle, BattleInstance, Shop, InventoryItems, News


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'usr', 'bday', 'coins')

@admin.register(Battle)
class BattleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'item_status', 'item_features')


@admin.register(InventoryItems)
class InventoryItemsAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'inventory')

class InventoryInline(admin.TabularInline):
    model = InventoryItems

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'id')
    inlines = [InventoryInline]

@admin.register(BattleInstance)
class BattleInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'opp_a', 'opp_b')

@admin.register(Nugget)
class NuggetAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('text',)

admin.site.register(NuggetAttribute)
admin.site.register(Shop)
admin.site.register(Friend)
