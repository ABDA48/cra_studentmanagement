from django.contrib.auth import logout
from django.urls import path
from main import views
urlpatterns = [
    path("login/",views.login,name="login"),
    path("home/",views.home,name="home"),
    path("",views.home,name="home"),
    path('singin/',views.singin,name='singin'),
     path('logout/',views.logoutUser,name='logout'),
      path('studentadd/',views.studentAdd,name='studentadd'),
       path('university/',views.university,name='university'),
        path('university/<int:id>',views.universitydetail,name='universitydetail'),
        path('studentadd/save',views.studentAddsave,name='studentAddsave'),
        path('studentadd/update',views.studentAddupdate,name='studentAddupdate'),
 path('studentadd/delete',views.studentAdddelete,name='studentAdddelete'),
  path('studentadd/edit',views.studentAddedit,name='studentAddedit'),
  path('studentadd/savenotes',views.studentAddsavenotes,name='studentAddsavenotes'),
    path('studentadd/deletenotes',views.studentAdddeletenotes,name='studentAdddeletenotes'),
path('studentadd/editnotes',views.studentAddeditnotes,name='studentAddeditnotes'),
path('studentadd/updatenotes',views.studentAddupdatenotes,name='studentAddupdatenotes'),
path('university/details',views.universitydetails,name='universitydetails'),
path('studentadd/search',views.studentAddsearch,name='studentAddsearch'),
path('studentadd/searchid',views.studentAddsearchid,name='studentAddsearchid'),


path('university/notesdetails',views.notesdetails,name='notesdetails'),
path("university/<int:id>/resume",views.resume,name='resume'),
#############Jeunes Links###############################
path('jeunegarcons/',views.jeunegarcons,name='jeunegarcons'),
path('jeunedetail/notesdetails',views.notesjeunedetail,name='notesdetails'),
path('jeunedetail/details',views.jeunnedetails,name='jeunnedetails'),
path('jeunefille/',views.jeunefille,name='jeunefille'),
path('petitgarcons/',views.petitgarcons,name='petitgarcons'),
path('petitefille/',views.petitefille,name='petitefille'),
path('jeunneadd/',views.jeunneadd,name='jeunneadd'),
path('jeunneadd/save',views.jeunneaddsave,name='jeunneaddsave'),
    path('jeunneadd/update',views.jeunneaddupdate,name='jeunneaddupdate'),
 path('jeunneadd/delete',views.jeunneadddelete,name='jeunneadddelete'),
  path('jeunneadd/edit',views.jeunneaddedit,name='jeunneaddedit'),
   path('jeunneadd/savenotes',views.jeunneaddsavenotes,name='jeunneaddsavenotes'),
    path('jeunneadd/deletenotes',views.jeunneadddeletenotes,name='jeunneadddeletenotes'),
path('jeunneadd/editnotes',views.jeunneaddeditnotes,name='jeunneaddeditnotes'),
path('jeunneadd/updatenotes',views.jeunneaddupdatenotes,name='jeunneaddupdatenotes'),
path('jeunedetail/<int:id>',views.jeunedetail,name='jeunedetail'),
path("jeunedetail/<int:id>/resume",views.resumeJeunes,name='resumeJeunes'),
path('jeunneadd/search',views.jeunneaddsearch,name='jeunneaddsearch'),
path('jeunneadd/searchid',views.jeunneaddsearchid,name='jeunneaddsearchid'),
    
path('university/bages',views.universitybages,name='universitybages'),

path('jeunedetail/bages',views.jeunedetailbages,name='jeunedetailbages'),



  
     
   
     

]
