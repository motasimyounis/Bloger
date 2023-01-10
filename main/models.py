from django.db import models

# Create your models here.

class New(models.Model):
    type_post = [
        ('News','News'),
        ('Blogs','Blogs'),
    ]
    choices= [
        ('اقتصاد','اقتصاد'),
        ('رياضة','رياضة'),
        ('صحةوجمال','صحةوجمال'),
        ('تكنولوجيا','تكنولوجيا'),
        ('خبر','خبر')
    ]
     
    title = models.CharField(max_length=100,unique=True)
    author = models.CharField(max_length=20,null=True, blank=True)
    image = models.ImageField()
    date_post = models.DateField(null=True, blank=True)
    short_decsription = models.CharField(max_length=100)
    long_decsription = models.TextField(default='DESC')
    type = models.CharField(max_length=50, choices=type_post,default='Blogs')
    most_popular = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)
    main = models.BooleanField(default=False)
    main2 = models.BooleanField(default=False)
    cate = models.CharField(choices=choices,max_length=12)




    def __str__(self):
        return f"{self.id} {self.title} "




