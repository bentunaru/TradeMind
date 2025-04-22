import os
from dotenv import load_dotenv
from supabase import create_client
from openai import OpenAI

def test_supabase_connection():
    """Teste la connexion à Supabase"""
    try:
        # Charger les variables d'environnement
        load_dotenv()
        
        # Récupérer les clés
        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_KEY")
        
        print("\nVérification des variables d'environnement :")
        print(f"SUPABASE_URL: {supabase_url}")
        print(f"SUPABASE_KEY: {supabase_key[:10]}...")  # Afficher seulement le début de la clé
        
        if not supabase_url or not supabase_key:
            return False, "Les variables d'environnement Supabase ne sont pas configurées"
        
        # Tester la connexion
        print("\nTentative de connexion à Supabase...")
        supabase = create_client(supabase_url, supabase_key)
        
        # Tester une requête simple
        print("\nTest de requête sur la table user_config...")
        response = supabase.from_("user_config").select("*").limit(1).execute()
        print(f"Réponse de Supabase : {response}")
        
        return True, "Connexion à Supabase réussie"
        
    except Exception as e:
        print(f"\nErreur détaillée : {str(e)}")
        return False, f"Erreur de connexion à Supabase : {str(e)}"

def test_openai_connection():
    """Teste la connexion à OpenAI"""
    try:
        # Charger les variables d'environnement
        load_dotenv()
        
        # Récupérer la clé
        openai_key = os.getenv("OPENAI_API_KEY")
        
        if not openai_key:
            return False, "La variable d'environnement OpenAI n'est pas configurée"
        
        # Tester la connexion
        client = OpenAI(api_key=openai_key)
        
        # Tester une requête simple
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Test de connexion"}],
            max_tokens=5
        )
        
        return True, "Connexion à OpenAI réussie"
        
    except Exception as e:
        return False, f"Erreur de connexion à OpenAI : {str(e)}"

if __name__ == "__main__":
    print("Test des connexions...")
    
    # Test Supabase
    supabase_success, supabase_message = test_supabase_connection()
    print(f"\nSupabase: {supabase_message}")
    
    # Test OpenAI
    openai_success, openai_message = test_openai_connection()
    print(f"OpenAI: {openai_message}")
    
    # Résumé
    if supabase_success and openai_success:
        print("\n✅ Toutes les connexions sont fonctionnelles")
    else:
        print("\n❌ Certaines connexions ont échoué") 