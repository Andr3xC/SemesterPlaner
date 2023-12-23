#create database Carreras;
use Carreras;
show databases;
CREATE TABLE Sistemas(
	_id int auto_increment,
    _Name varchar(255),
    _value int,
    _status boolean,
    PRIMARY KEY(_id)
);

insert into Sistemas(_name,_value,_status) values ("AYED",4,False);

SHOW create table Sistemas;
select * from Sistemas;