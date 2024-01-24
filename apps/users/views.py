from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from apps.users.models import Member
from django.core.paginator import Paginator

# Create your views here.
# Create your views here.
################ Authentication URLs ##############
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            
            return redirect('home') 
    return render(request, 'accounts/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def members(request):
    members = Member.objects.all()

    paginator = Paginator(members, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj
    }
    return render(request, "members/members.html", context)


def new_member(request):
    if request.method == "POST":
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        id_number = request.POST.get("id_number")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        address = request.POST.get("address")
        city = request.POST.get("city")
        country = request.POST.get("country")
        county = request.POST.get("county")

        member = Member.objects.create(
            name=name,
            gender=gender,
            id_number=id_number,
            phone_number=phone_number,
            email=email,
            address=address,
            city=city,
            county=county,
            country=country
        )

        return redirect("members")
    return render(request, "members/new_member.html")



def edit_member(request):
    if request.method == "POST":
        member_id = request.POST.get("member_id")
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        id_number = request.POST.get("id_number")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        address = request.POST.get("address")
        city = request.POST.get("city")
        county = request.POST.get("county")
        country = request.POST.get("country")

        member = Member.objects.get(id=member_id)
        member.name = name
        member.gender = gender
        member.id_number = id_number
        member.email = email
        member.phone_number = phone_number
        member.address = address
        member.city = city
        member.county = county
        member.country = country
        member.save()

        return redirect("members")

    return render(request, "members/edit_member.html")

def delete_member(request):
    if request.method == "POST":
        member_id = request.POST.get("member_id")
        member = Member.objects.get(id=member_id)
        member.delete()

        return redirect("members")

    return render(request, "members/delete_member.html")