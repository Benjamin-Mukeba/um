from django.db import models
#zfrom django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    sexe_list = (('M', 'Masculin'), ('F', 'Feminin'))
    etat_list = (('C', 'CELIBATAIRE'), ('M', 'MARIE'), ('D', 'DIVORCE'), ('V', 'VEUF'))
    fac_list = (('S', 'SCIENCES APPLIQUEES'), ('M', 'MEDECINE'), ('E', 'ECONOMIE'), ('D', 'DROIT'))
    dep_list = (('I', 'INFORMATIQUE'), ('M', 'MECANIQUE'), ('N', 'MINES'), ('C', 'CONSTRUCTION'))
    prom_list = (('1', 'G1'), ('2', 'G2'), ('3', 'G3'), ('4', 'L1'), ('5', 'L2'))
    nom = models.CharField(max_length=55)
    postnom = models.CharField(max_length=55)
    prenom = models.CharField(max_length=55)
    lieu_naissance = models.CharField(max_length=55)
    date_naissance = models.DateField()
    sexe = models.CharField(max_length=1, choices=sexe_list)
    Etat_civil = models.CharField(max_length=1, choices=etat_list)
    email = models.EmailField()
    adresse = models.CharField(max_length=155)
    nom_pere = models.CharField(max_length=55)
    nom_mere = models.CharField(max_length=55)
    diplome_pourcent = models.IntegerField()
    diplome_option = models.CharField(max_length=55)
    registration_date = models.DateTimeField(auto_now_add=True)
    faculte = models.CharField(max_length=1, choices=fac_list)
#    if faculte == 'SCIENCES APPLIQUEES':
#        dep_list = (('I', 'INFORMATIQUE'), ('M', 'MECANIQUE'), ('N', 'MINES'), ('C', 'CONSTRUCTION'))
#    elif faculte == 'MEDECINE':
#        dep_list = (('M', 'MEDECINE GENERALE'))
#    elif faculte == 'ECONOMIE':
#        dep_list = (('A', 'ECONOMIE APPLIQUEE'), ('B', 'ECONOMIE FINANCIERE'))
#    else:
#        dep_list = (('A', 'DROIT PRIVE'), ('B', 'DROIT PUBLIC'))
    departement = models.CharField(max_length=1, choices=dep_list)
    promotion = models.CharField(max_length=1, choices=prom_list)
    annee_academique = models.CharField(max_length=55)

    def save(self, *args, **kwargs):
        super(Student, self).save(*args, **kwargs)

    class Meta:
        ordering = ['registration_date']

        def __unicode__(self):
            return self.nom
