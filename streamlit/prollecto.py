import streamlit as st

# --- Configuración de página ---
st.set_page_config(
    page_title="Mi Portafolio",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
    padding-top: 2rem;
}

/* Estilo del sidebar */
.css-1d391kg {
    background-color: rgba(255, 255, 255, 0.95) !important;
    border-right: 2px solid #071739;
}

/* Títulos del sidebar */
.sidebar-title {
    font-size: 24px;
    color: #071739;
    font-weight: 700;
    margin-bottom: 30px;
    text-align: center;
    padding: 20px 0;
    border-bottom: 2px solid #8fb3ff;
}

/* Botones del sidebar */
.sidebar-nav-item {
    display: block;
    width: 100%;
    padding: 15px 20px;
    margin: 8px 0;
    background-color: transparent;
    border: 2px solid #8fb3ff;
    border-radius: 10px;
    color: #071739;
    text-decoration: none;
    font-weight: 600;
    transition: all 0.3s ease;
    cursor: pointer;
}

.sidebar-nav-item:hover {
    background-color: #8fb3ff;
    color: white;
    transform: translateX(5px);
}

.sidebar-nav-item.active {
    background-color: #071739;
    color: white;
    border-color: #071739;
}

/* Títulos de sección principales */
.section-title {
    font-size: 42px;
    color: #071739;
    margin-bottom: 30px;
    text-align: center;
    font-weight: 700;
    animation: slideInLeft 0.8s ease-in-out;
}

.section-subtitle {
    font-size: 18px;
    color: #071739;
    margin-bottom: 40px;
    text-align: center;
    opacity: 0.8;
    animation: fadeIn 1s ease-in-out;
}

/* Imágenes animadas */
img {
    animation: fadeIn 1s ease-in-out;
    transition: transform 0.3s ease;
    border-radius: 12px;
    box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
}

img:hover {
    transform: scale(1.05);
    box-shadow: 0px 8px 20px rgba(0,0,0,0.2);
}

