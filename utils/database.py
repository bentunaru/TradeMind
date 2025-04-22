from supabase import create_client
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Initialisation du client Supabase
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

if not supabase_url or not supabase_key:
    raise ValueError("Les variables d'environnement Supabase ne sont pas configurées")

supabase = create_client(supabase_url, supabase_key)

def save_user_config(user_id, config_data):
    """
    Sauvegarde la configuration utilisateur dans Supabase
    
    Args:
        user_id (str): ID de l'utilisateur
        config_data (dict): Données de configuration
    
    Returns:
        dict: Réponse de Supabase
    """
    data = {
        "user_id": user_id,
        "ict_level": config_data["ict_level"],
        "starting_capital": config_data["starting_capital"],
        "risk_per_trade": config_data["risk_per_trade"],
        "indicators": config_data["indicators"],
        "timeframes": config_data["timeframes"],
        "continuation_checklist": config_data["continuation_checklist"],
        "reversal_checklist": config_data["reversal_checklist"]
    }
    
    response = supabase.table("user_config").insert(data).execute()
    return response

def get_user_config(user_id):
    """
    Récupère la configuration utilisateur depuis Supabase
    
    Args:
        user_id (str): ID de l'utilisateur
    
    Returns:
        dict: Configuration utilisateur
    """
    response = supabase.table("user_config").select("*").eq("user_id", user_id).execute()
    return response.data[0] if response.data else None

def update_user_config(user_id, config_data):
    """
    Met à jour la configuration utilisateur dans Supabase
    
    Args:
        user_id (str): ID de l'utilisateur
        config_data (dict): Nouvelles données de configuration
    
    Returns:
        dict: Réponse de Supabase
    """
    response = supabase.table("user_config").update(config_data).eq("user_id", user_id).execute()
    return response 