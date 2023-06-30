# Generated by Django 4.2.2 on 2023-06-29 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bird.family')),
            ],
        ),
        migrations.CreateModel(
            name='Kingdom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bird.domain')),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('genus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bird.genus')),
            ],
        ),
        migrations.CreateModel(
            name='Phylum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('kingdom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bird.kingdom')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bird.class')),
            ],
        ),
        migrations.AddField(
            model_name='family',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bird.order'),
        ),
        migrations.AddField(
            model_name='class',
            name='phylum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bird.phylum'),
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('weight', models.FloatField()),
                ('parent_group', models.CharField(max_length=100)),
                ('height', models.FloatField()),
                ('lifespan', models.IntegerField()),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bird.species')),
            ],
        ),
    ]
