from django.db import models

# Create your models here.
class Materia(models.Model):
    materia=models.CharField(max_length=20)

    def __str__(self):
        return self.materia

class Studente(models.Model):
    nome=models.CharField(max_length=20)
    def __str__(self):
        return self.nome
    
class Voti(models.Model):
    voto=models.CharField(max_length=2)
    assenza=models.CharField(max_length=3)
    materia=models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="materie")
    studente=models.ForeignKey(Studente, on_delete=models.CASCADE, related_name="studente")
    def __str__(self):
        return self.studente.nome + " " + self.materia.materia + " " + self.voto + " " + self.assenza
