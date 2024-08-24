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

create table hovli(
     id text primary key default generate_id(),
);

------------------------------
