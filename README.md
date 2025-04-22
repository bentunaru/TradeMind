# TradeMind - Journal de Trading IA

Une application Streamlit pour le suivi et l'analyse des trades, avec coaching IA intégré.

## Fonctionnalités

- Journal de trading structuré
- Analyse multi-timeframe
- Feedback IA basé sur les setups ICT
- Dashboard de performance
- Export de rapports

## Installation

1. Cloner le repository
```bash
git clone https://github.com/votre-username/trademind.git
cd trademind
```

2. Créer et activer l'environnement virtuel
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. Installer les dépendances
```bash
pip install -r requirements.txt
```

4. Configurer les variables d'environnement
```bash
cp .env.example .env
# Éditer .env avec vos clés API
```

5. Lancer l'application
```bash
streamlit run streamlit_app.py
```

## Structure du Projet

```
trademind/
├── pages/           # Pages Streamlit
├── utils/           # Fonctions utilitaires
├── data/            # Données locales
├── assets/          # Images, styles
├── streamlit_app.py # Application principale
└── requirements.txt # Dépendances
```

## Configuration

L'application nécessite les clés API suivantes :
- Supabase (URL et clé)
- OpenAI (clé API)

## Licence

MIT 