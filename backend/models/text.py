from pydantic import BaseModel

class TextInput(BaseModel):
    text: str

class TextOutput(BaseModel):
    corrected_text: str
