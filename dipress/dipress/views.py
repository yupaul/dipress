from django.http import HttpResponse


def index(request):
    return HttpResponse('<html><body><script>document.location.href="/create/";</script></body></html>')

