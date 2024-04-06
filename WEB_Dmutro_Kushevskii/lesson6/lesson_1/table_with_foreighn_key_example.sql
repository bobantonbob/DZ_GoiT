create table client_photo(
  id serial primary key,
  url varchar(255),
  client_id_fk int references clients(id) on delete cascade
);
