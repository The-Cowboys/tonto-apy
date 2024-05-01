CREATE TABLE tontos (
    id SERIAL PRIMARY KEY,
    cowboy_id int not null references cowboys(id),
    dia varchar(10) not null UNIQUE,
    created timestamptz not null
);
grant all on cowboys to app;

CREATE INDEX index_cowboy_dia
ON tontos(dia);


