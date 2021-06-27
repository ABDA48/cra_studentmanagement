from django.contrib.auth import authenticate
from main.form import UniversityRegistration,JeunesRegistration
from django.shortcuts import redirect, render
from main.form import UserLogin,UserSingin,NotesUniversityForm,NotesJeunesForm
from django.contrib.auth  import authenticate,login as auth_login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthentificated_user,allowed_permisstion
from .models import University,NotesUniversity,NotesJeunes,Jeunes
from django.http import JsonResponse
from django.contrib.auth.models import Group

from django import template
import cloudinary
import qrcode
Root="https://cramanagement.herokuapp.com/"
register = template.Library()

@register.filter()
def range(min=5):
    return range(min)

@unauthentificated_user
def login(response):
    if response.POST:
        username=response.POST["username"]
        password=response.POST["password"]
        user=authenticate(response,username=username,password=password)
        if user is not None:
            auth_login(response,user)
            return redirect('home')
        else:
            messages.info(response,'UserName or Password Incorect')
    form=UserLogin()
    return render(response,"main/login.html",{"form":form})
@login_required(login_url='login')
def home(response):
      u=response.user.groups.all()[0].name
      if u=="Admin":
        print(u)
        return render(response,"main/home.html",{"u":u})
      else:
        return render(response,"main/home.html",{})
      

def logoutUser(response):
    logout(response)
    return redirect('login')
@unauthentificated_user
def singin(response):
    if response.method=="POST":
        print(response.POST)
        user=UserSingin(response.POST)
        if user.is_valid():
            ugroup=user.save()
            group=Group.objects.get(name='Basics')
            ugroup.groups.add(group)
            return redirect('login')
        else:
             messages.info(response,"Your Username can’t be too similar to your password.")
             messages.info(response,"Your password must contain at least 8 characters. ex:abcd@1234")
             messages.info(response,"UserName already existed or password doesn't mactch")

    form=UserSingin()
    return render(response,"main/singin.html",{"form":form})
@login_required(login_url='login')
@allowed_permisstion(allowed_roles=['Admin'])
def studentAdd(response):    
     form=UniversityRegistration
     ls=University.objects.all()
     formnotes=NotesUniversityForm
     noteslist=NotesUniversity.objects.all()
     u=response.user.groups.all()[0].name
     if u=="Admin":
        print(u)
        return render(response,"main/studentadd.html",{"form":form,"ls":ls,'formnotes':formnotes,'noteslist':noteslist,'u':u})
     else:
         return render(response,"main/studentadd.html",{"form":form,"ls":ls,'formnotes':formnotes,'noteslist':noteslist})

#####Jeunne###########
@login_required(login_url='login')
@allowed_permisstion(allowed_roles=['Admin'])
def jeunneadd(response):
    form=JeunesRegistration
    ls=Jeunes.objects.all()
    formnotes=NotesJeunesForm
    noteslist=NotesJeunes.objects.all()
    u=response.user.groups.all()[0].name
    if u=="Admin":
        print(u)
        return render(response,"main/jeunneadd.html",{"form":form,"ls":ls,'formnotes':formnotes,'noteslist':noteslist,'u':u})
    else:
         return render(response,"main/jeunneadd.html",{"form":form,"ls":ls,'formnotes':formnotes,'noteslist':noteslist})









@login_required(login_url='login')
def studentAddsave(response):
     if response.method=='POST':
         print(response.POST)
         university=UniversityRegistration(response.POST,response.FILES)
         if university.is_valid():
                    university.save()
                    u=University.objects.values()
                    u=list(u)
                    return JsonResponse({"status":"Saved","universities":u})
         else:
                return JsonResponse({"status":"Few Problem"})

@login_required(login_url='login')
def jeunneaddsave(response):
     if response.method=='POST':
         print(response.POST)
         jeunes=JeunesRegistration(response.POST,response.FILES)
         if jeunes.is_valid():
                    jeunes.save()
                    u=Jeunes.objects.values()
                    u=list(u)
                    return JsonResponse({"status":"Saved","universities":u})
         else:
                return JsonResponse({"status":"Few Problem"})


