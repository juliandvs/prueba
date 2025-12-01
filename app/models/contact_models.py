from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    nombre: str
    correo: str
    telefono: str
    
class dejar_nota(BaseModel):
    correo: str
    nota: str
    
class actualizar_usuario(BaseModel):
    correo: str
    nombre: Optional[str] = None
    telefono: Optional[str] = None
    estado: Optional[str] = None