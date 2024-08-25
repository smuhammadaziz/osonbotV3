-- id generator
CREATE OR REPLACE FUNCTION generate_id() RETURNS TEXT AS $$
DECLARE
    chars TEXT := 'abcdefghijklmnopqrstuvwxyz0123456789';
    result TEXT := '';
    i INT := 0;
BEGIN
    FOR i IN 1..4 LOOP
        result := result || substr(chars, (floor(random() * length(chars) + 1))::INT, 1);
    END LOOP;
    RETURN result;
END;
$$ LANGUAGE plpgsql;

-- Table

CREATE TABLE users (
    id TEXT PRIMARY KEY DEFAULT generate_id(),
    name TEXT NOT NULL,
    username TEXT NOT NULL,
    chat_id VARCHAR(255) NOT NULL UNIQUE, -- Add UNIQUE constraint
    phone VARCHAR(100) NOT NULL
);

CREATE TABLE yer (
    id TEXT PRIMARY KEY DEFAULT generate_id(),
    user_id VARCHAR(255) NOT NULL,
    photos TEXT NOT NULL,
    captions TEXT NOT NULL,
    message_id TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(chat_id)
);

------------------------------
