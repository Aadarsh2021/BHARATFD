# Generated by Django 5.1.5 on 2025-02-02 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("faq", "0002_remove_faq_question_bn_faq_answer_hi"),
    ]

    operations = [
        migrations.AddField(
            model_name="faq",
            name="answer_bn",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_gu",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_kn",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_ml",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_mr",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_pa",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_ta",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_te",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="answer_ur",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_bn",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_gu",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_kn",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_ml",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_mr",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_pa",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_ta",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_te",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="faq",
            name="question_ur",
            field=models.TextField(blank=True, null=True),
        ),
    ]
