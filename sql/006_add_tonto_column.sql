ALTER TABLE cowboys ADD COLUMN tonto int;

UPDATE cowboys SET tonto = 0 where id = 4;
UPDATE cowboys SET tonto = 0 where id = 3;
UPDATE cowboys SET tonto = 0 where id = 5;
UPDATE cowboys SET tonto = 0 where id = 6;
UPDATE cowboys SET tonto = 0 where id = 2;
UPDATE cowboys SET tonto = 0 where id = 1;

ALTER TABLE cowboys ALTER COLUMN tonto SET NOT NULL;
