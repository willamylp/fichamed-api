# Generated by Django 5.0.4 on 2024-05-01 10:43

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='Nome de Usuário')),
                ('email', models.EmailField(max_length=255, verbose_name='E-mail')),
                ('full_name', models.CharField(max_length=255, verbose_name='Nome Completo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('is_active', models.BooleanField(default=True, help_text='Desmarque essa opção para desativar o usuário e impedir o login.', verbose_name='Ativo')),
                ('is_staff', models.BooleanField(default=False, help_text='Marque essa opção para conceder acesso a área administrativa.', verbose_name='Admin')),
                ('is_superuser', models.BooleanField(default=False, help_text='Marque essa opção para conceder todos os privilégios, sem a necessidade de permissões.', verbose_name='Superusuário')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'db_table': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
