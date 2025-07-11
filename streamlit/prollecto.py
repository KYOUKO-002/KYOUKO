import streamlit as st

# --- CSS Avanzado con Fondo, Tipografía, Hover y Animaciones ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700&display=swap');

/* Aplica fondo a toda la aplicación */
.stApp {
    background-color: #8fb3ff !important;
    font-family: 'Outfit', sans-serif;
}

/* Elimina fondo blanco de secciones internas */
.block-container {
    background-color: transparent !important;
}

/* Títulos animados */
.section-title {
    font-size: 32px;
    color: #071739;
    margin-top: 40px;
    border-bottom: 1px solid #071739;
    padding-bottom: 10px;
    animation: slideInLeft 0.8s ease-in-out;
}

/* Imágenes animadas */
img {
    animation: fadeIn 1s ease-in-out;
    transition: transform 0.3s ease;
    border-radius: 10px;
}

img:hover {
    transform: scale(1.03);
    box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
}

/* Tarjetas */
.card {
    background-color: rgba(255,255,255,0.7);
    padding: 16px;
    border-radius: 12px;
    box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    margin-bottom: 20px;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0px 8px 16px rgba(0,0,0,0.2);
}

/* Animaciones */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes slideInLeft {
    from {
        opacity: 0;
        transform: translateX(-50px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}
</style>
""", unsafe_allow_html=True)

# --- Tabs / Secciones ---
tabs = st.tabs(["🏠 Inicio", "🖼️ Portafolio", "📁 Proyectos", "🏆 Reconocimientos"])

# Inicio
with tabs[0]:
    st.markdown("<div class='section-title'>Bienvenido</div>", unsafe_allow_html=True)
    st.write("Esta es una plantilla base inspirada en sitios modernos. Aquí puedes integrar visualizaciones, datos y estilo personalizado.")

# Portafolio
with tabs[1]:
    st.markdown("<div class='section-title'>Portafolio Visual</div>", unsafe_allow_html=True)
    
    st.markdown("<div style='margin-top: 30px;'>", unsafe_allow_html=True)  # Añadido

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.image("https://cdn.thenifty.com/portal-assets/img/phase_zero.jpg", caption="Proyecto Alpha")
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.image("https://cdn.thenifty.com/portal-assets/img/phase_one.jpg", caption="Proyecto Beta")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# Proyectos
with tabs[2]:
    st.markdown("<div class='section-title'>Proyectos Analíticos</div>", unsafe_allow_html=True)
    st.write("Aquí puedes cargar dashboards de datos, gráficos de big data o predicciones de modelos.")
    st.button("Simular Modelo de Datos")

# Reconocimientos
with tabs[3]:
    st.markdown("<div class='section-title'>Premios y Reconocimientos</div>", unsafe_allow_html=True)
    st.success("🏆 Awwwards: Mejor diseño emergente 2024")
    st.info("🎖 CSSDA: UI/UX Destacado 2023")