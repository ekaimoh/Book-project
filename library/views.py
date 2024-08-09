from django.contrib import messages
from django.shortcuts import render, redirect

from library.models import LibraryBooks


# Create your views here.
def index(request):
    form = LibraryBooks()

    if request.method == 'POST':
        form = LibraryBooks(request.POST)
    if form.is_valid():
        # print("VALID")
        form.save()
        LibraryBooks()
        messages.success(request, 'User Registered Successfully')
        return redirect('index')
    else:
        form = LibraryBooks()
    return render(request, 'index.html',
                  {'form': form})