from django.db import models
 
class ForUser(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)

class University(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,default="cra@gmail.com")
    date_naissance=models.DateField()
    telephone=models.IntegerField()
    ville=models.CharField(max_length=100)
    name_pere=models.CharField(max_length=100)
    name_mere=models.CharField(max_length=100)
    designationchoice=(('university','Etudiant Universitair'),('Jeunne garcons','Jeunne Garcons')
    )
    designation=models.CharField(max_length=100,choices=designationchoice,default='university')
    imageprofile=models.ImageField(default='images/avatar.jpg',null=True,blank=True,upload_to='images/')
    institution=models.CharField(max_length=100)
    fillier=models.CharField(max_length=100)
    batchchoice=(('1 ere annee','1 ere annee'),('2 eme annee','2 eme annee'),('3 eme annee','3 eme annee'),
    ('4 eme annee','4 eme annee'),('5 eme annee','5 eme annee'),('6 eme annee','6 eme annee')
    )
    batch=models.CharField(max_length=100,choices=batchchoice,default='1 ere annee')
    address=models.CharField(max_length=100)
    telephone_mere=models.IntegerField()
    telephone_pere=models.IntegerField()

class NotesUniversity(models.Model):
     university=models.ForeignKey(University,on_delete=models.CASCADE)
     yearchoice=(
        ('2021','2021'),('2022','2022'),('2023','2023'),('2024','2024'),('2025','2025'))
     year=models.CharField(max_length=20,choices=yearchoice,default='2021')
     semchoice=(('sem1','SEMESTER 1'),('sem2','SEMESTER 2'))
     sem=models.CharField(max_length=20,choices=semchoice,default='sem1')
     matiere=models.CharField(max_length=150)
     notes=models.CharField(max_length=150)
     charchoice=(('Academic','Academic'),('Dine','Dine'))
     characteristic=models.CharField(max_length=20,choices=charchoice,default='Academic')
     moyen=models.IntegerField()


class Jeunes(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    date_naissance=models.DateField()
    ville=models.CharField(max_length=100)
    name_pere=models.CharField(max_length=100)
    name_mere=models.CharField(max_length=100)
    designationchoice=(('Jeunne garcons','Jeunne Garcons'),('Jeunne fille','Jeunne Fille'),
    ('Petit garcons','Petit Garcons'),('Petite fille','Petite Fille'),
    )
    designation=models.CharField(max_length=100,choices=designationchoice,default='Jeunes')
    imageprofile=models.ImageField(default='images/avatar.jpg',null=True,blank=True,upload_to='images/')
    institution=models.CharField(max_length=100,default="La Sagesse")
    batchchoice=(('T1','T1'),('T2','T2'),('T3','T3'),('T4','T4'),('T5','T5'),('6 eme','6 eme'),('5 eme','5 eme'),('4 eme','4 eme'),('3 eme','3 eme'),('Second','Second'),('Premiere','Premiere'),('Terminal','Terminal'))
    batch=models.CharField(max_length=100,choices=batchchoice,default='6 eme')
    address=models.CharField(max_length=100)
    telephone_mere=models.IntegerField()
    telephone_pere=models.IntegerField()

class NotesJeunes(models.Model):
     jeunes=models.ForeignKey(Jeunes,on_delete=models.CASCADE)
     yearchoice=(('2021','2021'),('2022','2022'),('2023','2023'),('2024','2024'),('2025','2025'))
     year=models.CharField(max_length=20,choices=yearchoice,default='2021')
     semchoice=(('sem1','SEMESTER 1'),('sem2','SEMESTER 2'),('sem3','SEMESTER 3'))
     sem=models.CharField(max_length=20,choices=semchoice,default='sem1')
     matiere=models.CharField(max_length=150)
     notes=models.CharField(max_length=150)
     charchoice=(('Academic','Academic'),('Dine','Dine'))
     characteristic=models.CharField(max_length=20,choices=charchoice,default='Academic')
     moyen=models.IntegerField()




    

