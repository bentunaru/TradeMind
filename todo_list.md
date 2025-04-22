# TODO List for Trading Journal Project

0. **Initialize Project Structure**
   - Create a Git repository and base directory layout (e.g., `streamlit_app.py`, `pages/`, `utils/`, `data/`, `assets/`).
   - Set up a Python virtual environment and `requirements.txt`:
   - Pin dependencies to the latest available versions: `streamlit`, `supabase`, `openai`, `numpy`, `pandas`, `matplotlib`, `seaborn`
   - Configure basic project settings (e.g., `.gitignore`, project readme).

1. **Onboarding Module**
   - Implement Streamlit page for initial configuration (ICT Level, Starting Capital, Risk %, Indicators, Timeframes, Checklists).
   - Test form fields, validate inputs, persist settings in Supabase.
   - Ask for user confirmation of successful setup.

2. **Quick Journal Module**
   - Build Streamlit page to record a trade (Symbol, Direction, ICT Setup, Note).
   - Display appropriate checklist (Continuation/Reversal) and enforce all items checked.
   - Save trade details and checklist status to Supabase.
   - Test saving and retrieval of a sample trade; ask for feedback.

3. **Import & Analysis Module**
   - Add CSV upload and screenshot uploader components.
   - Run multi-timeframe analysis using Python logic; show results in UI.
   - Store uploads in Supabase Storage.
   - Verify analysis outputs; request validation from user.

4. **Dashboard Module**
   - Create KPIs summary, heatmap, and equity curve using Matplotlib in Streamlit.
   - Fetch data from Supabase and render charts.
   - Test rendering with sample data; ask for design/UX feedback.

5. **Trade Details Module**
   - Develop detail view: trade info, checklist, AI feedback, notes.
   - Implement PDF export functionality.
   - Validate PDF output; prompt user for comments.

6. **AI Coaching & Reviews Module**
   - Integrate OpenAI API to generate pre- and post-session feedback.
   - Build Reports page with weekly/monthly filters and export options.
   - Test API calls and report exports; ask for accuracy and completeness.

7. **Testing, Packaging & Deployment**
   - Ensure offline and online data persistence (Supabase + local cache).
   - Package app for local use (requirements.txt, run scripts).
   - Perform end-to-end testing; collect user feedback before final release.

---

**Development Flow**
- Use this TODO List to guide each implementation step.
- After completing each step, run tests and confirm functionality.
- Before moving to the next step, ask the user for confirmation and any questions about progress.