def studentAddupdate(response):
    i=response.POST['id']
    name=response.POST['name']
    email=response.POST['email']
    date_naissance=response.POST["date_naissance"]
    telephone=response.POST["telephone"]
    ville=response.POST["ville"]
    name_pere=response.POST["name_pere"]
    name_mere=response.POST["name_mere"]
    designation=response.POST["designation"]
    institution=response.POST["institution"]
    fillier=response.POST["fillier"]
    batch=response.POST["batch"]
    address=response.POST["address"]
    telephone_pere=response.POST["telephone_pere"]
    telephone_mere=response.POST["telephone_mere"]
    University.objects.filter(pk=i).update(
              name=name
            )
    University.objects.filter(pk=i).update(
              email=email
            )
    University.objects.filter(pk=i).update(
              date_naissance=date_naissance
            )
    University.objects.filter(pk=i).update(
              telephone=telephone
        )
    University.objects.filter(pk=i).update(
              ville=ville
        )
    University.objects.filter(pk=i).update(
              name_pere=name_pere
            )
    University.objects.filter(pk=i).update(
              name_mere=name_mere
        )
    University.objects.filter(pk=i).update(
              designation=designation
        )
    University.objects.filter(pk=i).update(
              institution=institution
            )
    University.objects.filter(pk=i).update(
              fillier=fillier
        )
    University.objects.filter(pk=i).update(
              batch=batch
        )
    University.objects.filter(pk=i).update(
              address=address
        )
    University.objects.filter(pk=i).update(
              telephone_pere=telephone_pere
            )
    University.objects.filter(pk=i).update(
              telephone_mere=telephone_mere
        )
    u=University.objects.values()
    u=list(u)
    return JsonResponse({"status":"Saved","universities":u})

def jeunneaddupdate(response):
    i=response.POST['id']
    name=response.POST['name']
   
    date_naissance=response.POST["date_naissance"]
   
    ville=response.POST["ville"]
    name_pere=response.POST["name_pere"]
    name_mere=response.POST["name_mere"]
    designation=response.POST["designation"]
    institution=response.POST["institution"]
 
    batch=response.POST["batch"]
    address=response.POST["address"]
    telephone_pere=response.POST["telephone_pere"]
    telephone_mere=response.POST["telephone_mere"]
    Jeunes.objects.filter(pk=i).update(
              name=name
            )
     
    Jeunes.objects.filter(pk=i).update(
              date_naissance=date_naissance
            )
    
    Jeunes.objects.filter(pk=i).update(
              ville=ville
        )
    Jeunes.objects.filter(pk=i).update(
              name_pere=name_pere
            )
    Jeunes.objects.filter(pk=i).update(
              name_mere=name_mere
        )
    Jeunes.objects.filter(pk=i).update(
              designation=designation
        )
    Jeunes.objects.filter(pk=i).update(
              institution=institution
            )
     
    Jeunes.objects.filter(pk=i).update(
              batch=batch
        )
    Jeunes.objects.filter(pk=i).update(
              address=address
        )
    Jeunes.objects.filter(pk=i).update(
              telephone_pere=telephone_pere
            )
    Jeunes.objects.filter(pk=i).update(
              telephone_mere=telephone_mere
        )
    u=Jeunes.objects.values()
    u=list(u)
    return JsonResponse({"status":"Saved","universities":u})




@login_required(login_url='login')
def studentAdddelete(response):
     if response.method=="POST":
        id=response.POST["id"]
        u=University.objects.filter(pk=id)
        u.delete()
        u=University.objects.values()
        u=list(u)
        return JsonResponse({"status":"deleted","users":u})
     else:
        return JsonResponse({"status":"Few Problem"})
