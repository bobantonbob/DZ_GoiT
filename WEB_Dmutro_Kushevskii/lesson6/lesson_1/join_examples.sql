select c.id, c.name, c.surname, p.url as photo_url
from clients as c
inner join client_photo as p on p.client_id_fk = c.id;

select c.id, c.name, c.surname, p.url as photo_url
from clients as c
full join client_photo as p on p.client_id_fk = c.id;

select c.id, c.name, c.surname, p.url as photo_url
from clients as c
right join client_photo as p on p.client_id_fk = c.id;
