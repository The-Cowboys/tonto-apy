SET TIME ZONE 'UTC';
CREATE TABLE titulos (
    id SERIAL PRIMARY KEY,
    name varchar (30) not null unique,
    cowboy_id int not null references cowboys(id),
    created timestamptz not null,
    updated timestamptz
);
grant all on cowboys to app;

insert into titulos (name, created, cowboy_id) values ('El mas grande', now(), 1);



