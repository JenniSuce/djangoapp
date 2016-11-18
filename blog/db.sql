CREATE TABLE `blog_postear` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`titulo`	varchar(200) NOT NULL,
	`ISBN`	text NOT NULL,
	`Portada`	text NOT NULL,
	`Editorial`	text NOT NULL,
	`pais`	text NOT NULL,
	`years`	text NOT NULL,
	`creacion_date`	datetime NOT NULL,
	`publicacion_date`	datetime,
	`autor_id`	integer NOT NULL,
	FOREIGN KEY(`autor_id`) REFERENCES "auth_user" ( "id" )
);