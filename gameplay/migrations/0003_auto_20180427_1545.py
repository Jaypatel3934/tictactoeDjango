# Generated by Django 2.0.4 on 2018-04-27 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0002_game_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('F', 'First Player To Move'), ('S', 'Second Player To Move'), ('W', 'First player Win'), ('L', 'Second Player Win'), ('D', 'Draw')], default='F', max_length=1),
        ),
    ]
