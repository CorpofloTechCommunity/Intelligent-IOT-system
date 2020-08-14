from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Farm(models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=50,
        unique=True
    )
    slug = models.SlugField(
        verbose_name=_('slug'),
        blank=True
    )
    ph = models.DecimalField(
        verbose_name=_('soil pH'),
        max_digits=2,
        decimal_places=1
    )
    speed = models.IntegerField(
        verbose_name=_('wind speed'),
    )
    humidity = models.PositiveSmallIntegerField(
        verbose_name=_('humidity'),
    )
    soil_content = models.IntegerField(
        verbose_name=_('soil water content'),
    )
    pressure = models.PositiveSmallIntegerField(
        verbose_name=_('air pressure')
    )
    temperature = models.DecimalField(
        verbose_name=_('temperature'),
        max_digits=3,
        decimal_places=2
    )
    created = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'slug'],
                name='unique_name_slug'
            )
        ]
        ordering = ['name']
