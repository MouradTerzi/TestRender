from django.shortcuts import render, redirect
from .models import Personne

def home(request):
    
    if request.method == "POST":
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")

        if nom and prenom:
            Personne.objects.create(
                nom=nom,
                prenom=prenom
            )

        return redirect("home")

    personnes = Personne.objects.all().order_by("-created_at")

    return render(request, "home.html", {
        "personnes": personnes
    })
