# Generated by Django 4.1.4 on 2022-12-28 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0003_alter_animal_especie'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultaVeterinaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('descricao', models.CharField(blank=True, max_length=200)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.animal')),
            ],
        ),
    ]