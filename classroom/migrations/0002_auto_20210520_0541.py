# Generated by Django 3.0 on 2021-05-20 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='annee',
            field=models.CharField(default=True, max_length=100, verbose_name="Si oui année de l'obtention du diplôme "),
        ),
        migrations.AlterField(
            model_name='student',
            name='formation_1',
            field=models.BooleanField(default=True, verbose_name="Je souhaite également m'inscrire le 29 Juin à la formation payante "),
        ),
        migrations.AlterField(
            model_name='student',
            name='formation_2',
            field=models.BooleanField(default=True, verbose_name="Je souhaite également m'inscrire le 30 Juin à la formation payante "),
        ),
        migrations.AlterField(
            model_name='student',
            name='niveau_etude',
            field=models.BooleanField(default=True, verbose_name="Niveau d'étude "),
        ),
    ]