def studentAddedit(response):
    if response.method=="POST":
        id=response.POST["id"]
        u=University.objects.get(pk=id)
        data= {'id':u.id,'name':u.name,'date_naissance':u.date_naissance,'telephone':u.telephone,
'ville':u.ville,'name_pere':u.name_pere,'name_mere':u.name_mere,'designation':u.designation,'institution':u.institution,'fillier':u.fillier,
'batch':u.batch,'address':u.address,'telephone_pere':u.telephone_pere,'telephone_mere':u.telephone_pere}
        return JsonResponse({"status":"deleted","data":data})
    else:
        return JsonResponse({"status":"Few Problem"})

def jeunneadddelete(response):
    if response.method=="POST":
        id=response.POST["id"]
        u=Jeunes.objects.filter(pk=id)
        u.delete()
        u=Jeunes.objects.values()
        u=list(u)
        return JsonResponse({"status":"deleted","users":u})
    else:
        return JsonResponse({"status":"Few Problem"})

def jeunneaddedit(response):
    if response.method=="POST":
        id=response.POST["id"]
        u=Jeunes.objects.get(pk=id)
        data= {'id':u.id,'name':u.name,'date_naissance':u.date_naissance,
'ville':u.ville,'name_pere':u.name_pere,'name_mere':u.name_mere,'designation':u.designation,'institution':u.institution,
'batch':u.batch,'address':u.address,'telephone_pere':u.telephone_pere,'telephone_mere':u.telephone_pere}
        return JsonResponse({"status":"deleted","data":data})
    else:
        return JsonResponse({"status":"Few Problem"})


@login_required(login_url='login')
def studentAddsavenotes(response):
    if response.method=="POST":
            notes=NotesUniversityForm(response.POST)
            if notes.is_valid():
                notes.save()
                print('save')
                n=NotesUniversity.objects.values()
                n=list(n)
                return JsonResponse({"status":"Saved","notes":n})
            else:
                return JsonResponse({"status":"Few Problem"})
 
@login_required(login_url='login')
def jeunneaddsavenotes(response):
    if response.method=="POST":
            notes=NotesJeunesForm(response.POST)
            if notes.is_valid():
                notes.save()
                print('save')
                n=NotesJeunes.objects.values()
                n=list(n)
                return JsonResponse({"status":"Saved","notes":n})
            else:
                return JsonResponse({"status":"Few Problem"})



@login_required(login_url='login')
def jeunneadddeletenotes(response):
    if response.method=='POST':
        id=response.POST["id"]
        u=NotesJeunes.objects.filter(pk=id)
        u.delete()
        u=NotesJeunes.objects.values()
        u=list(u)
        return JsonResponse({"status":"deleted","users":u})
    else:
        return JsonResponse({"status":"Few Problem"})
@login_required(login_url='login')
def studentAddeditnotes(response):
    if response.method=="POST":
        id=response.POST["id"]
        u=NotesUniversity.objects.get(pk=id)
        data= {'id':id,'uid':u.university_id,'year':u.year,'sem':u.sem,'matiere':u.matiere,
'notes':u.notes,'characteristic':u.characteristic,'moyen':u.moyen}
        return JsonResponse({"status":"deleted","data":data})
    else:
        return JsonResponse({"status":"Few Problem"})
    pass

@login_required(login_url='login')
def jeunneaddeditnotes(response):
    if response.method=="POST":
        id=response.POST["id"]
        u=NotesJeunes.objects.get(pk=id)
        data= {'id':id,'uid':u.jeunes_id,'year':u.year,'sem':u.sem,'matiere':u.matiere,
'notes':u.notes,'characteristic':u.characteristic,'moyen':u.moyen}
        return JsonResponse({"status":"deleted","data":data})
    else:
        return JsonResponse({"status":"Few Problem"})
    pass

@login_required(login_url='login')
def studentAdddeletenotes(response):
    if response.method=='POST':
        id=response.POST["id"]
        u=NotesUniversity.objects.filter(pk=id)
        u.delete()
        u=NotesUniversity.objects.values()
        u=list(u)
        return JsonResponse({"status":"deleted","users":u})
    else:
        return JsonResponse({"status":"Few Problem"})

