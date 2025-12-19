import streamlit as st
from supabase import create_client, Client

# ---------------------------------
# CONFIGURACIÓN SUPABASE
# ---------------------------------
SUPABASE_URL = "https://nxambvgqormhaykxtvim.supabase.co"
SUPABASE_KEY = "sb_secret_X-fnD5aPgSVbnAYnkHpWoA_dkOC5d5M"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ---------------------------------
# FUNCIONES PARA OBTENER DATOS
# ---------------------------------

def obtener_pacientes():
    try:
        response = supabase.table("pacientes").select("*").execute()
        return response.data if response.data else []
    except Exception as e:
        st.error(f"Error al obtener pacientes: {e}")
        return []

def obtener_historial():
    try:
        response = supabase.table("historial").select("*").execute()
        return response.data if response.data else []
    except Exception as e:
        st.error(f"Error al obtener historial clínico: {e}")
        return []

def obtener_tratamientos():
    try:
        response = supabase.table("tratamientos").select("*").execute()
        return response.data if response.data else []
    except Exception as e:
        st.error(f"Error al obtener tratamientos: {e}")
        return []


# ---------------------------------
# INTERFAZ
# ---------------------------------

st.title("Sistema Clínico - Sele Dent")

menu = st.sidebar.selectbox(
    "Menú",
    ["Pacientes", "Historial Clínico", "Tratamientos"]
)

# ---------------------------------
# OPCIÓN 1: VER PACIENTES
# ---------------------------------
if menu == "Pacientes":
    st.header("🧑‍⚕️ Lista de Pacientes Registrados")

    pacientes = obtener_pacientes()

    if pacientes:
        st.success(f"Pacientes encontrados: {len(pacientes)}")
        st.table(pacientes)
    else:
        st.warning("No hay pacientes registrados.")


# ---------------------------------
# OPCIÓN 2: VER HISTORIAL CLÍNICO
# ---------------------------------
elif menu == "Historial Clínico":
    st.header("📘 Historial Clínico de Pacientes")

    historial = obtener_historial()

    if historial:
        st.success(f"Registros encontrados: {len(historial)}")
        st.table(historial)
    else:
        st.warning("No hay historial registrado.")


# ---------------------------------
# OPCIÓN 3: VER TRATAMIENTOS
# ---------------------------------
elif menu == "Tratamientos":
    st.header("💊 Tratamientos Realizados")

    tratamientos = obtener_tratamientos()

    if tratamientos:
        st.success(f"Tratamientos encontrados: {len(tratamientos)}")
        st.table(tratamientos)
    else:
        st.warning("No hay tratamientos registrados.")

