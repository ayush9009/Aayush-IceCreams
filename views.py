from django.shortcuts import render ,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

#ab ab ye soch ye rendere hai kya ,ye template ko render karne kai liye hota hai
#there are two static files ka concept and template ka concept

# ye jjo neeche kar raka ye url dispatching kah lata hai
# jitni bhi templates hum banyenge yaha kahe use karengef vo sab templates folder mai dalenge
# ab dekte ye static kya hai,ab chaenge kuch static jo user dek paye jaise maine koi dsa study website bnayi aur mai
# chata hunstudey material sab ko avaoiable ho to vo sab mai static files mai dal dunga(inshortvocheezjoaapkeserver pai aakey
# koi bhi dek le)
#in hello project we have settings.py to usme static urls honge

# Create your views here.
def index(request):
    context={
        'varible':"hey everyone this is aayush sharma"
        # ye to smjne kai  liye ,hum ya to apne models se vaues detch karke bejenge yaha phir  ya phirdatabse se pahle fetch karke title ko as a variable bejenge title bejenge 
    }
    # context set of varibles hote hai jo aap templates mai bej te ho
    return render(request,'index.html')
    # return HttpResponse("this is a aayush homepage")

def about(request):
    # return HttpResponse("this is a aayush about page")
    return render(request,'about.html')

def contact(request):
    # return HttpResponse("this is a aayush contact page")
    # databse se kaise bnta hai django mai,model kya hota hai,ek model bnate hai contact naam ka uska is view mai import karte hai ,aur jaise hi koi humari
    # webiste pai post request marega hum us data ko model dal lege
    # model bnayegi phir migrations ko run karayegey,phir uske bad migrate karenge
    if request.method=="POST":
        # mtlb agr request hui post ki to ye sab cheeze set kardo,
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        # contact ka ek object bna rai jaha 
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
       
        # is function se databse ab names ayenge ki kisne register kara 
        contact.save()
        messages.success(request, 'Your message has been sent!')
    
    return render(request,'contact.html')

def services(request):
    # return HttpResponse("this is a aayush service page")
    return render(request,'services.html')
# jab humko string deni hoti to hum use http response ki madath se deta hai ,iske kya hota hai ,is sey http resposne
# ki madath se hum string ko render kar pate hai,lakin ideally hum templates ka use karte hai ye to bas aise hi show kar diya