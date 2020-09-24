from django.contrib import admin

# Register your models here.
from sqlorders import models


@admin.register(models.DbConfig)
class DbConfigAdmin(admin.ModelAdmin):
    list_display = ('host', 'port', 'character', 'env_id', 'use_type', 'rds_type', 'rds_category')
    list_display_links = ('host',)
    search_fields = ('host', 'port', 'env_id')
    list_per_page = 10


@admin.register(models.DbSchemas)
class DbSchemasAdmin(admin.ModelAdmin):
    list_display = ('cid', 'schema', 'created_at')
    list_display_links = ('cid',)
    search_fields = ('cid__host', 'schema')
    list_per_page = 10


@admin.register(models.DbEnvironment)
class DbEnvironmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_per_page = 10
