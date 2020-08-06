create table if not exists example(
	ex1 varchar(25) not null,
    ex2 varchar(25) not null,
    ex3 int not null auto_increment,
    primary key (ex3)
);

insert into general.example(ex1, ex2) 
values('example_first', 'example_last');
    
select * from general.example where ex3=1;
