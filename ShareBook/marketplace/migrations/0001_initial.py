# Generated by Django 4.2.1 on 2023-08-21 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('patronymic', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('file', models.FileField(upload_to='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('count_pages', models.IntegerField()),
                ('age_restriction', models.CharField(choices=[('0+', '0+'), ('6+', '6+'), ('12+', '12+'), ('16+', '16+'), ('18+', '18+')], max_length=4)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_books', to='marketplace.author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DelebleModel',
            fields=[
                ('book_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='marketplace.book')),
                ('delete', models.BooleanField()),
            ],
            bases=('marketplace.book',),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genre_books', to='marketplace.genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.language'),
        ),
    ]