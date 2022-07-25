# Generated by Django 4.0.5 on 2022-07-25 13:27

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id_produto', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('descricao', models.CharField(blank=True, max_length=100, null=True)),
                ('valor_unitario_compra', models.DecimalField(decimal_places=2, default=0, max_digits=11)),
                ('valor_unitario_venda', models.DecimalField(decimal_places=2, default=0, max_digits=11)),
                ('data_inclusao', models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 25, 10, 27, 38, 380676), null=True)),
                ('usuario_inclusao', models.CharField(blank=True, max_length=50, null=True)),
                ('data_alteracao', models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 25, 10, 27, 38, 380676), null=True)),
                ('usuario_alteracao', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'cad_produto',
                'managed': True,
            },
        ),
    ]
