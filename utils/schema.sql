-- Table pour stocker la configuration utilisateur
CREATE TABLE IF NOT EXISTS user_config (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    user_id UUID NOT NULL UNIQUE,
    ict_level TEXT NOT NULL,
    starting_capital DECIMAL(10,2) NOT NULL,
    risk_per_trade DECIMAL(5,2) NOT NULL,
    indicators TEXT[] NOT NULL,
    timeframes TEXT[] NOT NULL,
    continuation_checklist TEXT[] NOT NULL,
    reversal_checklist TEXT[] NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Index pour optimiser les requêtes
CREATE INDEX IF NOT EXISTS idx_user_config_user_id ON user_config(user_id);

-- Trigger pour mettre à jour le timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_user_config_updated_at
    BEFORE UPDATE ON user_config
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column(); 