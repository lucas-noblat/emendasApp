from django.db import models

class Proponente(models.Model):
    cod_proponente = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Funcao(models.Model):
    cod_funcao = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Localidade(models.Model):
    id_local = models.AutoField(primary_key=True)
    municipio = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.municipio} - {self.uf}"


class Instituicao(models.Model):
    cod_instituicao = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    id_local = models.ForeignKey(Localidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Programa(models.Model):
    cod_programa = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Emenda(models.Model):
    cod_emenda = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=50)
    ano = models.IntegerField(null=True, blank=True)
    numero_emenda = models.CharField(max_length=20, null=True, blank=True)
    codigo_funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE)
    codigo_proponente = models.ForeignKey(Proponente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Emenda {self.cod_emenda}"


class AcaoOrcamentaria(models.Model):
    cod_acao = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=150)
    valor_empenhado = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    valor_pago = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    codigo_emenda = models.ForeignKey(Emenda, on_delete=models.CASCADE)
    codigo_programa = models.ForeignKey(Programa, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.descricao


class Repasse(models.Model):
    codigo_emenda = models.ForeignKey(Emenda, on_delete=models.CASCADE)
    codigo_instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    possui_convenio = models.BooleanField(null=True, blank=True)

    class Meta:
        unique_together = (('codigo_emenda', 'codigo_instituicao'),)

    def __str__(self):
        return f"Repasse: Emenda {self.codigo_emenda_id} - Instituição {self.codigo_instituicao_id}"

