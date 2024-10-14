from models.task import Task, db

class TaskRepository:

    @staticmethod
    def create_task(name, description):
        # Buscar si existe una tarea con el mismo nombre
        existing_task = Task.query.filter_by(name=name).first()#db.session.query.filter_by(name=name).first()
        
        if existing_task:
            # Si existe, actualizar la descripción
            existing_task.description = description
            db.session.commit()
            # la sugerencia de gemini fue, pero priorizamos la accion de task controller
            # return jsonify(existing_task.to_json()), 200  # Retornamos 200 (OK) ya que actualizamos un registro existente
            # al ver que arroja error pues task no se definio entonces agragamos
            task = existing_task
        else: 
            task = Task(name=name, description=description)
            db.session.add(task)
            db.session.commit()
        return task