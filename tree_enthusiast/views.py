from django.shortcuts import render


def handler404(request, exception):
    return render(request, "error_pages/404.html", status=404)


def handler500(request):
    return render(request, "error_pages/500.html", status=500)


def handler403(request, exception):
    return render(request, "error_pages/403.html", status=403)


def handler405(request, exception):
    return render(request, "error_pages/405.html", status=405)