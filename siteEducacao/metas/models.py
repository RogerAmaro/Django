from django.db import models


class indicador(models.Model):
    meta_prevista = models.IntegerField() 
    executado = models.IntegerField() 
    não_executado = models.IntegerField() 
    Descrição_da_meta = models.TextField()


class metas(models.Model):
    
    número_da_meta = models.IntegerField()
    Descrição_da_meta = models.TextField()
    indicador_A = models.ForeignKey(indicador, on_delete=models.CASCADE, related_name="indicador_A")
    indicador_B = models.ForeignKey(indicador, on_delete=models.CASCADE, related_name="indicador_B")

    def __str__(self):
        return ("Meta" + str(self.numero_meta))

