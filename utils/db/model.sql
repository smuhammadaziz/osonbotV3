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

create table users(
     id text primary key default generate_id(),
     name text not null,
     username text not null,
     chat_id varchar(255) not null,
     phone varchar(100) not null
);

CREATE TABLE yer (
    id TEXT PRIMARY KEY DEFAULT generate_id(),
    user_id VARCHAR(255) NOT NULL, -- Match the data type of chat_id in users table
    photos TEXT NOT NULL,
    captions TEXT NOT NULL,
    message_id TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(chat_id) -- Reference chat_id in users table
);

------------------------------
