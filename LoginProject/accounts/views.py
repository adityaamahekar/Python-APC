
import re
from django.shortcuts import render

def login_view(request):
    message = ""
    success = False

    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        username_pattern = r"^[A-Za-z0-9_]{5,15}$"
        password_pattern = r"^(?=.*[A-Za-z])(?=.*\d).{8,}$"

        if not re.fullmatch(username_pattern, username):
            message = "Invalid username format!"

        elif not re.fullmatch(password_pattern, password):
            message = "Invalid password format!"

        elif username == "student123" and password == "Test1234":
            message = "Login Successful! Welcome student123"
            success = True

        else:
            message = "Incorrect username or password!"

    return render(request, "login.html", {
        "message": message,
        "success": success
    })
