from django.contrib import admin

from .models import Post, PostTranslation

class PostTranslationInline(admin.StackedInline):
  model = PostTranslation
  prepopulated_fields = {"slug": ("title",)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  inlines = [
    PostTranslationInline,
  ]
