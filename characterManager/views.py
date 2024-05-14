from src.custumRender import render

# Create your views here.
def index(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Access the user ID
        user_id = request.user.id
        # Print the user ID
        print("User ID:", user_id)
        # Alternatively, you can return the user ID in an HttpResponse
        user_id = request.user.id
        
    return render(request, "index.html", context = {})