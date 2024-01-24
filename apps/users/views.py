from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, render

from apps.users.models import Member


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
    members = Member.objects.all().order_by("-created")

    if request.method == "POST":
        search_text = request.POST.get("search_text")
        members = Member.objects.filter(
            Q(name__icontains=search_text) | Q(id_number__icontains=search_text)
        ).order_by("-created")

    paginator = Paginator(members, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj
    }
    return render(request, "members/members.html", context)


def member_details(request, member_id=None):
    member = Member.objects.get(id=member_id)

    books_issued = member.memberissuedbooks.all()
    paginator = Paginator(books_issued, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "member": member,
        "page_obj": page_obj
    }

    return render(request, "members/member_details.html", context)

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