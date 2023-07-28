from django.shortcuts import render, redirect
from details.models import Student
from details.forms import StudentForm

# Create your views here.


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = StudentForm()
        return render(request, 'index.html', {'form': form})