@login_required(login_url='login')
def jeunneadddeletenotes(response):
    if response.method=='POST':
        id=response.POST["id"]
        u=NotesJeunes.objects.filter(pk=id)
        u.delete()
        u=NotesJeunes.objects.values()
        u=list(u)
        return JsonResponse({"status":"deleted","users":u})
    else:
        return JsonResponse({"status":"Few Problem"})
 
@login_required(login_url='login')
def studentAddupdatenotes(response):
         i=response.POST['id']
         print(response.POST)
         university=response.POST['university']
         sem=response.POST['sem']
         matiere=response.POST['matiere']
         note=response.POST['notes']
         characteristic=response.POST['characteristic']
         moyen=response.POST['moyen']
         NotesUniversity.objects.filter(pk=i).update(
              university=university
            )
         NotesUniversity.objects.filter(pk=i).update(
              sem=sem
            )
         NotesUniversity.objects.filter(pk=i).update(
              matiere=matiere
            )
         NotesUniversity.objects.filter(pk=i).update(
              notes=note
            )
         NotesUniversity.objects.filter(pk=i).update(
              characteristic=characteristic
            )
         NotesUniversity.objects.filter(pk=i).update(moyen=moyen)
         n=NotesUniversity.objects.values()
         n=list(n)
         return JsonResponse({"status":"Saved","notes":n})

 
@login_required(login_url='login')
def  jeunneaddupdatenotes(response):
         i=response.POST['id']
         print(response.POST)
         jeunes=response.POST['jeunes']
         sem=response.POST['sem']
         matiere=response.POST['matiere']
         note=response.POST['notes']
         characteristic=response.POST['characteristic']
         moyen=response.POST['moyen']
         NotesJeunes.objects.filter(pk=i).update(
              jeunes=jeunes
            )
         NotesJeunes.objects.filter(pk=i).update(
              sem=sem
            )
         NotesJeunes.objects.filter(pk=i).update(
              matiere=matiere
            )
         NotesJeunes.objects.filter(pk=i).update(
              notes=note
            )
         NotesJeunes.objects.filter(pk=i).update(
              characteristic=characteristic
            )
         NotesJeunes.objects.filter(pk=i).update(moyen=moyen)
         n=NotesJeunes.objects.values()
         n=list(n)
         return JsonResponse({"status":"Saved","notes":n})

@login_required(login_url='login')
def university(response):
    ls=University.objects.all()
    u=response.user.groups.all()[0].name
    if u=="Admin":
        print(u)
        return render(response,'main/university.html',{"ls":ls,'u':u})
    else:
        return render(response,'main/university.html',{"ls":ls})

@login_required(login_url='login')
def jeunegarcons(response):
    ls=Jeunes.objects.filter(designation='Jeunne garcons')
    u=response.user.groups.all()[0].name
    if u=="Admin":
        print(u)
        return render(response,'main/jeunegarcons.html',{"ls":ls,'u':u})
    else:
        return render(response,'main/jeunegarcons.html',{"ls":ls})
@login_required(login_url='login')
def jeunefille(response):
    ls=Jeunes.objects.filter(designation='Jeunne fille')
    u=response.user.groups.all()[0].name
    if u=="Admin":
        print(u)
        return render(response,'main/jeunegarcons.html',{"ls":ls,'u':u})
    else:
        return render(response,'main/jeunegarcons.html',{"ls":ls})
@login_required(login_url='login')
def petitgarcons(response):
    ls=Jeunes.objects.filter(designation='Petit garcons')
    u=response.user.groups.all()[0].name
    if u=="Admin":
        print(u)
        return render(response,'main/jeunegarcons.html',{"ls":ls,'u':u})
    else:
        return render(response,'main/jeunegarcons.html',{"ls":ls})
@login_required(login_url='login')
def petitefille(response):
    ls=Jeunes.objects.filter(designation='Petite fille')
    u=response.user.groups.all()[0].name
    if u=="Admin":
        print(u)
        return render(response,'main/jeunegarcons.html',{"ls":ls,'u':u})
    else:
        return render(response,'main/jeunegarcons.html',{"ls":ls})

    

