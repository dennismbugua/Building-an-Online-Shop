# Generated by Django 4.1.7 on 2023-03-23 14:59

from django.db import migrations
import django.db.models.deletion
import parler.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_translations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shop.category'),
        ),
        migrations.AlterField(
            model_name='producttranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shop.product'),
        ),
    ]
