from django.shortcuts import render


def handler_404(request, exception):
    context = {"page_title": "404 Page Not Found" }
    return render(request, "error_pages/404.html", context, status=404)


def handler_500(request):
    context = {"page_title": "500 Internal Server Error" }
    return render(request, "error_pages/500.html", context, status=500)


def handler_403(request, exception):
    context = {"page_title": "403 Forbidden" }
    return render(request, "error_pages/403.html", context, status=403)


def handler_405(request, exception):
    context = {"page_title": "405 Method Not Allowed" }
    return render(request, "error_pages/405.html", context, status=405)