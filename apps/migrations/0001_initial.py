# Generated by Django 3.2.5 on 2021-07-10 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('speciality', models.TextField()),
                ('nmc_no', models.CharField(max_length=10)),
                ('doctor_image', models.ImageField(upload_to='doctor_image')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('contact_no', models.CharField(max_length=15)),
                ('hospital_image', models.ImageField(upload_to='hospital_image')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('contact_no', models.CharField(max_length=10)),
                ('volunteer_image', models.ImageField(upload_to='volunteer_image')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='HospitalRelated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_doctor', models.CharField(choices=[('Not Available', 'Not Available'), ('Available', 'Available')], default='Not Available', max_length=50)),
                ('has_ambulance', models.CharField(choices=[('Not Available', 'Not Available'), ('Available', 'Available')], default='Not Available', max_length=50)),
                ('has_blood', models.CharField(choices=[('Not Available', 'Not Available'), ('Available', 'Available')], default='Not Available', max_length=50)),
                ('has_bed', models.CharField(choices=[('Not Available', 'Not Available'), ('Available', 'Available')], default='Not Available', max_length=50)),
                ('has_oxygen', models.CharField(choices=[('Not Available', 'Not Available'), ('Available', 'Available')], default='Not Available', max_length=50)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.doctor')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.hospital')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.volunteer')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.hospital'),
        ),
        migrations.CreateModel(
            name='Blood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_type', models.CharField(choices=[('A +', 'A positive'), ('B +', 'B positive'), ('O +', 'O positive'), ('AB +', 'AB positive'), ('A -', 'A negative'), ('B -', 'B negative'), ('O -', 'O negative'), ('AB -', 'AB negative')], max_length=10)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.hospital')),
            ],
        ),
    ]
