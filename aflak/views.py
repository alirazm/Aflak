from django.http import HttpResponse

def home_test(reques):
    return HttpResponse("<script>alert(1)</script>")