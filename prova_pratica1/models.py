from django.db import models

# Create your models here.
class Materia(models.Model):
    materia=models.CharField(max_length=20)

    def __str__(self):
        return self.nome + " " + self.materia

class Voti(models.Model):
    nome=models.CharField(max_length=20)
    voto=models.CharField(max_length=2)
    assenza=models.CharField(max_length=3)
    materia=models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="materie")

    def __str__(self):
        return self.nome + " " + self.materia + " " + self.voto + " " + self.assenza