@login_required(login_url='login')
@allowed_permisstion(allowed_roles=['Admin','Users'])  
def universitydetail(response,id):
    ls=University.objects.filter(id=id)
    n=NotesUniversity.objects.filter(university=id,year='2021',characteristic='Academic')
    n2=NotesUniversity.objects.filter(university=id,year='2021',characteristic='Dine')
    
    m2={}
    m={}
    msem2=""
    msem1=""
    matiere2=""
    if n:
        if n[0]:
            nm=n[0].matiere
            nm=nm.split('-')
            matiere1=nm
            nm=n[0].notes
            nm=nm.split('-')
            notes1=nm
            msem1=n[0].moyen
        if len(n)>1:
            nm2=n[1].matiere
            nm2=nm2.split('-')
            matiere2=nm2
            nm2=n[1].notes
            nm2=nm2.split('-')
            notes2=nm2
            msem2=n[1].moyen
        else:
            matiere2=""
            notes2=""
        m={'matiere1':matiere1,'matiere2':matiere2,'notes1':notes1,'notes2':notes2,'msem1':msem1,'msem2':msem2}
    if n2:
        if n2[0]:
            nm=n2[0].matiere
            nm=nm.split('-')
            matiere1=nm
            nm=n2[0].notes
            nm=nm.split('-')
            notes1=nm
            msem1=n2[0].moyen
        if len(n2)>1:
            nm2=n2[1].matiere
            nm2=nm2.split('-')
            matiere2=nm2
            nm2=n2[1].notes
            nm2=nm2.split('-')
            notes2=nm2
            msem2=n2[1].moyen
        else:
            matiere2=""
            notes2=""
        m2={'matiere1':matiere1,'matiere2':matiere2,'notes1':notes1,'notes2':notes2,'msem1':msem1,'msem2':msem2}
    u=response.user.groups.all()[0].name
    if u=="Admin":
        print(u)
        return render(response,'main/universitydetails.html',{'ls':ls,'n2':n2,'m2':m2,'n':n,'m':m,'u':u})
    else:
        return render(response,'main/universitydetails.html',{'ls':ls,'n2':n2,'m2':m2,'n':n,'m':m})

@login_required(login_url='login')
@allowed_permisstion(allowed_roles=['Admin','Users'])  
def jeunedetail(response,id):
    ls=Jeunes.objects.filter(id=id)
    n=NotesJeunes.objects.filter(jeunes=id,year='2021',characteristic='Academic')
    n2=NotesJeunes.objects.filter(jeunes=id,year='2021',characteristic='Dine')
    
    m2={}
    m={}
    msem2=""
    msem3=""
    msem1=""
    matiere3=""
    notes3=""
    notes2=""
    matiere2=""
    if n:
        if n[0]:
            nm=n[0].matiere
            nm=nm.split('-')
            matiere1=nm
            nm=n[0].notes
            nm=nm.split('-')
            notes1=nm
            msem1=n[0].moyen
        if len(n)>1:
            nm2=n[1].matiere
            nm2=nm2.split('-')
            matiere2=nm2
            nm2=n[1].notes
            nm2=nm2.split('-')
            notes2=nm2
            msem2=n[1].moyen
        if len(n)>2:
           nm3=n[2].matiere
           nm3=nm3.split('-')
           matiere3=nm3
           nm3=n[2].notes
           nm3=nm3.split('-')
           notes3=nm3
           msem3=n[2].moyen
        m={'matiere1':matiere1,'matiere2':matiere2,'matiere3':matiere3,'notes1':notes1,'notes2':notes2,'notes3':notes3,
        'msem1':msem1,'msem2':msem2,'msem3':msem3,
        }
    if n2:
        if n2[0]:
            nm=n2[0].matiere
            nm=nm.split('-')
            matiere1=nm
            nm=n2[0].notes
            nm=nm.split('-')
            notes1=nm
            msem1=n2[0].moyen
        if len(n2)>1:
            nm2=n2[1].matiere
            nm2=nm2.split('-')
            matiere2=nm2
            nm2=n2[1].notes
            nm2=nm2.split('-')
            notes2=nm2
            msem2=n2[1].moyen
        if len(n2)>2:
           nm3=n[2].matiere
           nm3=nm3.split('-')
           matiere3=nm3
           nm3=n[2].notes
           nm3=nm3.split('-')
           notes3=nm3
           msem3=n[2].moyen
        m={'matiere1':matiere1,'matiere2':matiere2,'matiere3':matiere3,'notes1':notes1,'notes2':notes2,'notes3':notes3,
        'msem1':msem1,'msem2':msem2,'msem3':msem3,
        }
    u=response.user.groups.all()[0].name
    if u=="Admin":
        print(u)
        return render(response,'main/jeunedetail.html',{'ls':ls,'n2':n2,'m2':m2,'n':n,'m':m,'u':u})
    else:
        return render(response,'main/jeunedetail.html',{'ls':ls,'n2':n2,'m2':m2,'n':n,'m':m})
    
