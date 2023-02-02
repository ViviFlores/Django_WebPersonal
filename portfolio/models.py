from tabnanny import verbose
from venv import create
from django.db import models

# Create your models here.


class Project(models.Model):  # heredando de la clase Model que brinda Django
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    link = models.URLField(null=True, blank=True, verbose_name="Enlace")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edición")

    class Meta:  # modificiaciones extendidas del modelo
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self):  # retornar en forma de string la información del objeto
        return self.title
