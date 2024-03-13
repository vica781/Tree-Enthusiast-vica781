from django.shortcuts import render


def handler_404(request, exception):
    return render(request, "error_pages/404.html", {}, status=404)


def handler_500(request):
    return render(request, "error_pages/500.html", {}, status=500)


def handler_403(request, exception):
    return render(request, "error_pages/403.html", {}, status=403)


def handler_405(request, exception):
    return render(request, "error_pages/405.html", {}, status=405)