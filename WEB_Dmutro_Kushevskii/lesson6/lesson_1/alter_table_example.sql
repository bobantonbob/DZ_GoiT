alter table clients
add column visa bool;
alter table clients
drop column age;

alter table client change age str_age varchar(255);
