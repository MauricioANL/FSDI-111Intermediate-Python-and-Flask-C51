CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45),
    last_name VARCHAR(45),
    hobbies TEXT,
    is_online BOOLEAN DEFAULT 1
);

INSERT UNTO user (
    first_name ,
    last_name ,
    hobbies 
)VALUES(
    "Mauricio",
    "Navarro",
    "Run"
);

INSERT UNTO user (
    first_name ,
    last_name ,
    hobbies 
)VALUES(
    "Antonio",
    "Lopez",
    "Play Scoocer"
);

UPDATE user SET
    first_name = 'Antonio',
    hobbies = "diy srtuff and watching TV"
WHERE id=2;

DELETE FROM user WHERE id=1;