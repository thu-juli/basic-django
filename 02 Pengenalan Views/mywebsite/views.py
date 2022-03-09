from django.http import HttpResponse


def index(request):
    header1 = '<h1>Hello From views</h1>'
    header2 = '<p>try use tag html on variable</p>'
    output = header1 + header2
    return HttpResponse(output)
