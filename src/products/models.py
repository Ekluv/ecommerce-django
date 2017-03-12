from django.db import models
from django.db.models import Q
from django.core.urlresolvers import reverse


class ProductManager(models.Manager):
    def all(self, **kwargs):
        return self.filter(active=True, **kwargs)

    def get_related_products(self, instance):
        qs1 = self.all().filter(categories__in=instance.categories.all())
        qs2 = self.all().filter(default=instance.default)
        return (qs1 | qs2).exclude(id=instance.id).distinct()


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    categories = models.ManyToManyField('Category', blank=True)
    default = models.ForeignKey('Category', related_name='default_category', null=True, blank=True)
    # slug
    objects = ProductManager()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=(self.id,))

    def get_image_url(self):
        img = self.productimage_set.first()
        return img.image.url if img else img


    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        if self.variation_set.all().count() == 0:
            Variation.objects.create(product=self, price=self.price, title='Default')
        


class Variation(models.Model):
    product = models.ForeignKey(Product)
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    sale_price = models.PositiveIntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
    inventory = models.IntegerField(null=True, blank=True) # None is unlimited

    def __unicode__(self):
        return self.title

    def get_price(self):
        """
        return sale price if not None otherwise return prices
        """
        return self.sale_price if self.sale_price else self.price

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def get_title(self):
        return '{0}- {1}'.format(self.product.title, self.title)

    def add_to_cart(self):
        return '{0}?item={1}'.format(reverse('create_cart'), self.id)

    def remove_from_cart(self):
        return '{0}&{1}'.format(self.add_to_cart(), 'delete=y')


class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to='products/', null=True)

    def __unicode__(self):
        return self.product.title


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class ProductFeatured(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to='products/featured/')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400, blank=True, null=True)
    description_right = models.BooleanField(default=False)
    show_price = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.product.title
