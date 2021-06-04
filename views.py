from django.shortcuts import render
#after working with class models we can eliminated this Httpresponse 
#from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
#this LoginRequiredMixin is used for restricting user to look into or invalid user login
from .models import Task

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks')

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    #template_name = 'base/task_list.html'
    context_object_name = 'tasks'
    
    def get_context_object_name(self, tasks):
        context_object_name = 'tasks'
        
        #Get the name to use for the object.

        if self.tasks:
            return self.tasks
        elif isinstance(obj, models.Model):
            return obj._meta.model_name
        else:
            return None

    def get_context_data(self, **kwargs):
        """
        Insert the single object into the context dict.
        """
        context = {}
        if self.tasks:
            context['tasks'] = self.tasks
            tasks = self.tasks(self.object)
            if tasks:
                context['tasks'] = self.object
        context.update(kwargs)
        return super(SingleObjectMixin, self).tasks(**context)
    """def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context ["tasks"].filter(user =self.request.user)
        context['count'] = context ["tasks"].filter(complete=False).count()
     #   context['wines_sum'] = Wine.objects.count()
        return context """

class TaskDetail(DetailView):
    model = Task
    paginate_by = 5
    #template_name = 'base/task_detail.html'
    context_object_name = 'task'
    #paginate_by = 5
#now we will build model.py ...here we handle database in dajgo
#we create class as table and all the attribute are the model column

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    #fields = '__all__' #this shows every field we have  
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
    template_name='base/task_form.html'
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task    
    fields = ['title', 'description', 'complete'] 
    success_url = reverse_lazy('tasks')

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task    
    context_object_name = 'task'  
    success_url = reverse_lazy('tasks')



# Create your views here.
#def taskList(request):return HttpResponse('To do list')
    # now we set here the data
       #context['ram'] = "sita"

    #paginate_by = 5
  
       #this function is for getting the data of each user in their own profile    