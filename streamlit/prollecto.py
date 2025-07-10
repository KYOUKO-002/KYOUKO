# streamlit_app.py
import streamlit as st

# --- CSS Limpio con animaciones suaves ---
st.markdown("""
<style>
body {
    background-color: #ffffff;
    color: #071739;
    font-family: 'Poppins', sans-serif;
    overflow-x: hidden;
}

.section-title {
    font-size: 32px;
    color: #071739;
    margin-top: 40px;
    border-bottom: 1px solid #071739;
    padding-bottom: 10px;
    animation: fadeIn 1s ease-in-out;
}

img {
    animation: fadeIn 1s ease-in-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)

# --- Tabs / Secciones ---
tabs = st.tabs(["Inicio", "Portafolio", "Proyectos", "Reconocimientos"])

with tabs[0]:
    st.markdown("<div class='section-title'>Bienvenido</div>", unsafe_allow_html=True)
    st.write("Esta es una plantilla base inspirada en sitios modernos. Aquí puedes integrar visualizaciones, datos y estilo personalizado.")

with tabs[1]:
    st.markdown("<div class='section-title'>Portafolio Visual</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://cdn.thenifty.com/portal-assets/img/phase_zero.jpg", caption="Proyecto Alpha")
    with col2:
        st.image("https://cdn.thenifty.com/portal-assets/img/phase_one.jpg", caption="Proyecto Beta")

with tabs[2]:
    st.markdown("<div class='section-title'>Proyectos Analíticos</div>", unsafe_allow_html=True)
    st.write("Aquí puedes cargar dashboards de datos, gráficos de big data o predicciones de modelos.")
    st.button("Simular Modelo de Datos")

with tabs[3]:
    st.markdown("<div class='section-title'>Premios y Reconocimientos</div>", unsafe_allow_html=True)
    st.success("🏆 Awwwards: Mejor diseño emergente 2024")
    st.info("🎖 CSSDA: UI/UX Destacado 2023")
