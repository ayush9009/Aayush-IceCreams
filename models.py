from django.db import models

# Create your models here.
# model kya cheez hai jo aapkey database ko define karti hai
# makemigrations -create the changes and store it in a file
# migrate-apply the pending changes created by makemigrations
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12) 
    desc=models.TextField()
    date=models.DateField() 
    
    def __str__(self):   
        # is function ki madth se jaise aap dekna chaogey vaise dik jaga
            return self.name
    # python manage.py makemigrations ->is linek ka kya matlb haimodel mai kuch bhi vo kya hai vo tables ek trah se mere databse mai
    # contact kya hia table hai,jo ki data store karti hai,bilkul excel sheet ki trah ,aur name email phone etc ye table kai colum
    # hai,yani aise ek ecel sheet hai contact jisme ye baki sab columns hai
    # mange.py makemigrations maine models mai kuch changes kare hai databse mai un changes ki ek file bna lo,ye ni kaha changes jake datbase mai changes kar __do
    # maine kaha un changs ki file bna lo bas abhi
    # abhi commmand run karogey to no changes detected likha va ayega lakin aapne name ,email ye sab to bnaye yani changes to kare
    # to uske liyeaap ko pahle register karna pagega,to admin.py file mai jake karlo
    # pahle register kar liya phir apne aap 
    # 'home.apps.HomeConfig',ye aise installed apps mai mention kar diya
    # ab jab make migrations run karogey to initial.py karke file genertae is file mai jo bhi  aapne changes kare vo sab mention hai
    # below are the points for make model
    #admin.py mai jo bhi aapne model bnaya vo registe rkar do,dusri cheez app register kar do ,HomeConfig tha aaps.py mai to
    # use instlalled apps mai register kar diya 
    # abhi sirf changes ki file bni ,changes se kuch fark ni pda maatlb databse ye sab columns,ya kahe table genertate nhi hui
    # uske liye python manage.py migrate run kardo
    
    
