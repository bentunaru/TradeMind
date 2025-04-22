import streamlit as st
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Configuration de la page
st.set_page_config(
    page_title=os.getenv("APP_TITLE", "TradeMind - Journal de Trading IA"),
    page_icon=os.getenv("APP_ICON", "📊"),
    layout="wide",
    initial_sidebar_state="expanded"
)

# Styles CSS personnalisés
st.markdown("""
    <style>
    .main {
        background-color: #EDF2F4;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    </style>
""", unsafe_allow_html=True)

# Titre de l'application
st.title("TradeMind - Journal de Trading IA")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.image("assets/logo.png", width=200)
    st.markdown("## Navigation")
    st.markdown("""
    - 📊 Dashboard
    - 📝 Journal
    - 📈 Analyse
    - 🤖 Coaching
    - ⚙️ Paramètres
    """)

# Contenu principal
st.markdown("""
    ## Bienvenue sur TradeMind
    
    Votre assistant IA pour le trading professionnel.
    
    ### Fonctionnalités principales :
    - Journal de trading structuré
    - Analyse multi-timeframe
    - Feedback IA basé sur les setups ICT
    - Dashboard de performance
    - Export de rapports
""")

# Vérification des variables d'environnement
if not os.getenv("SUPABASE_URL") or not os.getenv("SUPABASE_KEY"):
    st.warning("⚠️ Configuration Supabase manquante. Veuillez configurer les variables d'environnement.")
if not os.getenv("OPENAI_API_KEY"):
    st.warning("⚠️ Clé API OpenAI manquante. Veuillez configurer les variables d'environnement.") 