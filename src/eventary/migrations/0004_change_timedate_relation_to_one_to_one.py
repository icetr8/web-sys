# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-02 21:50
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import eventary.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('eventary', '0003_auto_i18n_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', verbose_name='Normalisierung'),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Titel'),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='view_limit',
            field=models.IntegerField(help_text='limitiert die number der täglichen Zugriffe für nicht publizierte Veranstaltungen', verbose_name='Ansichtsbegrenzung'),
        ),
        migrations.AlterField(
            model_name='event',
            name='calendar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventary.Calendar', verbose_name='Kalender'),
        ),
        migrations.AlterField(
            model_name='event',
            name='comment',
            field=models.CharField(blank=True, help_text='Kommentar', max_length=255, null=True, verbose_name='Kommentar'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, help_text='Beschreibung', null=True, verbose_name='Beschreibung'),
        ),
        migrations.AlterField(
            model_name='event',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to=eventary.models._get_upload_path, verbose_name='Dokument'),
        ),
        migrations.AlterField(
            model_name='event',
            name='homepage',
            field=models.URLField(blank=True, null=True, verbose_name='Homepage'),
        ),
        migrations.AlterField(
            model_name='event',
            name='host',
            field=models.CharField(max_length=255, verbose_name='Veranstalter'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=eventary.models._get_upload_path, verbose_name='Bild'),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Veranstaltungsort'),
        ),
        migrations.AlterField(
            model_name='event',
            name='prize',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Preis', max_digits=6, null=True, verbose_name='Preis'),
        ),
        migrations.AlterField(
            model_name='event',
            name='published',
            field=models.BooleanField(help_text='Publizierungsstatus', verbose_name='Publiziert'),
        ),
        migrations.AlterField(
            model_name='event',
            name='recurring',
            field=models.BooleanField(default=False, help_text='periodische Veranstaltung', verbose_name='periodische Veranstaltung'),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Titel'),
        ),
        migrations.AlterField(
            model_name='eventtimedate',
            name='comment',
            field=models.CharField(blank=True, help_text='Kommentar', max_length=255, null=True, verbose_name='Kommentar'),
        ),
        migrations.AlterField(
            model_name='eventtimedate',
            name='end_date',
            field=models.DateField(blank=True, help_text='Datum Ende', null=True, verbose_name='Datum Ende'),
        ),
        migrations.AlterField(
            model_name='eventtimedate',
            name='end_time',
            field=models.TimeField(blank=True, help_text='Endzeit', null=True, verbose_name='Endzeit'),
        ),
        migrations.AlterField(
            model_name='eventtimedate',
            name='event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='eventary.Event', verbose_name='Veranstaltung'),
        ),
        migrations.AlterField(
            model_name='eventtimedate',
            name='start_date',
            field=models.DateField(help_text='Datum Beginn', verbose_name='Datum Beginn'),
        ),
        migrations.AlterField(
            model_name='eventtimedate',
            name='start_time',
            field=models.TimeField(blank=True, help_text='Startzeit', null=True, verbose_name='Startzeit'),
        ),
        migrations.AlterField(
            model_name='group',
            name='events',
            field=models.ManyToManyField(blank=True, to='eventary.Event', verbose_name='Veranstaltungen'),
        ),
        migrations.AlterField(
            model_name='group',
            name='grouping',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventary.Grouping', verbose_name='Gruppierung'),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Titel'),
        ),
        migrations.AlterField(
            model_name='grouping',
            name='calendars',
            field=models.ManyToManyField(blank=True, to='eventary.Calendar', verbose_name='Kalender'),
        ),
        migrations.AlterField(
            model_name='grouping',
            name='grouping_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventary.GroupingType', verbose_name='generischer Gruppierungstyp'),
        ),
        migrations.AlterField(
            model_name='grouping',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Titel'),
        ),
        migrations.AlterField(
            model_name='groupingtype',
            name='label',
            field=models.CharField(max_length=255, verbose_name='Etikett'),
        ),
        migrations.AlterField(
            model_name='host',
            name='homepage',
            field=models.URLField(verbose_name='Homepage'),
        ),
        migrations.AlterField(
            model_name='host',
            name='organization',
            field=models.CharField(help_text='Veranstalter', max_length=49, verbose_name='Veranstalter'),
        ),
        migrations.AlterField(
            model_name='host',
            name='phone',
            field=models.CharField(max_length=19, verbose_name='tel. Kontakt'),
        ),
        migrations.AlterField(
            model_name='secret',
            name='calls',
            field=models.IntegerField(default=0, verbose_name='Aufrufe'),
        ),
        migrations.AlterField(
            model_name='secret',
            name='creation_date',
            field=models.DateField(auto_now_add=True, verbose_name='Erstellungsdatum'),
        ),
        migrations.AlterField(
            model_name='secret',
            name='event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='eventary.Event', verbose_name='Veranstaltung'),
        ),
        migrations.AlterField(
            model_name='secret',
            name='last_call',
            field=models.DateField(null=True, verbose_name='letzter Aufruf'),
        ),
        migrations.AlterField(
            model_name='secret',
            name='secret',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Geheimnis'),
        ),
    ]