select * from clients;
select * from clients where age > 23;
select * from clients where age in (23, 32);
select * from clients where age between 24 and 31;
select * from clients where age not between 24 and 31;

select name, age from clients order by age desc;

select url from client_photo where client_id_fk in (select id from clients where surname = 'Kushchevskyi');
