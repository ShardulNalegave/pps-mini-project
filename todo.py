
import uuid

class Todo:
  def __init__(self, title: str, completed: bool = False):
    self.id = uuid.uuid4().hex
    self.title = title
    self.completed = completed