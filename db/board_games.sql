DROP TABLE IF EXISTS board_games;
DROP TABLE IF EXISTS manufacturers;


CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    contact_details VARCHAR(255)
);

CREATE TABLE board_games (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    quantity INT,
    buying_cost INT,
    selling_price INT,
    manufacturer_id INT REFERENCES manufacturers(id)
);