def universitydetails(response):
    if response.GET:
        id=int(response.GET['id'])
        print(id)
        ls=University.objects.filter(id=id).values()
        return JsonResponse({"status":"Saved","details":ls[0]})

def jeunnedetails(response):
    if response.GET:
        id=int(response.GET['id'])
        print(id)
        ls=Jeunes.objects.filter(id=id).values()
        return JsonResponse({"status":"Saved","details":ls[0]})

def notesdetails(response):
    if response.GET:
        id=int(response.GET['id'])
        year=response.GET['year']
        characteristic=response.GET['characteristic']
        print(id)
        print(year)
        n=NotesUniversity.objects.filter(university=id,year=year,characteristic=characteristic).values()
        if n:
            notes={}
            notes['sem1']=n[0]
            notes['moyen']=n[0]['moyen']
            if len(n)>1:
                notes['sem2']=n[1]
                notes['moyen2']=n[1]['moyen']
            else:
                notes['sem2']=""
                notes['moyen2']=""
            return JsonResponse({"status":"Saved","details":notes})
        return JsonResponse({"status":"Saved","details":""})
def notesjeunedetail(response):
    if response.GET:
        id=int(response.GET['id'])
        year=response.GET['year']
        characteristic=response.GET['characteristic']
        print(id)
        print(year)
        n=NotesJeunes.objects.filter(jeunes=id,year=year,characteristic=characteristic).values()
        if n:
            notes={}
            notes['sem1']=n[0]
            notes['moyen']=n[0]['moyen']
            if len(n)>1:
                notes['sem2']=n[1]
                notes['moyen2']=n[1]['moyen']
            if len(n)>2:
                notes['sem3']=n[2]
                notes['moyen3']=n[2]['moyen']
            return JsonResponse({"status":"Saved","details":notes})
        return JsonResponse({"status":"Saved","details":""})
        
def studentAddsearch(response):
    if response.GET:
        name=response.GET['name']
        u=University.objects.filter(name__contains=name).values()
        u=list(u)
        return JsonResponse({"status":"Saved","data":u})
def jeunneaddsearch(response):
    if response.GET:
        name=response.GET['name']
        print("name"+name)
        u=Jeunes.objects.filter(name__contains=name).values()
        u=list(u)
        print(u)
        return JsonResponse({"status":"Saved","data":u})

def jeunneaddsearchid(response):
    if response.GET:
        id=response.GET['name']
        u=NotesJeunes.objects.filter(jeunes=id).values()
        u=list(u)
        return JsonResponse({"status":"Saved","data":u})
       
def studentAddsearchid(response):
    if response.GET:
        id=response.GET['name']
        u=NotesUniversity.objects.filter(university=id).values()
        u=list(u)
        return JsonResponse({"status":"Saved","data":u})
        
        
         

