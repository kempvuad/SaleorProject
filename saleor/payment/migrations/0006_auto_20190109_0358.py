# Generated by Django 2.1.4 on 2019-01-09 09:58

import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("payment", "0005_auto_20190104_0443")]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="gateway_response",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                encoder=django.core.serializers.json.DjangoJSONEncoder
            ),
        )
    ]
