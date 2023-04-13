from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model


def get_sentinel_user(): # sayfanin ustunde bir yerde yazabilirsiniz.
    return get_user_model().objects.get_or_create(username='deleted', )[0]

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.SET(get_sentinel_user), verbose_name='Yazar',related_name='posts')
    title = models.CharField(max_length=120, verbose_name='başlık')
    content = RichTextField(verbose_name='İçerik')
    publishing_date = models.DateTimeField(verbose_name='yayınlanma tarihi', auto_now_add=True)
    image = models.FileField(null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'slug':self.slug})
        #return "/past/{}".format(self.id);

    def get_create_url(self):
        return reverse('post:create')
    def get_update_url(self):
        return reverse('post:update', kwargs={'slug':self.slug})
    def get_delete_url(self):
        return reverse('post:delete', kwargs={'slug':self.slug})

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        sayac = 1
        while Post.objects.filter(slug=unique_slug):
            unique_slug = '{}-{}'.format(slug, sayac)
            sayac += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_unique_slug()
        return super(Post, self).save(*args,**kwargs)

    class Meta:
        ordering = ['-publishing_date', 'id']

class Comment(models.Model):
        post = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='comments')
        name = models.CharField(max_length=200, verbose_name='Ad Soyad')
        content = models.TextField(verbose_name='Yorum')

        created_date = models.DateTimeField(auto_now_add=True)
