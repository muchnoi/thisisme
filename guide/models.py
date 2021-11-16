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
    ordering = ["order"] # defines order of items
    
  def get_absolute_url(self):
    return ('%s' % self.name)

  def get_description(self):
    if   'Tuto' in self.name: return 'Materials for students: tutorials and textbooks on optics, etc.'
    elif 'Publ' in self.name: return 'Selected scientific papers that are most important to me personally.'
    elif 'Slid' in self.name: return 'A collection of slides I have ever prepared for conferences, workshops, seminars, etc.'
    elif 'Thes' in self.name: return 'Here are my qualification works.'
    elif 'Draf' in self.name: return 'Incomplete or unpublished studies which however I do not want to forget.'
    elif 'Soft' in self.name: return 'Here are the (Github) links to software projects developed by myself.'
    elif 'Link' in self.name: return 'Some other links to the resources that I visit sometimes.'
 
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
  summary = models.TextField(max_length=500, blank=True, null=True, help_text="A brief description of the reference")
  itype   = models.ForeignKey(ReferenceType, on_delete=models.SET_NULL, null=True)
  year    = models.PositiveIntegerField(default=1970, blank=True, null=True)
  upload  = models.FileField(upload_to='static/', default = '', blank=True, null=True)
  exturl  = models.URLField(default = '', blank=True, null=True)
  
  class Meta:
    ordering = ["-year", "title"]

  def get_absolute_url(self):
      """
      Returns the url to access a particular  instance.
      """
      if self.upload:
        return reverse('view-pdf', args=[str(self.id)])
      else:
        return self.exturl

  def __str__(self):
      """
      String for representing the Model object.
      """
      return self.title


