CREATE DATABASE CREDITO;
CREATE TABLE ESTATUS(
	IDU serial primary key, 
	PRIMER_NOMBRE varchar(20) not null,
	APELLIDO_PAT varchar(20) not null, 
	APELLIDO_MAT varchar(20) not null, 
	FECHA_NAC date not null default '1900-01-01',
	RFC varchar(13) not null, 
	INGRESOS_MENSUALES float not null,
	DEPENDIENTES int not null,
	APROBADO varchar(10)
)