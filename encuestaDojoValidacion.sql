

USE encuesta_dojo;

SELECT *
FROM dojos;

DELETE FROM dojos WHERE id>0;

INSERT INTO dojos(name, location, languaje, comment, created_at, update_at)
VALUES('Andres', 'Arequipa', 'Python', 'megusta', NOW(), NOW());