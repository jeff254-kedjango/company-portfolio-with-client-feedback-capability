from unicodedata import category
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from .utils import unique_slug_generator
from django.db.models.signals import pre_save


def upload_to(instance, filename):
    return 'media/{filename}'.format(filename=filename)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class NutritionCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    post_image = models.ImageField(
        _('Image'), upload_to=upload_to, default='media/default.jpg', blank=True, null=True)
    inline_image = models.ImageField(
        _('Image'), upload_to=upload_to, default='media/default.jpg', blank=True, null=True)
    video = models.FileField(upload_to=upload_to, null=True, blank=True, validators=[
                             FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    content = models.TextField()
    slug = models.SlugField(max_length=250, blank=True, null=True)
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(
        max_length=10, choices=options, default='published')
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


class Feedback(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    message = models.TextField()
    published = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.firstname


class Projects(models.Model):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(ProjectCategory, on_delete=models.PROTECT)
    post_image = models.ImageField(
        _('Image'), upload_to=upload_to, default='media/default.jpg', blank=True, null=True)
    description = models.TextField()
    inline_image = models.ImageField(
        _('Image'), upload_to=upload_to, default='media/default.jpg', blank=True, null=True)
    video = models.FileField(upload_to=upload_to, null=True, blank=True, validators=[
                             FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    slug = models.SlugField(max_length=250, blank=True, null=True)
    published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


class Nutrition(models.Model):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(NutritionCategory, on_delete=models.PROTECT)
    post_image = models.ImageField(
        _('Image'), upload_to=upload_to, default='media/default.jpg', blank=True, null=True)
    description = models.TextField()
    inline_image = models.ImageField(
        _('Image'), upload_to=upload_to, default='media/default.jpg', blank=True, null=True)
    slug = models.SlugField(max_length=250, blank=True, null=True)
    published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Post)
pre_save.connect(slug_generator, sender=Projects)
pre_save.connect(slug_generator, sender=Nutrition)
