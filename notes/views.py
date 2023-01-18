from django.shortcuts import render
from django.contrib import messages
from notes.models import Notes

# Create your views here.
def home(request):
    # user = Notes.objects.filter(id=Notes.user.id)
    if request.method == "POST":
        body = request.POST['note']
        save_student = Notes.objects.create(body=body)
        messages.info(request, 'Note Added')
        save_student.save()
    else:
        messages.info(request, 'Note failed')


    return render(request, "index.html")

def noter(request):
    emps = Notes.objects.all()

    return render(request, "noter.html",{'emps':emps})