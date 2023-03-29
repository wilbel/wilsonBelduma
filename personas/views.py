from django.shortcuts import render
from .models import Persona
from .models import Pais
from django.http import HttpRequest,JsonResponse


# Create your views here.

class FormularioPersonaView(HttpRequest):
    def index(request):
        get_pais = Pais.objects.all()
        data = {
            'get_pais': get_pais
        }
        #return render(request,'home.html',{"form":persona})
        return render(request,'home.html',data)
        
    

    def procesar_formulario(request):
        try:
            cod = request.POST['codigo']
            nombre = request.POST['nombre']
            fechaNacimiento = request.POST['fechaNacimiento']
            codigo_pais = request.POST['pais']
            persona = Persona(codigo=cod,nombre=nombre,nacimiento=fechaNacimiento,nacionalidad_id=codigo_pais)
            persona.save()
            persona = Persona()
            get_personas = Persona.objects.all()
            data = {
                'get_personas': get_personas
            }
            #return render(request,"home.html",{"form":persona,"mensaje":"ok"})
            return render(request,"personaslista.html",data)
        except:
            return render(request,"home.html",{"form":persona,"mensaje":"ok"})


    def showformActualizar(request,id):
        try:
            inter = Persona.objects.get(codigo=id)
            fa = inter.nacimiento
            if fa.day>=1 and fa.day<=9:
                dia = "0" + str(fa.day)
            else:
                dia = str(fa.day)

            if fa.month>=1 and fa.month<=9:
                mes = "0" + str(fa.month)
            else:
                mes = str(fa.month)
            fecha = str(fa.year) + "-" + mes + "-"+ dia
        
            datos={
                'inter':inter,
                'fecha':fecha
            }

            return render(request,'form_actualizar.html',datos)
        except:
            #listper = Persona.objects.all()
            return render(request,'personaslista.html')
        

    def actualizarPersona(request, id):
        try:
            cod = request.POST['codigo']
            nombre = request.POST['nombre']
            fechaNacimiento = request.POST['fechaNacimiento']
            codigo_pais = request.POST['pais']
            pers = Persona.objects.get(id=id)
            pers.codigo=cod
            pers.nombre=nombre
            pers.nacimiento = fechaNacimiento
            pers.nacionalidad_id=codigo_pais
            pers.save()
        except:
            listper = Persona.objects.all()
            return render(request,'personaslista.html',listper)
        persona = Persona()
        get_personas = Persona.objects.all()
        data = {
            'get_personas': get_personas
        }

        return render(request,"personaslista.html",data)
    
    def get_pais(request):
        paises = list(Pais.objects.values())

        if(len(paises)>0):
            data = {'message':"Success", 'paises':paises}
        else:
            data = {'message':'Not Found'}

        return JsonResponse(data)
    
    def get_nacionalidad(request,idpais):
        pais = list(Pais.objects.filter(id=idpais).values())
        data = {'message':"Success",'nacionalidad':pais}
        return JsonResponse(data)
    

    def obtener_pais(request):
        get_pais = Pais.objects.all()
        data = {
            'get_pais': get_pais
        }
        return render(request,'form_actualizar.html',data)
        





def personalist(request):
    get_personas = Persona.objects.all()

    data = {
        'get_personas': get_personas
    }
    return render(request,'personaslista.html',data)

