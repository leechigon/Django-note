from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Note

class Write(CreateView):
    model = Note
    fields = ['name', 'text']
    success_url = reverse_lazy('note')

# Create your views here.
#def hello(request):
#    import random
#    n = random.randint(1,100)

#    html = "<h1>Hello, Django. {}</h1>".format(n)
#    return HttpResponse(html)    

def hello(request):
    import random
    nums = list(range(1,45))
    random.shuffle(nums)
    lotto = nums[0:6]
    lotto.sort()
    people = {'name':'honux', 'age': 25}

    return render(request, 'note/hello.html', { 'data': lotto })

def note(request):
    memos = Note.objects.all().order_by('-published_date')
    return render(request, 'note/note.html', {'notes': memos})    



 