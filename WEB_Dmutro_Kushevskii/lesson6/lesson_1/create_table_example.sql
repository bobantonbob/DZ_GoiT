create table clients(
  id serial primary key,
  name varchar(30),
  surname varchar(30),
  age int check (age >= 0),
  constraint persons_surname_un unique (surname)
);