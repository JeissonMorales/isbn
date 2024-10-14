# Esta version incluye el reto:
*Añadir una funcionalidad que permita modificar una tarea ya creada.*

## implementacion:
Para permitir de forma rapida y sencilla que las tareas sean modificables (en su descripcion), el metodo **TaskRepository.create_task** primero valida si existe un registro en la base de datos con ese nombre de tarea y si existe modifica la descripcion, de lo contrario crea un nuevo registro en la base de datos, de modo que, solo actualizamos la descripcion de una tarea ya existente, identificandola con su nombre. 

### Nota:
Tenemos en cuenta que el frontend es bastante basico, que no muestra al usuario informacion sobre la tarea recien creada ni las demas existentes, de modo que, considero que esta implementacion es suficiente, si ir mas alla modificando el frontend.