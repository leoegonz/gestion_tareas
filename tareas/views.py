from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea  # modelo Tarea definido
from .forms import TareaForm  # Importamos el formulario
# Create your views here.
###  return render(request, 'tareas/vista.html', {'nombre': nombre}) #diccionario con clave y valor

# Vista para la lista de tareas

def lista_tareas(request):
    tareas = Tarea.objects.all()  # Obtener todas las tareas
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})

# Vista para crear una nueva tarea
def crear_tarea(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():  # Validamos los datos del formulario
            form.save()
            return redirect('lista_tareas')  # Redirigimos a la lista de tareas
    else:
        form = TareaForm()  # Si el método es GET, mostramos un formulario vacío

    return render(request, 'tareas/crear_tarea.html', {'form': form})

# Vista para editar una tarea
def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)

    if request.method == "POST":
        form = TareaForm(request.POST, instance=tarea)  # Pasamos la tarea a editar
        if form.is_valid():  # Validamos el formulario
            form.save()
            return redirect('lista_tareas')  # Redirigimos a la lista de tareas
    else:
        form = TareaForm(instance=tarea)  # Mostramos los datos de la tarea en el formulario

    return render(request, 'tareas/editar_tarea.html', {'form': form, 'tarea': tarea})

# Vista para eliminar una tarea
def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=id)

    if request.method == "POST":
        tarea.delete()  # Eliminamos la tarea
        return redirect('lista_tareas')  # Redirigimos a la lista de tareas

    return render(request, 'tareas/eliminar_tarea.html', {'tarea': tarea})
