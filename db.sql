CREATE TABLE padre (
    padre_id integer PRIMARY KEY,
    nom text 
);

CREATE TABLE hijo (

    hijo_id   INTEGER PRIMARY KEY,
    nom TEXT    , 
    padre_id  INTEGER,
    FOREIGN KEY (padre_id)
       REFERENCES padre (padre_id) 

); 

INSERT INTO padre (nom, padre_id)
VALUES('peter papa.', 4); 

INSERT INTO hijo (nom, padre_id)
VALUES('peter.', 4);