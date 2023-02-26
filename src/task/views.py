from django.shortcuts import render

def index(req):
    pass
"""
# Create your views here.

def index(request):
    tasks = Task.objects.all()
    categories = Category.objects.all()
    if request.method == "POST": 
        if "taskAdd" in request.POST:
            print(request.POST)
            title = request.POST["description"]  # title
            date = str(request.POST["date"])  # date
            category = request.POST["category_select"]  # category
            status = request.POST["status_select"]  # category
            content = title + " -- " + date + " " + category  # content
            task = Task(title=title, content=content, due_date=date
                            , category=Category.objects.get(name=category)
                            , status=status)
            task.save()  # saving the todo
            return redirect("/")  # reloading the page

        if "taskDelete" in request.POST:  # checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"]  # checked todos to be deleted
            for task_id in checkedlist:
                print(task_id)
                task = TodoList.objects.get(id=int(task_id))  # getting todo id
                task.delete()  # deleting todo

    return render(request, "index.html",
                  {"todos": tasks, "categories": categories, "status": [st[0] for st in TODO_STATUS]})


class TodoDetailView(ListView):
    paginate_by = 10
    model = Task
    template_name = 'detail.html'
"""