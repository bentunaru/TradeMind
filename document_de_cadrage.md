## Document de cadrage – Étape 1 à 4 : Journal de Trading IA

### 1. Mission et vision
- **Rigueur dans les trades** : tenir un journal structuré pour imposer une discipline et systématiser le processus de prise de décision.
- **Suivi des performances** : mesurer le ratio gains/pertes, le drawdown et l'évolution de la performance dans le temps.
- **Amélioration continue** : identifier les points faibles et axes d'amélioration à chaque évaluation.
- **Horizon** : objectifs à moyen et long terme pour stabiliser et optimiser le trading.

### 2. Objectifs et KPIs
- **Objectifs clés** :
  - Améliorer le ratio gains/pertes.
  - Réduire le drawdown maximal.
  - Assurer le respect strict des setups et des règles de money management.
- **KPIs et granularité** :
  - **Ratio gains/pertes** (suivi quotidien, hebdomadaire, mensuel, trimestriel).
  - **Taux de trades gagnants**.
  - **Drawdown maximal**.
  - **Taux de conformité aux checklists de setups ICT (Continuation et Reversal)**.
- **Périodes de suivi** : quotidien, hebdomadaire, mensuel, trimestriel.

### 3. Architecture technique (haut niveau)
1. **Front‑end**  
   - Application web locale (Streamlit) fonctionnant entièrement en local.  
   - Widgets pour : formulaire de journal, import captures, affichage graphiques.  
2. **Back‑end & Stockage**  
   - Supabase pour la persistance (Auth, Realtime, Storage).  
   - Client `supabase` en Python pour trade, CSV, screenshots, Functions.  
3. **Séparation des responsabilités & modularité**  
   - Front‑end gère l’UI, back‑end la logique et les données.  
   - Architecture modulaire pour tests et maintenance.  
4. **Moteur IA / Coaching**  
   - Appels à l’API OpenAI (package `openai` v1.75.0) pour feedback.  
   - Pipeline d’ingestion, détection ICT, génération de feedback.  
5. **Sécurité & conformité**  
   - Auth Supabase, cryptage, sauvegarde et réplication UE (GDPR).

**Prochaines étapes** :
- Revue et validation de l’architecture.
- Lancement de l’étape 4 : UX/UI et parcours utilisateur.
