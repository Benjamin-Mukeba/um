from django.contrib import admin
from student.models import Student

class StudentA(admin.ModelAdmin):
    list_display = ('nom', 'postnom', 'prenom', 'sexe', 'email', 'lieu_naissance', 'date_naissance', 'Etat_civil', 'adresse', 'faculte', 'departement', 'promotion', 'annee_academique', 'registration_date')
    list_filter = ('nom', 'postnom', 'prenom','registration_date',)
    search_fields = ('nom', 'postnom', 'prenom',)

# Register your models here.
admin.site.register(Student, StudentA)

admin.site.site_header = "Student Registration"
