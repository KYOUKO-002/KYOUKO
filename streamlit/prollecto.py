import streamlit as st

# --- Configuración de página ---
st.set_page_config(
    page_title="Rendimiento Académico",
    page_icon="📊",
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
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 20px;
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

/* Contenedor de navegación centrado */
.sidebar-nav-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    flex-grow: 1;
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
    st.markdown("<div class='sidebar-title'>Rendimiento Académico</div>", unsafe_allow_html=True)
    
    # Inicializar el estado de la sesión si no existe
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "Inicio"
    
    # Contenedor centrado para los botones de navegación
    st.markdown("<div class='sidebar-nav-container'>", unsafe_allow_html=True)
    
    # Botones de navegación
    if st.button("🏠 INICIO", key="home", use_container_width=True):
        st.session_state.current_page = "Inicio"
    
    if st.button("📊 ESTADISTICAS", key="stats", use_container_width=True):
        st.session_state.current_page = "Estadisticas"
    
    if st.button("🔮 PREDICCIONES", key="predictions", use_container_width=True):
        st.session_state.current_page = "Predicciones"
    
    if st.button("📝 BLOG", key="blog", use_container_width=True):
        st.session_state.current_page = "Blog"
    
    st.markdown("</div>", unsafe_allow_html=True)

# --- Contenido Principal ---
if st.session_state.current_page == "Inicio":
    st.markdown("<div class='section-title'>Bienvenido a Rendimiento Académico</div>", unsafe_allow_html=True)
    
    # --- SECCIÓN DE EQUIPO DE DESARROLLO ---
    st.markdown("<div class='section-title' style='margin-top: 20px;'>Equipo de Desarrollo</div>", unsafe_allow_html=True)
    
    # Añadir CSS específico para el equipo
    st.markdown("""
    <style>
    .team-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 30px;
        margin-top: 40px;
    }

    .team-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
        position: relative;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        border: 1px solid rgba(7, 23, 57, 0.1);
    }

    .team-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
    }

    .profile-image {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        margin: 0 auto 20px;
        overflow: hidden;
        border: 4px solid #667eea;
        transition: all 0.3s ease;
        position: relative;
        background-color: #8fb3ff;
    }

    .team-card:hover .profile-image {
        transform: scale(1.1);
        border-color: #764ba2;
    }

    .member-name {
        font-size: 1.4rem;
        font-weight: bold;
        color: #071739;
        margin-bottom: 10px;
    }

    .github-info {
        background: linear-gradient(135deg, #333 0%, #555 100%);
        color: white;
        padding: 12px 20px;
        border-radius: 25px;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        font-size: 0.9rem;
        transition: all 0.3s ease;
        text-decoration: none;
        margin: 10px 0;
    }

    .github-info:hover {
        transform: scale(1.05);
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }

    .github-icon {
        width: 20px;
        height: 20px;
    }

    .role {
        color: #666;
        font-size: 0.9rem;
        margin-top: 10px;
        font-style: italic;
    }

    .stats {
        display: flex;
        justify-content: space-around;
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px solid #eee;
    }

    .stat-item {
        text-align: center;
    }

    .stat-number {
        font-size: 1.2rem;
        font-weight: bold;
        color: #667eea;
    }

    .stat-label {
        font-size: 0.8rem;
        color: #666;
    }
    
    .floating-animation {
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    /* Animaciones para cada tarjeta */
    .delay-0 { animation-delay: 0s; }
    .delay-1 { animation-delay: 0.5s; }
    .delay-2 { animation-delay: 1s; }
    .delay-3 { animation-delay: 1.5s; }
    </style>
    """, unsafe_allow_html=True)
    
    # Grid de miembros del equipo
    with st.container():
        st.markdown("<div class='team-grid'>", unsafe_allow_html=True)
        
        # Miembro 1: Eduardo Mendieta
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("""
            <div class='team-card floating-animation delay-0'>
                <div class='profile-image'></div>
                <h3 class='member-name'>Eduardo Mendieta</h3>
                <div class='role'>Desarrollador Full Stack</div>
                <a href='https://github.com/edwmn01' class='github-info' target='_blank'>
                    <svg class='github-icon' viewBox='0 0 24 24' fill='currentColor'>
                        <path d='M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z'/>
                    </svg>
                    edwmn01
                </a>
                <div class='stats'>
                    <div class='stat-item'>
                        <div class='stat-number'>25</div>
                        <div class='stat-label'>Commits</div>
                    </div>
                    <div class='stat-item'>
                        <div class='stat-number'>8</div>
                        <div class='stat-label'>Repos</div>
                    </div>
                    <div class='stat-item'>
                        <div class='stat-number'>12</div>
                        <div class='stat-label'>Issues</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Miembro 2: Anthony Rosillo
        with col2:
            st.markdown("""
            <div class='team-card floating-animation delay-1'>
                <div class='profile-image'></div>
                <h3 class='member-name'>Anthony Rosillo</h3>
                <div class='role'>Backend Developer</div>
                <a href='https://github.com/rezeranty' class='github-info' target='_blank'>
                    <svg class='github-icon' viewBox='0 0 24 24' fill='currentColor'>
                        <path d='M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z'/>
                    </svg>
                    rezeranty
                </a>
                <div class='stats'>
                    <div class='stat-item'>
                        <div class='stat-number'>32</div>
                        <div class='stat-label'>Commits</div>
                    </div>
                    <div class='stat-item'>
                        <div class='stat-number'>6</div>
                        <div class='stat-label'>Repos</div>
                    </div>
                    <div class='stat-item'>
                        <div class='stat-number'>9</div>
                        <div class='stat-label'>Issues</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Miembro 3: Justin Escalante
        with col3:
            st.markdown("""
            <div class='team-card floating-animation delay-2'>
                <div class='profile-image'></div>
                <h3 class='member-name'>Justin Escalante</h3>
                <div class='role'>Frontend Developer</div>
                <a href='https://github.com/KYOUKO-002' class='github-info' target='_blank'>
                    <svg class='github-icon' viewBox='0 0 24 24' fill='currentColor'>
                        <path d='M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z'/>
                    </svg>
                    KYOUKO-002
                </a>
                <div class='stats'>
                    <div class='stat-item'>
                        <div class='stat-number'>28</div>
                        <div class='stat-label'>Commits</div>
                    </div>
                    <div class='stat-item'>
                        <div class='stat-number'>11</div>
                        <div class='stat-label'>Repos</div>
                    </div>
                    <div class='stat-item'>
                        <div class='stat-number'>7</div>
                        <div class='stat-label'>Issues</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Miembro 4: Evelyn Criollo
        with col4:
            st.markdown("""
            <div class='team-card floating-animation delay-3'>
                <div class='profile-image'></div>
                <h3 class='member-name'>Evelyn Criollo</h3>
                <div class='role'>UI/UX Designer</div>
                <a href='https://github.com/Nidddddddd' class='github-info' target='_blank'>
                    <svg class='github-icon' viewBox='0 0 24 24' fill='currentColor'>
                        <path d='M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z'/>
                    </svg>
                    Nidddddddd
                </a>
                <div class='stats'>
                    <div class='stat-item'>
                        <div class='stat-number'>19</div>
                        <div class='stat-label'>Commits</div>
                    </div>
                    <div class='stat-item'>
                        <div class='stat-number'>5</div>
                        <div class='stat-label'>Repos</div>
                    </div>
                    <div class='stat-item'>
                        <div class='stat-number'>15</div>
                        <div class='stat-label'>Issues</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
# Estadisticas
elif st.session_state.current_page == "Estadisticas":
    st.markdown("<div class='section-title'>Estadísticas Académicas</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-subtitle'>Análisis detallado del rendimiento estudiantil</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class='card'>
            <h3 style='color: #071739; margin-bottom: 20px;'>📈 Análisis de Rendimiento</h3>
            <p style='color: #071739; opacity: 0.8; margin-bottom: 20px;'>
                Visualizaciones detalladas del desempeño académico, tendencias de calificaciones
                y análisis comparativo por materias y períodos.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='card' style='text-align: center;'>
            <h4 style='color: #071739;'>Métricas Clave</h4>
            <p style='color: #071739; opacity: 0.8;'>
                Promedio General<br>
                Materias Aprobadas<br>
                Asistencia<br>
                Tendencias<br>
                Comparativas
            </p>
        </div>
        """, unsafe_allow_html=True)

# Predicciones
elif st.session_state.current_page == "Predicciones":
    st.markdown("<div class='section-title'>Predicciones Académicas</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-subtitle'>Modelos predictivos para el rendimiento estudiantil</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class='card'>
            <h3 style='color: #071739; margin-bottom: 20px;'>🔮 Modelos Predictivos</h3>
            <p style='color: #071739; opacity: 0.8; margin-bottom: 20px;'>
                Algoritmos avanzados de machine learning para predecir el rendimiento académico
                futuro basado en datos históricos y patrones de comportamiento.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='card' style='text-align: center;'>
            <h4 style='color: #071739;'>Algoritmos</h4>
            <p style='color: #071739; opacity: 0.8;'>
                Regresión Lineal<br>
                Random Forest<br>
                Neural Networks<br>
                SVM<br>
                Time Series
            </p>
        </div>
        """, unsafe_allow_html=True)

# Blog
elif st.session_state.current_page == "Blog":
    st.markdown("<div class='section-title'>Blog Académico</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-subtitle'>Artículos y recursos sobre educación y análisis de datos</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='card'>
            <h3 style='color: #071739; text-align: center; margin-bottom: 20px;'>📝 Artículos Recientes</h3>
        </div>
        """, unsafe_allow_html=True)
        st.success("📖 Cómo interpretar las métricas académicas")
        st.info("🔍 Análisis de tendencias educativas 2024")
        st.warning("💡 Mejores prácticas en evaluación estudiantil")
    
    with col2:
        st.markdown("""
        <div class='card'>
            <h3 style='color: #071739; text-align: center; margin-bottom: 20px;'>🎯 Recursos</h3>
        </div>
        """, unsafe_allow_html=True)
        st.success("📊 Guías de análisis de datos")
        st.info("🔧 Herramientas recomendadas")
        st.warning("📚 Bibliografía especializada")