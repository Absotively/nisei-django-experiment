from django.db import models
from tinymce import models as tinymce_models
from django.conf import settings
from django.utils import translation
import datetime


class LivePostsManager(models.Manager):
  def get_queryset(self):
    return super().get_queryset().filter(publish=True).filter(publication_date__lte=datetime.datetime.now())

class Post(models.Model):
  publish = models.BooleanField()
  publication_date = models.DateTimeField()
  slug = models.SlugField(unique=True)

  objects = models.Manager()
  live_posts = LivePostsManager()

  def __str__(self):
    # TODO: get the full list of translations once only & look through it
    t = self.posttranslation_set.get(language=translation.get_language())
    if t is None:
      t = self.posttranslation_set.get(language=settings.LANGUAGE_CODE)
    if t is None:
      t = self.posttranslation_set.all()[0]

    if t:
      return t.title
    else:
      return "[Titleless post - %s]" % (publication_date)

class PostTranslation(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  language = models.CharField(max_length=10,choices=settings.LANGUAGES)
  title = models.CharField(max_length=512)
  slug = models.SlugField()
  body = tinymce_models.HTMLField()

  class Meta:
    unique_together = (("language","slug"),("language","post"))

  def __str__(self):
    return "%s (%s)" % (self.title, self.language)
