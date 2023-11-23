
from django.db import models

from apps.series.models import Serie, Temporada
# Create your models here.


def upload_to(instance, filename):
    """Define la ruta donde se guardan las imagenes de los videos 

    Args:
        instance (_type_): _description_
        filename (_type_): nombre del archivo imagen

    Returns:
        path: ruta en donde se guarda la imagen
    """    
    return 'videos/{filename}'.format(filename=filename)

#class Palabras_claves(models.Model):
#    
#    palabra = models.CharField(max_length=45)
#    class Meta:
#
#        verbose_name = 'Palabra clave'
#        verbose_name_plural = 'Palabras clave'
#
#    def __str__(self):
#        return self.palabra
class palabrasClaves(models.Model):
    palabrasClaves = models.CharField('Palabras Claves', max_length=50)

    class Meta:
        """Meta definition for palabras claves."""

        verbose_name = 'palabrasclaves'
        verbose_name_plural = 'palabrasclaves'

    def __str__(self):
        """Unicode representation of palabras claves."""
        return self.palabrasClaves
    
class Keywords(models.Model):

    keyword = models.CharField(max_length=45)

    def __str__(self):
        return self.keyword
    class Meta:

        verbose_name = 'Keyword'
        verbose_name_plural = 'Keywords'

class Categoria(models.Model):
    categoria = models.CharField('Categoria', max_length=50)

    class Meta:
        """Meta definition for Categoria."""

        verbose_name = 'Categoria del video'
        verbose_name_plural = 'Categorias del video'

    def __str__(self):
        """Unicode representation of Categoria."""
        return self.categoria

class Especialidad(models.Model):
    especialidad = models.CharField('Especialidad', max_length=50)

    class Meta:
        """Meta definition for Especialidad."""

        verbose_name = 'Especialidad del video'
        verbose_name_plural = 'Especialidades del video'

    def __str__(self):
        """Unicode representation of Especialidad."""
        return self.especialidad
    
class subEspecialidad(models.Model):
    subEspecialidad = models.CharField('Sub Especialidad', max_length=50)

    class Meta:
        """Meta definition for subEspecialidad."""

        verbose_name = 'Subespecialidad del video'
        verbose_name_plural = 'Subespecialidades del video'

    def __str__(self):
        """Unicode representation of subEspecialidad."""
        return self.subEspecialidad
    


class Idioma(models.Model):
    language = models.CharField('Idioma', max_length=50)

    class Meta:
        """Meta definition for Idioma."""

        verbose_name = 'language del video'
        verbose_name_plural = 'languages del video'

    def __str__(self):
        """Unicode representation of Idioma."""
        return self.language

class tipoVideo(models.Model):
    tipe_video = models.CharField('Tipo de video', max_length=50)

    class Meta:
        """Meta definition for tipoVideo."""

        verbose_name = 'Tipo del video'
        verbose_name_plural = 'Tipos de video'

    def __str__(self):
        """Unicode representation of tipoVideo."""
        return self.tipe_video

class Video(models.Model):
    code_esp = models.CharField('Código del video en español de vimeo', max_length=150, null=True,blank= True)
    code_engl = models.CharField('Código del video en ingles de vimeo', max_length=150, null=True,blank= True)
    title_espanol = models.CharField('Titulo en español', max_length=100)
    title_english = models.CharField('Titulo en ingles', max_length=100)
    title_cap_esp = models.CharField('Titulo del capitulo en español', max_length=150, blank= True, null=True)
    title_cap_english = models.CharField('Titulo del capitulo en ingles', max_length=150, blank= True, null=True)
    description_esp = models.TextField('Descripción en español', blank= True, null=True)
    description_english = models.TextField('Descripción en ingles', blank= True, null=True)
    upload_date = models.DateTimeField('Fecha de subida', auto_now=False, auto_now_add=True)
    create_date = models.DateTimeField('Fecha de creación', blank= True, null=True)
    duration = models.DurationField('Duración',blank= True, null=True)
    featured_image = models.ImageField('Imagen destacada', upload_to=upload_to, null=True, blank=True,height_field=None, width_field=None, max_length=None)
    min_image = models.ImageField('Imagen comprimida', upload_to=upload_to, null=True, blank=True,height_field=None, width_field=None, max_length=None)
    score = models.DecimalField('puntuación', max_digits=3, decimal_places=2, null=True)
    cumulative_score = models.IntegerField('puntuaje acumulado', null=True, blank=True)
    numberOfVotes = models.IntegerField('Cantidad de votos', null=True, blank=True)
    state = models.BooleanField('Estado',default = True)
    tipe_of_video = models.ForeignKey(tipoVideo,on_delete=models.CASCADE, verbose_name='Tipo de video')
    categorias = models.ManyToManyField(Categoria, related_name="Categorias", verbose_name="Categorias")
    especialidad = models.ManyToManyField(Especialidad, related_name="Especialidades", verbose_name="Especialidades")
    subEspecialidad = models.ManyToManyField(subEspecialidad, related_name="subEspecialidades", verbose_name="subEspecialidades")
    languages = models.ManyToManyField(Idioma, related_name="Idiomas", verbose_name='Idiomas')
    palabrasClaves = models.ManyToManyField(palabrasClaves, related_name="palabraslaves", verbose_name='palabras claves', blank=True)
    keywords = models.ManyToManyField(Keywords, related_name="Keywords", verbose_name='Keywords', blank=True)
    temporada = models.ForeignKey(Temporada, verbose_name='Temporada',  on_delete=models.SET_NULL, null=True, blank=True)
    class Meta: 
        """Meta definition for Video."""

        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def get_lenguages_video(self):
        return Idioma.objects.filter(Idiomas = self)

    def get_categories_video(self):
        return Categoria.objects.filter(Categorias = self)
    
    def get_especialidades_video(self):
        return Especialidad.objects.filter(especialidad = self)
    
    def get_subEspecialidades_video(self):
        return subEspecialidad.objects.filter(subEspecialidad = self)
    def get_palabrasClaves_video(self):
        return palabrasClaves.objects.filter(palabrasClaves = self)

    def __str__(self):
        """Unicode representation of Video."""
        return self.title_espanol

class historial_Video(models.Model):
    reproducciones = models.IntegerField(default=0)
    video = models.OneToOneField(Video, on_delete= models.CASCADE)

    def __str__(self):
        return f'{self.id}'
