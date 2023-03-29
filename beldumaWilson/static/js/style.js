let Pais = [];
const listarPaises = async (codigo) => {
    try {
        const response = await fetch("/paises/");
        const data = await response.json();
        if (data.message === "Success") {
            let opciones = ``;
            data.paises.forEach((paises) => {
                aux_codigo = `${paises.id}`;
                if(parseInt(aux_codigo) ==  parseInt(codigo) ){
                    opciones = `<option value='${paises.id}'> ${paises.nombre} </option>`;
                    txtnacionalidad1.innerHTML = `<input class="form-control" type="text" value='${paises.nacionalidad}'>`;;
                }
            });
            data.paises.forEach((pais) => {
                opciones += `<option value='${pais.id}'>${pais.nombre}</option>`;
            });
            txtpais.innerHTML = opciones;
        } else {
            alert("Países no encontrados...");
        }
    } catch (error) {
        console.log(error);
    }
};

const listarNacionalidad = async (idPais) => {
    try {
        const response = await fetch(`/nacionalidad/${idPais}`);
        const data = await response.json();
        if (data.message === "Success") {
            ciudades = data.nacionalidad;
            let opciones = ``;
            ciudades.forEach((ciudad) => {
                opciones = `<input class="form-control" type="text" value='${ciudad.nacionalidad}'>`;
            });
            txtnacionalidad1.innerHTML = opciones;
        } else {
            alert("Países no encontrados...");
        }
    } catch (error) {
        console.log(error);
    }
};

const cargainicial = async () => {
    var codigoNacionalidad = document.getElementById("codigoNacionalidad").value;
    await listarNacionalidad(1);
    await listarPaises(codigoNacionalidad);
    txtpais.addEventListener("change", (event) => {
        listarNacionalidad(event.target.value);
    });
}

window.addEventListener("load", async () => {
    await cargainicial();
});

function calcularEdad() {
    var fecha_nacimiento = document.getElementById("fechaNacimiento").value;
    var hoy = new Date();
    var cumpleanos = new Date(fecha_nacimiento);
    var edad = hoy.getFullYear() - cumpleanos.getFullYear();
    var m = hoy.getMonth() - cumpleanos.getMonth();
    if (m < 0 || (m === 0 && hoy.getDate() < cumpleanos.getDate())) {
        edad--;
    }
    if (edad > 18) {
        document.getElementById('mensaje').innerHTML = '<p style="color:green">Campo validado</p>';
        return true;
    } else {
        document.getElementById('mensaje').innerHTML = '<p style="color:red">Debe ser mayor de edad</p>';
        return false;
    }
}