/* Tarjetas */
.card {
    background-color: rgba(255,255,255,0.85);
    padding: 24px;
    border-radius: 16px;
    box-shadow: 0px 6px 12px rgba(0,0,0,0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    margin-bottom: 24px;
    border: 1px solid rgba(255,255,255,0.3);
}

.card:hover {
    transform: translateY(-10px);
    box-shadow: 0px 12px 24px rgba(0,0,0,0.2);
}

/* Métricas mejoradas */
.metric-container {
    background-color: rgba(255,255,255,0.9);
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
    margin: 10px 0;
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

/* Responsive */
@media (max-width: 768px) {
    .section-title {
        font-size: 32px;
    }
    .card {
        padding: 16px;
    }
}
</style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
with st.sidebar:
    st.markdown("<div class='sidebar-title'>🎨 Mi Portafolio</div>", unsafe_allow_html=True)
    
    # Inicializar el estado de la sesión si no existe
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "Inicio"
    
    # Botones de navegación
    if st.button("🏠 Inicio", key="home", use_container_width=True):
        st.session_state.current_page = "Inicio"
    
    if st.button("🖼️ Portafolio", key="portfolio", use_container_width=True):
        st.session_state.current_page = "Portafolio"
    
    if st.button("📁 Proyectos", key="projects", use_container_width=True):
        st.session_state.current_page = "Proyectos"
    
    if st.button("🏆 Reconocimientos", key="awards", use_container_width=True):
        st.session_state.current_page = "Reconocimientos"
    
    # Información adicional en el sidebar
    st.markdown("---")
    st.markdown("### 📊 Estadísticas")
    st.metric("Proyectos", "12", "3")
    st.metric("Clientes", "45", "8")
    st.metric("Años Exp.", "5", "1")

# --- Contenido Principal ---
# Inicio
if st.session_state.current_page == "Inicio":
    st.markdown("<div class='section-title'>Bienvenido a Mi Portafolio</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-subtitle'>Diseñador y desarrollador especializado en experiencias digitales modernas</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class='card'>
            <h3 style='color: #071739; text-align: center; margin-bottom: 20px;'>Sobre Mí</h3>
            <p style='color: #071739; text-align: center; line-height: 1.6;'>
                Esta es una plantilla base inspirada en sitios modernos. Aquí puedes integrar 
                visualizaciones, datos y estilo personalizado para crear experiencias únicas 
                que conecten con tu audiencia.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Sección de habilidades
    st.markdown("---")
    st.markdown("### 🚀 Mis Habilidades")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='metric-container'>
            <h4 style='color: #071739;'>Diseño UI/UX</h4>
            <p style='color: #071739; opacity: 0.8;'>Interfaces modernas y funcionales</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='metric-container'>
            <h4 style='color: #071739;'>Desarrollo Web</h4>
            <p style='color: #071739; opacity: 0.8;'>Aplicaciones responsivas y optimizadas</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='metric-container'>
            <h4 style='color: #071739;'>Análisis de Datos</h4>
            <p style='color: #071739; opacity: 0.8;'>Visualizaciones e insights</p>
        </div>
        """, unsafe_allow_html=True)

# Portafolio
elif st.session_state.current_page == "Portafolio":
    st.markdown("<div class='section-title'>Portafolio Visual</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-subtitle'>Explora mis proyectos más destacados</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.image("https://cdn.thenifty.com/portal-assets/img/phase_zero.jpg", caption="Proyecto Alpha - Diseño Innovador")
        st.markdown("""
        <div style='padding: 10px 0;'>
            <h4 style='color: #071739; margin: 0;'>Proyecto Alpha</h4>
            <p style='color: #071739; opacity: 0.8; margin: 5px 0;'>
                Una aplicación web moderna con enfoque en la experiencia del usuario
                y diseño responsive.
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.image("https://cdn.thenifty.com/portal-assets/img/phase_one.jpg", caption="Proyecto Beta - Desarrollo Avanzado")
        st.markdown("""
        <div style='padding: 10px 0;'>
            <h4 style='color: #071739; margin: 0;'>Proyecto Beta</h4>
            <p style='color: #071739; opacity: 0.8; margin: 5px 0;'>
                Plataforma de análisis de datos con visualizaciones interactivas
                y dashboard personalizable.
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Galería adicional
    st.markdown("---")
    st.markdown("### 🎨 Más Trabajos")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.image("https://via.placeholder.com/300x200/8fb3ff/071739?text=Proyecto+Gamma", 
                caption="Proyecto Gamma")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.image("https://via.placeholder.com/300x200/071739/8fb3ff?text=Proyecto+Delta", 
                caption="Proyecto Delta")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.image("https://via.placeholder.com/300x200/8fb3ff/071739?text=Proyecto+Epsilon", 
                caption="Proyecto Epsilon")
        st.markdown("</div>", unsafe_allow_html=True)

# Proyectos
elif st.session_state.current_page == "Proyectos":
    st.markdown("<div class='section-title'>Proyectos Analíticos</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-subtitle'>Dashboards de datos, gráficos y predicciones de modelos</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class='card'>
            <h3 style='color: #071739; margin-bottom: 20px;'>🔍 Análisis de Datos</h3>
            <p style='color: #071739; opacity: 0.8; margin-bottom: 20px;'>
                Herramientas avanzadas para el análisis y visualización de grandes conjuntos de datos,
                incluyendo machine learning y predicciones en tiempo real.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='card' style='text-align: center;'>
            <h4 style='color: #071739;'>Tecnologías</h4>
            <p style='color: #071739; opacity: 0.8;'>
                Python<br>
                Pandas<br>
                Plotly<br>
                Streamlit<br>
                SQL
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Simulación de datos
    st.markdown("---")
    if st.button("🚀 Simular Modelo de Datos", use_container_width=True):
        import numpy as np
        import pandas as pd
        
        # Generar datos simulados
        data = {
            'Mes': ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'],
            'Ventas': np.random.randint(100, 1000, 6),
            'Usuarios': np.random.randint(50, 500, 6)
        }
        df = pd.DataFrame(data)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 📊 Datos Simulados")
            st.dataframe(df, use_container_width=True)
        
        with col2:
            st.markdown("#### 📈 Gráfico de Ventas")
            st.line_chart(df.set_index('Mes')['Ventas'])

# Reconocimientos
elif st.session_state.current_page == "Reconocimientos":
    st.markdown("<div class='section-title'>Premios y Reconocimientos</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-subtitle'>Logros destacados en mi carrera profesional</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='card'>
            <h3 style='color: #071739; text-align: center; margin-bottom: 20px;'>🏆 Premios Principales</h3>
        </div>
        """, unsafe_allow_html=True)
        st.success("🏆 Awwwards: Mejor diseño emergente 2024")
        st.info("🎖️ CSSDA: UI/UX Destacado 2023")
        st.warning("🥇 FWA: Sitio del Día 2023")
    
    with col2:
        st.markdown("""
        <div class='card'>
            <h3 style='color: #071739; text-align: center; margin-bottom: 20px;'>🎯 Certificaciones</h3>
        </div>
        """, unsafe_allow_html=True)
        st.success("✅ Google UX Design Certificate")
        st.info("✅ AWS Cloud Practitioner")
        st.warning("✅ Python Data Analysis")
    
    # Timeline de logros
    st.markdown("---")
    st.markdown("### 📅 Timeline de Logros")
    
    timeline_data = {
        "2024": "🏆 Awwwards - Mejor diseño emergente",
        "2023": "🎖️ CSSDA - UI/UX Destacado",
        "2023": "🥇 FWA - Sitio del Día",
        "2022": "🎓 Graduación en Diseño Digital"
    }
    
    for year, achievement in timeline_data.items():
        st.markdown(f"""
        <div class='card'>
            <h4 style='color: #071739; margin: 0;'>{year}</h4>
            <p style='color: #071739; opacity: 0.8; margin: 5px 0;'>{achievement}</p>
        </div>
        """, unsafe_allow_html=True)