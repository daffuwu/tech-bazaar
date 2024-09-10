from django.shortcuts import render

def show_main(request):
    context = {
        'app_name' : 'Tech Bazaar',
        'name' : 'Daffa Rayhan Ananda',
        'class' : 'PBP-E'
    }

    return render(request, "main.html", context)