def resume(response,id):
        ls=University.objects.filter(id=id)
        ns1_2021A=NotesUniversity.objects.filter(university=id,year='2021',characteristic='Academic')
        ns1_2022A=NotesUniversity.objects.filter(university=id,characteristic='Academic',year='2022')
        ns1_2023A=NotesUniversity.objects.filter(university=id,year='2023',characteristic='Academic')
        ns1_2024A=NotesUniversity.objects.filter(university=id,characteristic='Academic',year='2024')
        ns1_2025A=NotesUniversity.objects.filter(university=id,characteristic='Academic',year='2025')

        ns1_2021D=NotesUniversity.objects.filter(university=id,year='2021',characteristic='Dine')
        ns1_2022D=NotesUniversity.objects.filter(university=id,characteristic='Dine',year='2022')
        ns1_2023D=NotesUniversity.objects.filter(university=id,year='2023',characteristic='Dine')
        ns1_2024D=NotesUniversity.objects.filter(university=id,characteristic='Dine',year='2024')
        ns1_2025D=NotesUniversity.objects.filter(university=id,characteristic='Dine',year='2025')
        
        
        return render(response,'main/resume.html',{'id':id,'ls':ls,'ns1_2021A':ns1_2021A,'ns1_2022A':ns1_2022A,
        'ns1_2023A':ns1_2023A,'ns1_2024A':ns1_2024A,'ns1_2025A':ns1_2025A,'ns1_2021D':ns1_2021D,'ns1_2022D':ns1_2022D,
        'ns1_2023D':ns1_2023D,'ns1_2024D':ns1_2024D,'ns1_2025D':ns1_2025D
        })

def resumeJeunes(response,id):
        ls=Jeunes.objects.filter(id=id)
        ns1_2021A=NotesJeunes.objects.filter(jeunes=id,year='2021',characteristic='Academic')
        ns1_2022A=NotesJeunes.objects.filter(jeunes=id,characteristic='Academic',year='2022')
        ns1_2023A=NotesJeunes.objects.filter(jeunes=id,year='2023',characteristic='Academic')
        ns1_2024A=NotesJeunes.objects.filter(jeunes=id,characteristic='Academic',year='2024')
        ns1_2025A=NotesJeunes.objects.filter(jeunes=id,characteristic='Academic',year='2025')

        ns1_2021D=NotesJeunes.objects.filter(jeunes=id,year='2021',characteristic='Dine')
        ns1_2022D=NotesJeunes.objects.filter(jeunes=id,characteristic='Dine',year='2022')
        ns1_2023D=NotesJeunes.objects.filter(jeunes=id,year='2023',characteristic='Dine')
        ns1_2024D=NotesJeunes.objects.filter(jeunes=id,characteristic='Dine',year='2024')
        ns1_2025D=NotesJeunes.objects.filter(jeunes=id,characteristic='Dine',year='2025')
        
        
        return render(response,'main/resumeJeune.html',{'id':id,'ls':ls,'ns1_2021A':ns1_2021A,'ns1_2022A':ns1_2022A,
        'ns1_2023A':ns1_2023A,'ns1_2024A':ns1_2024A,'ns1_2025A':ns1_2025A,'ns1_2021D':ns1_2021D,'ns1_2022D':ns1_2022D,
        'ns1_2023D':ns1_2023D,'ns1_2024D':ns1_2024D,'ns1_2025D':ns1_2025D
        })
       
def universitybages(response):
    #http://127.0.0.1:8000/university/1001/resume
    ls=University.objects.all()
    for item in ls:
        print(type(item))
        id=item.id
        img=qrcode.make(Root+"/university/"+str(id)+"/resume")
        img.save("main/static/images/"+str(id)+".png")
        resultat=cloudinary.uploader.upload("main/static/images/"+str(id)+".png",overwrite =True)
        url=resultat.get("url")
    return render(response,"main/bages.html",{'ls':ls,'root':Root})

def  jeunedetailbages(response):
    ls=Jeunes.objects.all()
    for item in ls:
        print(type(item))
        id=item.id
        img=qrcode.make(Root+"/jeunedetail/"+str(id)+"/resume")
        img.save("main/static/images/"+str(id)+"jeune.png")
    return render(response,"main/bagesjeune.html",{'ls':ls,'root':Root})
       

    
        
                
     


 


