# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.2.3 on 2023-08-02 13:20

from django.db import migrations

import weblate.trans.fields


class Migration(migrations.Migration):
    dependencies = [
        ("weblate_auth", "0027_alter_group_components"),
    ]

    operations = [
        migrations.AlterField(
            model_name="autogroup",
            name="match",
            field=weblate.trans.fields.RegexField(
                default="^$",
                help_text="Users with e-mail addresses found to match will be added to this group.",
                max_length=200,
                verbose_name="Regular expression for e-mail address",
            ),
        ),
    ]
