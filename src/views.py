from src.custumRender import render


def index(request):
    print("page view")
    return render(request, "index.html", context={"navbar": "expend"})
