ALTER TABLE cowboys ADD COLUMN email varchar UNIQUE;

UPDATE cowboys SET email = 'gkroger11@gmail.com' where id = 4;
UPDATE cowboys SET email = 'el_mallic@hotmail.com' where id = 3;
UPDATE cowboys SET email = 'dgraficohunter235@gmail.com' where id = 5;
UPDATE cowboys SET email = 'cristianescobar47468@gmail.com' where id = 6;
UPDATE cowboys SET email = 'franconecat@gmail.com' where id = 2;
UPDATE cowboys SET email = 'yoomat.75@hotmail.com' where id = 1;

-- make email not null
ALTER TABLE cowboys ALTER COLUMN email SET NOT NULL;
