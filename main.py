from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def inicio(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")



@app.post("/enviar")
async def enviar_mensaje(usuario: str = Form(...), contraseña: str = Form(...)):
    usuario_correcto = "jhon"
    contraseña_correcto = "1234" 
    
    if usuario == usuario_correcto and contraseña == contraseña_correcto:
        return RedirectResponse(url="/bienvenido", status_code=303)
    else:
        return RedirectResponse(url="/", status_code=303)
    
@app.get("/bienvenido")
async def inicio(request: Request):
    return templates.TemplateResponse(request=request, name="bienvenido.html")



