from django.db   import models
from django.http import FileResponse
from django.urls import reverse

class ReferenceType(models.Model):
  """
  Model representing a category (e.g. Publication, Proceedings, Slides etc.).
  """
  name  = models.CharField(max_length=50,                help_text = "An item type e.g. Publication, Proceedings, Presentation etc.")
  title = models.TextField(max_length=200, default='',   help_text = "An item title as it should appear on the web.")
  order = models.PositiveIntegerField(default=0,         help_text = "The position of this type in the list.")
  decor = models.CharField(max_length=25,  default = '', help_text = "An item decoration unicode symbol.")
  
  class Meta:
    ordering = ["order"] # определяет порядок элементов списка на странице
    
  def get_absolute_url(self):
    return ('%s' % self.name)
 
  def __str__(self):
    """
    String for representing the Model object (in Admin site etc.)
    """
    return self.name
       
       
class Reference(models.Model):
  """
  Model representing one reference item.
  """
  title   = models.CharField(max_length=300)
  summary = models.TextField(max_length=500, help_text="A brief description of the reference")
  itype   = models.ForeignKey(ReferenceType, on_delete=models.SET_NULL, null=True)
  year    = models.PositiveIntegerField(default=1970, blank=True, null=True)
  upload  = models.FileField(upload_to='static/', default = '', blank=True, null=True)
  exturl  = models.URLField(default = '', blank=True, null=True)
  
  class Meta:
    ordering = ["title", "-year"]

  def get_url(self):
      """
      Returns the url to access a particular  instance.
      """
      if self.upload:
        return reverse('view-pdf', args=[str(self.id)])
      elif self.exturl:
        return self.exturl

  def __str__(self):
      """
      String for representing the Model object.
      """
      return self.title


