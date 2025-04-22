# TradeMind - AI Trading Journal

A Streamlit application for trade tracking and analysis, with integrated AI coaching.

## Features

- Structured trading journal
- Multi-timeframe analysis
- AI feedback based on ICT setups
- Performance dashboard
- Report exports

## Installation

1. Clone the repository
```bash
git clone https://github.com/your-username/trademind.git
cd trademind
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment variables
```bash
cp .env.example .env
# Edit .env with your API keys
```

5. Launch the application
```bash
streamlit run streamlit_app.py
```

## Project Structure

```
trademind/
├── pages/           # Streamlit pages
├── utils/           # Utility functions
├── data/           # Local data
├── assets/         # Images, styles
├── streamlit_app.py # Main application
└── requirements.txt # Dependencies
```

## Configuration

The application requires the following API keys:
- Supabase (URL and key)
- OpenAI (API key)

## License

MIT 