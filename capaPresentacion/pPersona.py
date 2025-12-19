import streamlit as st
import pandas as pd
from datetime import date
from capaLogica.dPersona import LPersona

class PPersonas:

    def __init__(self):
        self.lpersona = LPersona()

    def run(self):

        st.set_page_config(page_title="Sele Dent", layout="wide")
        st.title("Sistema Clínico - Sele Dent")

        menu = st.sidebar.selectbox(
            "Menú",
            [
                "Registrar Paciente",
                "Ver Pacientes",
                "Actualizar Paciente",
                "Eliminar Paciente"
            ]
        )

        if menu == "Registrar Paciente":
            with st.form("form_paciente"):
                dni = st.text_input("DNI")
                nombres = st.text_input("Nombres")
                apepaterno = st.text_input("Apellido Paterno")
                apematerno = st.text_input("Apellido Materno")
                fecha = st.date_input("Fecha nacimiento", date(2000,1,1))
                telefono = st.text_input("Teléfono")
                correo = st.text_input("Correo")
                contrasenia = st.text_input("Contraseña", type="password")
                genero = st.selectbox("Género", ["M", "F"])
                guardar = st.form_submit_button("Guardar")

            if guardar:
                persona = {
                    "dni": dni,
                    "nombres": nombres,
                    "apepaterno": apepaterno,
                    "apematerno": apematerno,
                    "fecha_nacimiento": str(fecha),
                    "telefono": telefono,
                    "correo": correo,
                    "contrasenia": contrasenia,
                    "genero": genero
                }
                self.lpersona.insertarPersona(persona)
                st.success("Paciente registrado")

        elif menu == "Ver Pacientes":
            pacientes = self.lpersona.mostrarPersona()
            if pacientes:
                st.dataframe(pd.DataFrame(pacientes), use_container_width=True)
            else:
                st.warning("No hay pacientes")
