DROP DATABASE IF EXISTS church; --  I added this just so i didnt create two identical databases --
CREATE DATABASE church; -- creates church database --
-- we will now create our first tuples starting with our entity types--
USE church; -- this signifies that we are using the database


CREATE TABLE Tithe(
Tithe_amount smallint(8)   ,
Membership_names varchar(50) 

);

INSERT INTO Tithe(Tithe_amount)
VALUES (78),(517),(432),(834),(266),
(975),(659),(563),(564),(865),(574),(0),
(877),(0),(0),(394),(686),(776),(637),(776),
(637),(270);



INSERT INTO Tithe(Membership_names)
VALUES ("Steven E. Clark"),
("Penny W. Hughes"),
("Amy D. Swanson"),
("Bethany J. Strickland"),
("Evan J. West"),
("Lydia R. Velazquez"),
("Yvonne J. Davis"),
("Irene G. Sanchez"),
(" C. Sanchez"),
("Joseph M. Han"),
("Daniel S. Holman"),
("Bonnie M. Holman"),
("Emily J. Holman"),
("Cora D. Holman"),
("Jack T. Holman"),
("Stephanie J. Culberson"),
("Gilberto J. Sweeney"),
("David Y. Escobar"),
("Maria K. Escobar"),
("Cathy J. Bowen");


-- we will also leave the empty blocks as zero because there is nothing recorded for them--

CREATE TABLE church_speakers(
speaker_name varchar(50) NOT NULL,
total_attendence int NOT NULL,
attendence_average float NOT NULL

);
INSERT INTO church_speakers(speaker_name,total_attendence,attendence_average)
VALUES ("Steven.E.Clark",395,32.91),("Heather.J.Rodriguez",68,34.00),("Penny.W.Hughes",168,33.60),("Bob.O.Resler",25,100.00);




CREATE TABLE roles_in_church(
pastor_name varchar(50) ,
voulenteer_name varchar(50) 

);
INSERT INTO roles_in_church(pastor_name)
VALUES ("Steven.E.Clark"),("Heather.J.Rodriguez"),("Penny.W.Hughes"),("Bob.O.Resler");

INSERT INTO roles_in_church(voulenteer_name)
VALUES("Joseph M. Han"),("Daniel S. Holman"),("Gilberto J. Sweeney"),("Evan J. West"),("Yvonne J. Davis"),("Richard C. Sanchez");

CREATE TABLE membership_groups(
membership_groups_names varchar(30)

);
INSERT INTO membership_groups(membership_groups_names)
VALUES ("Church Board"),("Celebrate Recovery"),("Student Group"),("Rising Son Class");

CREATE TABLE members_church(
Membership_names varchar(50)  NULL,
Age tinyint NOT NULL,
Adress varchar(50) NOT NULL,
Phone_Numbers varchar(50) NOT NULL,  
membership_attendence_average float PRIMARY KEY 


); 

INSERT INTO members_church(Membership_names,Age,Adress,Phone_Numbers,membership_attendence_average)
VALUES ("Steven E. Clark",	55,	"1150 Cantebury Drive",	"555-701-7006", 47.01),
("Penny W. Hughes",	74,	"4392 Cooks Mine Road",	"555-770-9482", 47.10),
("Amy D. Swanson",	57,	"3756 Railroad Street",	"555-742-5192", 9.11),
("Bethany J. Strickland",	52,	"1005 Hillcrest Circle", "555-568-7767",38.10),
("Evan J. West",	26,	"1106 Frank Avenue", "555-977-5258", 33.01),
("Lydia R. Velazquez",	46,	"4196 Wexford Way",	"555-332-1075", 23.01),
("Yvonne J. Davis",	28,	"1321 Whaley Lane",	"555-477-4036", 23.10),
("Irene G. Sanchez",00	,"582 Kennedy Court","555-275-8913", 19.01),
(" C. Sanchez",	61,	"582 Kennedy Court","555-275-8913", 19.1),
("Joseph M. Han",	33,	"2204 Calvin Drive","555-914-1703", 9.10),
("Daniel S. Holman",	44,	"1415 Owagner Lane","555-237-1129",38.11),
("Bonnie M. Holman",	45,	"1415 Owagner Lane","555-280-9489" ,33.33),
("Emily J. Holman",	20,	"1415 Owagner Lane","555-794-9326", 23.11),
("Cora D. Holman",	14,	"1415 Owagner Lane", "000000000",14.10),
("Jack T. Holman",	11,	"1415 Owagner Lane", "000000000",9.01),
("Stephanie J. Culberson",	37,	"4913 Scheuvront Drive", "555-474-4307", 28.01),
("Gilberto J. Sweeney",	48,	"604 Court Street",	"555-736-9830", 42.01),
("David Y. Escobar",	84,	"1126 Pine Tree Lane",	"555-403-7514" ,4.01),
("Maria K. Escobar",	82,	"1126 Pine Tree Lane",	"555-403-7514", 14.11),
("Cathy J. Bowen",	71,	"876 Selah Way","555-681-4279", 33.10);





ALTER TABLE members_church
ALTER COLUMN Phone_Numbers SET DEFAULT "000000000";

ALTER TABLE members_church
ALTER COLUMN Age SET DEFAULT 0;




-- Question 2 --

SELECT * FROM Tithe as t 
inner join
members_church as mc ON t.Membership_names = mc.Membership_names;

-- I keep getting null values even though I have already inserted values, even after explcictly making it a non-null value it and giving it a default value it only returns
-- the default value , even after changing around the order--


-- Question 3--

SELECT * FROM church_speakers;
-- On average Bob.O.Resler has the highest , however this is because he has only preached twice














