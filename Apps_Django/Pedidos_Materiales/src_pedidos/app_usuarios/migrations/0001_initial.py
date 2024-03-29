# Generated by Django 2.2.4 on 2019-09-08 03:25

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('codigo_area', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_area', models.CharField(max_length=50)),
                ('descripcion_area', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Rol_Usuario',
            fields=[
                ('codigo_rol', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_rol', models.CharField(max_length=50)),
                ('descripcion_rol', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('identificacion', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('area_r', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_usuarios.Area')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('roll_r', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_usuarios.Rol_Usuario')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'permissions': {('is_almacenista', 'Permiso Rol Almacenista'), ('is_gestor_de_area', 'Permiso Rol Gestor De Area'), ('is_coordinador_misional', 'Permiso Rol Coordinador Misional'), ('is_administrador', 'Permiso Rol Administrador'), ('is_subdirector', 'Permiso Rol Subdirector'), ('is_cordinador_academico', 'Permiso Rol Cordinador Academico'), ('is_instructor', 'Permiso Rol Instructor')},
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
