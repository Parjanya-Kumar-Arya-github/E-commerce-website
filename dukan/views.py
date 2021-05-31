from django.shortcuts import render
from .models import saman, Contact,Orders,OrderUpdate
import math
from django.contrib import messages
from django.http import HttpResponse
import json
from django.core.cache import cache

# Create your views here.
def home(request):
    allProds = []
    catprods = saman.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = saman.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + math.ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'home.html', params)

def List(request):
    params = saman.objects.all()
    print(params)
    return render(request, "List.html", {"product": params})

def contactus(request):
    if request.method=='POST':
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        message=request.POST.get('message','')
        contact=Contact(name=name,email=email,phone=phone,message=message)
        contact.save()
        messages.success(request,"Your response has been successfully submitted!")
    return render(request,'contact.html')
def productview(request,myid):
    object_choosed=saman.objects.filter(product_name=myid)
    return render(request,'product.html',{'product':object_choosed[0]})
def about(request):
    return render(request,'about.html')
# def check_out(request):

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'checkout.html', {'thank':thank, 'id': id})
    return render(request, 'checkout.html')

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'tracker.html')
def track(request,myid):
    order = Orders.objects.filter(order_id=myid)
    email=order[0].email
    print(email)
    return render(request, 'track.html',{'id':myid,'email':email})



def payment(request,myid):
    return render(request,'payment.html',{'id':myid})
    cache.clear()

def search(request):
    if request.method=='POST':
        searchedfor=str(request.POST.get('searchedabout')).lower()
        item_name_list=[]
        item_desc_list=[]
        item_cat_list=[]
        items=(saman.objects.all())
        result=set()
        for item in items:
            item_name_list.append(str(item).lower())
            item_desc_list.append(str(item.product_desc).lower())
            item_cat_list.append(str(item.category).lower())
        if searchedfor in item_name_list:
            try:
                result.add(item_name_list.index(searchedfor))
            except:
                pass
        for item_desc in item_desc_list:
            if searchedfor in item_desc:
                result.add(item_desc_list.index(item_desc))
        if searchedfor in item_cat_list:
            result.add(item_cat_list.index(searchedfor))

        final_list=[]
        for val in result:
            final_list.append(items[int(val)])
            
        return render(request,'search.html',{'searched':searchedfor.capitalize(),'items':final_list})

        
    return render(request,'search.html')

def buynow(request,myid):
    product=saman.objects.filter(product_name=myid)
    print(product)
    return render(request,'buynow.html',{'product':product[0]})