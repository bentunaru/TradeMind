import streamlit as st
import os
from dotenv import load_dotenv
from utils.database import save_user_config, get_user_config
import uuid

# Charger les variables d'environnement
load_dotenv()

# Configuration de la page
st.set_page_config(
    page_title="Onboarding - TradeMind",
    page_icon="🚀",
    layout="wide"
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
    .stButton>button {
        background-color: #2B2D42;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Titre de la page
st.title("Configuration Initiale")
st.markdown("---")

# Vérifier si l'utilisateur a déjà une configuration
if 'user_id' not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

existing_config = get_user_config(st.session_state.user_id)
if existing_config:
    st.warning("Vous avez déjà une configuration. Souhaitez-vous la modifier ?")
    if st.button("Modifier la configuration"):
        st.session_state.edit_mode = True
    else:
        st.stop()

# Formulaire d'onboarding
with st.form("onboarding_form"):
    st.markdown("### Questionnaire Initial")
    
    # Section 1: Informations de base
    col1, col2 = st.columns(2)
    with col1:
        ict_level = st.selectbox(
            "Niveau ICT",
            ["Débutant", "Intermédiaire", "Avancé"],
            help="Sélectionnez votre niveau de connaissance des concepts ICT"
        )
    
    with col2:
        starting_capital = st.number_input(
            "Capital de départ ($)",
            min_value=100,
            value=1000,
            step=100,
            help="Montant initial de votre capital de trading"
        )
    
    risk_per_trade = st.slider(
        "Risque par trade (%)",
        min_value=0.5,
        max_value=5.0,
        value=2.0,
        step=0.5,
        help="Pourcentage du capital risqué par trade"
    )
    
    st.markdown("### Quick Setup")
    
    # Section 2: Configuration technique
    indicators = st.multiselect(
        "Indicateurs préférés",
        ["RSI", "MACD", "Bollinger Bands", "Moving Averages", "Volume Profile"],
        default=["RSI", "Moving Averages"],
        help="Sélectionnez les indicateurs que vous utilisez régulièrement"
    )
    
    timeframes = st.multiselect(
        "Timeframes",
        ["1m", "5m", "15m", "1h", "4h", "1d", "1w"],
        default=["5m", "15m", "1h", "4h"],
        help="Timeframes que vous analysez"
    )
    
    # Section 3: Checklists
    st.markdown("### Checklists")
    
    continuation_checklist = st.multiselect(
        "Checklist Continuation",
        [
            "Higher High / Higher Low confirmé",
            "Volume en hausse",
            "RSI > 50",
            "EMA 20 > EMA 50",
            "Liquidity zone identifiée"
        ],
        default=["Higher High / Higher Low confirmé", "Volume en hausse"],
        help="Éléments à vérifier pour un setup de continuation"
    )
    
    reversal_checklist = st.multiselect(
        "Checklist Reversal",
        [
            "Divergence RSI",
            "Volume en hausse",
            "Liquidity zone testée",
            "Structure cassée",
            "FVG présent"
        ],
        default=["Divergence RSI", "Liquidity zone testée"],
        help="Éléments à vérifier pour un setup de reversal"
    )
    
    # Bouton de soumission
    submitted = st.form_submit_button("Commencer")
    
    if submitted:
        # Validation des données
        if not indicators:
            st.error("Veuillez sélectionner au moins un indicateur")
        elif not timeframes:
            st.error("Veuillez sélectionner au moins un timeframe")
        else:
            try:
                # Préparation des données
                config_data = {
                    "ict_level": ict_level,
                    "starting_capital": starting_capital,
                    "risk_per_trade": risk_per_trade,
                    "indicators": indicators,
                    "timeframes": timeframes,
                    "continuation_checklist": continuation_checklist,
                    "reversal_checklist": reversal_checklist
                }
                
                # Sauvegarde dans Supabase
                save_user_config(st.session_state.user_id, config_data)
                
                # Message de succès
                st.success("Configuration enregistrée avec succès !")
                st.balloons()
                
                # Redirection vers le dashboard
                st.markdown("Redirection vers le dashboard...")
                st.experimental_rerun()
                
            except Exception as e:
                st.error(f"Une erreur est survenue lors de l'enregistrement : {str(e)}") 