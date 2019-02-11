from django.shortcuts import render
from .models import Person
from .forms import PersonForm


def persons_list(requets):
    persons = Person.objects.all()
    return render(requets, 'person.html', {'persons':persons})
def persons_new(requests):
    form = PersonForm(request.POST, None)
    return render(request, 'person_form.html', {'form':form})

