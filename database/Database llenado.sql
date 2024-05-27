-- Insertar datos en la tabla city
DELETE FROM city;
ALTER SEQUENCE city_id_seq RESTART WITH 1;
INSERT INTO city (city_name, created_date, deleted_date)
VALUES
    ('Bogotá', '2024-04-24 00:00:00-05'::timestamp with time zone, NULL),
    ('Medellin', '2024-04-24 00:00:00-05'::timestamp with time zone, NULL),
    ('Cartagena', '2024-04-24 00:00:00-05'::timestamp with time zone, NULL),
    ('Cali', '2024-04-24 00:00:00-05'::timestamp with time zone, NULL),
    ('Santa Marta', '2024-04-24 00:00:00-05'::timestamp with time zone, NULL),
    ('Barranquilla', '2024-04-24 00:00:00-05'::timestamp with time zone, NULL),
    ('Bucaramanga', '2024-04-24 00:00:00-05'::timestamp with time zone, NULL);

-- Insertar datos en la tabla "parking_type"
DELETE FROM parking_type;
ALTER SEQUENCE parking_type_id_seq RESTART WITH 1;
INSERT INTO parking_type (description, created_date, deleted_date)
VALUES
    ('Cubierto', CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Semi-cubierto', CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('descubierto', CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL);

-- Insertar datos en la tabla "loyalty"
DELETE FROM loyalty;
ALTER SEQUENCE loyalty_id_seq RESTART WITH 1;
INSERT INTO loyalty (amount_points, amount_per_point, created_date, deleted_date)
VALUES
    (10000, 10, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    (20000, 20, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    (30000, 30, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL);

-- Insertar datos en la tabla "vehicle_type"
DELETE FROM vehicle_type;
ALTER SEQUENCE vehicle_type_id_seq RESTART WITH 1;
INSERT INTO vehicle_type (description, created_date, deleted_date)
VALUES
    ('carro', CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('moto', CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Bicicleta', CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL);

-- Insertar datos en la tabla "vehicle"
DELETE FROM vehicle;
ALTER SEQUENCE vehicle_id_seq RESTART WITH 1;
INSERT INTO vehicle (plate, vehicle_type_id, created_date, deleted_date)
VALUES
    ('npr 473', 2, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('rwc 659', 1, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('dkv 060', 1, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('xha 474', 1, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('osk 123', 2, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('jjq 415', 2, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('xmb 763', 1, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('krd 629', 2, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('ijf 764', 1, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('zyo 388', 2, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('ayj 458', 1, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('hkz 291', 2, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('hfi 371', 1, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('rof 111', 1, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('umf 423', 2, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('qvw 732', 1, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('uad 762', 1, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('sbs 406', 2, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('wgz 668', 1, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('rgo 641', 2, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('bici', 2, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL);

-- Insertar datos en la tabla "fee_type"
DELETE FROM fee_type;
ALTER SEQUENCE fee_type_id_seq RESTART WITH 1;
INSERT INTO fee_type (description, created_date, deleted_date)
VALUES
    ('hora', CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('minuto', CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('día', CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('reserva', CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL);

-- Insertar datos en la tabla "fee"
DELETE FROM fee;
ALTER SEQUENCE fee_id_seq RESTART WITH 1;
INSERT INTO fee (amount, fee_type_id, vehicle_type_id, created_date, deleted_date)
VALUES
    (3000, 1, 1, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    (100, 2, 1, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    (15000, 3, 1, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    (2000, 4, 1, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    (1500, 1, 2, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    (30, 2, 2, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    (7000, 3, 2, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    (2000, 4, 2, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    (1000, 1, 3, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    (20, 2, 3, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    (4000, 3, 3, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    (2000, 4, 3, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL);

-- Insertar datos en la tabla "schedule"
DELETE FROM schedule;
ALTER SEQUENCE schedule_id_seq RESTART WITH 1;
INSERT INTO schedule (week_day, opening_time, closing_time, created_date, deleted_date)
VALUES
    (NULL, '2024-04-01 00:00:00-05', '2024-04-01 20:00:00-05', CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    (NULL, '2024-04-02 00:00:00-05', '2024-04-02 00:00:00-05', CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    (NULL, '2024-04-03 03:00:00-05', '2024-04-03 22:00:00-05', CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    (NULL, '2024-04-04 02:00:00-05', '2024-04-04 20:00:00-05', CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    (NULL, '2024-04-05 01:00:00-05', '2024-04-05 21:00:00-05', CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL);

-- Insertar datos en la tabla "user"
DELETE FROM "user";
ALTER SEQUENCE user_id_seq RESTART WITH 1;
INSERT INTO "user" (user_name, last_name, email_address, user_password, ip_address, document_type, user_document, user_token, created_date, deleted_date)
VALUES
    ('Jacquelin', 'Josskowitz', 'jjosskowitz0@scientificamerican.com', 'bT7&vEToA9>cz#(', '9.21.93.208', 'CC', '6597746390', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Patsy', 'Geoghegan', 'pgeoghegan1@kickstarter.com', 'sN1/5>hT~w', '1652851209', 'CC', '1652851209', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Geordie', 'Cristoforetti', 'gcristoforetti2@goo.gl', 'lH4!SO#,TxZ', '3326670716', 'CC', '3326670716', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Lucias', 'Wyard', 'lwyard3@nationalgeographic.com', 'vB9"7=fj<', '35.199.23.65', 'CC', '309164781', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Ram', 'Kunath', 'rkunath4@mayoclinic.com', 'jW8{Rk?i', NULL, 'CC', '3751544354', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Moria', 'Beville', 'mbeville5@examiner.com', 'qH0<k?{A25fd&H+c', NULL, 'CC', '2196420586', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Darill', 'Izacenko', 'dizacenko6@abc.net.au', 'qD7>D|<D', '197.205.82.117', 'CC', '9427712496', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Ferdinanda', 'Jozefiak', 'fjozefiak7@merriam-webster.com', 'sR8~zeWg7\\6', NULL, 'CC', '5629739175', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Fern', 'Kinghorn', 'fkinghorn8@pagesperso-orange.fr', 'xV1/T+.(gs{Hn!J', NULL, 'CC', '2151572104', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Carver', 'Gregory', 'cgregory9@yahoo.com', 'nS6\\5xge', NULL, 'CC', '3092559437', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Jodi', 'Gerrill', 'jgerrilla@google.com.hk', 'rS7#TaHDfIz', NULL, 'CC', '6676429157', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Ophelie', 'LaBastida', 'olabastidab@gnu.org', 'xH0?4{+r', '248.214.109.37', 'CC', '112363649', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Grange', 'Penlington', 'gpenlingtonc@examiner.com', 'uR2|CDoD', NULL, 'CC', '2857257987', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Philippe', 'Domanski', 'pdomanskid@over-blog.com', 'sX8\cN\', '170.53.194.126', 'CC', '125584564', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Verna', 'Tire', 'vtiree@nationalgeographic.com', 'jC6)_d&%', '54.147.114.186', 'CC', '8957313087', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Reggie', 'MacMenamin', 'rmacmenaminf@wikispaces.com', 'iU1_8.1YF`5LwB', '202.22.116.179', 'CC', '6276286098', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Marysa', 'Colbridge', 'mcolbridgeg@aol.com', 'wZ5/*I\e', NULL, 'CC', '2841426323', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Jobi', 'Baverstock', 'jbaverstockh@over-blog.com', 'yF7$nO${', NULL, 'CC', '594123772', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Marie', 'Mompesson', 'mmompessoni@ow.ly', 'fK1+_1>wQgXZnEIj', '33.96.33.218', 'CC', '4569417562', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Haze', 'Surcombe', 'hsurcombej@mashable.com', 'wJ2$x}993(T', '217.127.205.61', 'CC', '1151687363', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Coriss', 'Skully', 'cskullyk@free.fr', 'tB9\~MuX`J/0P3', NULL, 'CC', '8644867384', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Britte', 'Cazalet', 'bcazaletl@ted.com', 'wP3=4V2wlMbuM0', '217.120.175.201', 'CC', '7502420918', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Dorie', 'Islep', 'dislepm@dell.com', 'rX7#adJUfj$f', '180.32.25.218', 'CC', '6056759016', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Lincoln', 'Ivashov', 'livashovn@phpbb.com', 'yM9_Qat1}qKmI|', '236.103.156.19', 'CC', '3940308886', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Clarabelle', 'Mityashin', 'cmityashino@chronoengine.com', 'rF3})Rym/f0', NULL, 'CC', '999819474', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Wolfgang', 'Roust', 'wroustp@gizmodo.com', 'pC4*afo@Ri', '204.121.103.237', 'CC', '8740085491', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Rowen', 'Zorzenoni', 'rzorzenoniq@yale.edu', 'cM3%xhCr', NULL, 'CC', '153010979', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Ramonda', 'Seatter', 'rseatterr@jugem.jp', 'uC1//Q\c8_w%|{)H', NULL, 'CC', '2637228608', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Stavros', 'Priver', 'sprivers@ustream.tv', 'vK4|A2RQK', NULL, 'CC', '4240211518', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Angelita', 'Wille', 'awillet@typepad.com', 'iV0"9N)/', NULL, 'CC', '4521261753', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Vidovik', 'Duddridge', 'vduddridgeu@over-blog.com', 'wA3`}\blsX\N\\', NULL, 'CC', '2278863041', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Matilde', 'Chimenti', 'mchimentiv@artisteer.com', 'tB9?T|gppO', NULL, 'CC', '7354707864', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Selig', 'Stayt', 'sstaytw@homestead.com', 'fN2,=v8=i{)V+=E', NULL, 'CC', '8486393331', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Etan', 'Farquarson', 'efarquarsonx@pagesperso-orange.fr', 'vI9{1aezyG8+hS', NULL, 'CC', '7334563293', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Chauncey', 'Matthieson', 'cmatthiesony@typepad.com', 'hO1._1F`FDQ', '184.99.218.126', 'CC', '3874766612', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Calv', 'Regler', 'creglerz@redcross.org', 'fI4~8YZ\\DA', '255.141.32.104', 'CC', '3137147434', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Darcy', 'Cottage', 'dcottage10@squarespace.com', 'gA8=Ikj_`eb4', NULL, 'CC', '5831229524', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Koralle', 'Sonnenschein', 'ksonnenschein11@umich.edu', 'nR1|g{5rz.4!,', '96.37.60.143', 'CC', '6113206647', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Alfredo', 'Shucksmith', 'ashucksmith12@ezinearticles.com', 'pS9+)@\epzsy', '32.230.96.153', 'CC', '9132548924', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Shae', 'Garriock', 'sgarriock13@tiny.cc', 'iN2"!ACZ20m\\', '83.212.80.207', 'CC', '1892099175', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Jonathan', 'Tucsell', 'jtucsell14@1688.com', 'sU2\t!3H\W~72sx', NULL, 'CC', '1094626742', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Tyson', 'Orviss', 'torviss15@ucoz.ru', 'rA9#{V&Xs{', NULL, 'CC', '3102577808', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Dianna', 'Lount', 'dlount16@free.fr', 'gF8\_Um_QhsoF\\66', '26.247.210.180', 'CC', '6373949809', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Noella', 'Kitcher', 'nkitcher17@nhs.uk', 'yO5?.kt8(D||D`', '19.28.35.189', 'CC', '7173016872', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Bobbie', 'McIlhone', 'bmcilhone18@google.co.jp', 'nZ2}7MzC=_O', NULL, 'CC', '5705492250', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Cinnamon', 'Randle', 'crandle19@ning.com', 'nS7\uXo,m`Mk(W', '93.224.2.247', 'CC', '6689131759', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Basilius', 'Braney', 'bbraney1a@google.it', 'wF7`\\c5|!WLG5"0', '199.242.114.50', 'CC', '418147964', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Kendall', 'De Benedetti', 'kde1b@patch.com', 'iM7>9e)=1($K{YAr', '213.125.171.171', 'CC', '8480724992', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Igor', 'Presslie', 'ipresslie1c@creativecommons.org', 'eB0+lm9J5+m}Z(<', '227.103.196.95', 'CC', '7553729257', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Angeli', 'Piner', 'apiner1d@amazon.com', 'mY5~7l/Fx4', '224.178.101.10', 'CC', '7918167824', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Lezlie', 'Keemer', 'lkeemer1e@jigsy.com', 'sC5+0RYZmc', '217.37.197.31', 'CC', '911445942', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Claudine', 'Morling', 'cmorling1f@examiner.com', 'wJ9"C0!k6`07oMK', '195.46.4.21', 'CC', '3083701909', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Sissie', 'Yard', 'syard1g@tinypic.com', 'rB3$\tzA5rm=5g/', '203.240.142.162', 'CC', '5999220104', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Ashly', 'Cherrington', 'acherrington1h@hhs.gov', 'pA4_f$dCB|\\CY', NULL, 'CC', '9663793192', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Aharon', 'Capstake', 'acapstake1i@123-reg.co.uk', 'hL5)ZLb+wS=F~@K', '115.148.118.88', 'CC', '6315058654', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Theadora', 'Wadworth', 'twadworth1j@4shared.com', 'hG6(4Q<\u\cAac', '19.61.63.56', 'CC', '3607615004', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Jess', 'Enoksson', 'jenoksson1k@tinypic.com', 'pG5_U1<p#"g|x{EY', '158.160.51.202', 'CC', '5109033130', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Faun', 'Torvey', 'ftorvey1l@homestead.com', 'zU5++RAxC>dhmn%,', '103.41.42.103', 'CC', '7620696663', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Tonnie', 'Henighan', 'thenighan1m@cocolog-nifty.com', 'jP1.)_n!?~d@', '241.218.106.45', 'CC', '3762738841', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Mariejeanne', 'Saterweyte', 'msaterweyte1n@oaic.gov.au', 'gS2}a*t@', '21.142.201.233', 'CC', '6179398319', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Weber', 'Hollingsbee', 'whollingsbee1o@washingtonpost.com', 'bA9$Rm_","?VrIY{', '251.237.238.62', 'CC', '9213168685', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Ludovico', 'Koene', 'lkoene1p@yahoo.co.jp', 'hS1\RqLR+npNiHpa', '130.9.128.4', 'CC', '2105572554', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Lesya', 'Carlsen', 'lcarlsen1q@ebay.co.uk', 'zI3/_aP=Mj)@qkd', '155.237.200.139', 'CC', '4321538712', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Kurtis', 'Stabler', 'kstabler1r@answers.com', 'sF8_y&waR|', '19.64.161.180', 'CC', '7616574787', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Catharine', 'Thornton', 'cthornton1s@ifeng.com', 'bF1.ZZ}wawTG9', '178.245.82.224', 'CC', '2213444588', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Stephine', 'Stegell', 'sstegell1t@samsung.com', 'cX3%\\yPjNR)', '241.38.35.197', 'CC', '1794365944', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Reine', 'Marian', 'rmarian1u@tiny.cc', 'iB2%YfQ,fYSEM/V', NULL, 'CC', '4615877275', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Erin', 'Mintoft', 'emintoft1v@statcounter.com', 'zN1*\mFI)szZ~jS', '203.78.155.86', 'CC', '2327618514', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Ky', 'Bonett', 'kbonett1w@stanford.edu', 'jB0\N?8EF?|15\2', '205.93.80.254', 'CC', '9790297932', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Margeaux', 'Grealey', 'mgrealey1x@hhs.gov', 'rO9&Ix=N|', '163.150.54.234', 'CC', '2357796135', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Lynda', 'Vedikhov', 'lvedikhov1y@shop-pro.jp', 'rX0#bDvWxUh', '60.175.127.105', 'CC', '376442496', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Patric', 'Fox', 'pfox1z@loc.gov', 'vC9$W%TgM)h$g\', '99.253.103.178', 'CC', '5015801165', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Bianca', 'Shallcrass', 'bshallcrass20@huffingtonpost.com', 'nD2&YW\<HeqY|sMJ', '38.197.153.224', 'CC', '1488232177', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Kelli', 'Jakubovski', 'kjakubovski21@behance.net', 'gZ2/R9|&|', '1.45.210.208', 'CC', '7146637684', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Faber', 'Lusgdin', 'flusgdin22@tiny.cc', 'eA8!3SHF0u5A', '179.229.76.254', 'CC', '1532133956', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Niels', 'Minget', 'nminget23@weibo.com', 'jQ2"|fQ$@OWQ9+a', '71.63.237.236', 'CC', '1647827614', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Ealasaid', 'Jedrych', 'ejedrych24@blogs.com', 'nF2+Mgck', '103.169.179.140', 'CC', '7771902198', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Philbert', 'Boller', 'pboller25@google.co.jp', 'bO1`rLrTh8gg', '193.216.211.251', 'CC', '9802155479', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Goldina', 'Lanceter', 'glanceter26@dailymotion.com', 'aJ3}%\\MXv7O>Vtk', '92.226.39.102', 'CC', '1739787738', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Rickie', 'Lorand', 'rlorand27@biblegateway.com', 'gT7*6Q2v0M', '123.25.54.185', 'CC', '9864896829', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Vanni', 'Rodenburg', 'vrodenburg28@alibaba.com', 'nJ8(}%a%', NULL, 'CC', '9149452319', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Lindsy', 'Bushen', 'lbushen29@is.gd', 'dR9>Z~6V0Zm@s', '10.103.201.194', 'CC', '4030028301', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Constantin', 'Dudding', 'cdudding2a@amazon.com', 'mW8/BF=5k', '73.255.67.60', 'CC', '5990122036', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Constance', 'Sogg', 'csogg2b@free.fr', 'qF0%0@KPY=/,~A', '108.39.85.71', 'CC', '3821674810', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Della', 'Gooddy', 'dgooddy2c@illinois.edu', 'bU2*%wU9eg', '221.143.122.185', 'CC', '4175089815', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Rollin', 'Grantham', 'rgrantham2d@ustream.tv', 'yN7\f%Yp7_xt', '205.191.169.243', 'CC', '5612966959', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Peggie', 'Asbery', 'pasbery2e@google.com.hk', 'xH3{\F>,A', '15.20.13.32', 'CC', '230395841', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Nicole', 'Cornillot', 'ncornillot2f@nbcnews.com', 'qR6{T%B{D<oBU/', '149.139.138.29', 'CC', '163057578', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Brit', 'Adamsky', 'badamsky2g@fc2.com', 'mT4}"7_)zq', '35.33.35.113', 'CC', '5752021047', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Korney', 'Ayerst', 'kayerst2h@csmonitor.com', 'fJ3!~2j2/O', '19.205.46.113', 'CC', '2918693054', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Marian', 'Dufer', 'mdufer2i@1und1.de', 'jP1=DZSR3TR*!', '101.24.250.186', 'CC', '2252782382', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Clayton', 'Georghiou', 'cgeorghiou2j@bloglovin.com', 'eN8@9clveOx', '1.248.166.253', 'CC', '173252675', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Manon', 'McClements', 'mmcclements2k@ibm.com', 'kE0(RC_Q', '50.135.35.104', 'CC', '2896537323', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Kaspar', 'Peer', 'kpeer2l@shinystat.com', 'xB8\\CHZ<"NYm', '242.46.52.15', 'CC', '3567135341', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Von', 'Osbourn', 'vosbourn2m@ocn.ne.jp', 'bV2}naZ5V_=!O', NULL, 'CC', '7203367592', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Lamont', 'Marrison', 'lmarrison2n@infoseek.co.jp', 'zW7\>SiW!@3<8nR_', '130.122.171.101', 'CC', '9966616443', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Oralia', 'Dempsey', 'oodempsey2o@wired.com', 'aL7#_frp', '12.185.64.18', 'CC', '406053658', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Michelle', 'McNeice', 'mmcneice2p@friendfeed.com', 'uQ7>Uz~H`,X7mEXU', NULL, 'CC', '8229017306', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Jinny', 'Moran', 'jmoran2q@google.com', 'bB5@tS{$,', '27.178.42.58', 'CC', '8874380660', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Kipp', 'Trump', 'ktrump2r@ezinearticles.com', 'tJ6%ehPalX', '133.151.210.231', 'CC', '64887342', NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL);

-- Insertar datos en la tabla "parking"
DELETE FROM "parking";
ALTER SEQUENCE parking_id_seq RESTART WITH 1;
INSERT INTO parking (park_name, spaces, street_address, admin_id, city_id, parking_type_id, loyalty_id, created_date, deleted_date) VALUES
    ('Estacion Fácil', 27, 'Calle 30 A No 6-25/38', 5, 1, 1, NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('ParqueSeguro', 48, 'Cra 7 No 61 - 47', 6, 1, 2, 2, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('EspacioParking', 33, 'Calle 12 B No. 71 D - 61', 8, 1, 2, NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('EstacionaYa', 40, 'CL 25B Sur N. 5 - 87', 9, 1, 2, 1, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('AutoGuardado', 37, 'Avda. 19 No 102 -31', 10, 1, 1, NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('ParqueCentro', 27, 'Cra. 64 #97', 11, 2, 3, 3, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('ParkVivo', 41, 'Cl. 49b #66', 13, 2, 2, 1, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('PlazaMotor', 26, 'Cl. 45 #54-51', 17, 2, 3, 2, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('EstacionaRápido', 45, '52, Av. Palacé #28', 18, 2, 1, NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('ParkingTotal', 39, 'Tv. 71a #31F-05', 21, 3, 2, 2, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('AutoAlmacén', 21, 'Dg. 32 #71-53', 25, 3, 3, NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('ParkCiudad', 25, 'Cl. 31d #64-95', 27, 3, 3, 1, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('GuardaAuto', 21, 'Cra. 7 #14-64', 28, 4, 3, NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('EstacionaExpress', 20, 'Cra. 5 #15-11', 31, 4, 1, 1, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('ParqueCentral', 33, 'Cl. 11 # 3-70', 32, 5, 3, 1, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Parqueadero Central', 29, 'Cra. 7 #116A - 40', 33, 5, 3, NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Parqueo Fácil', 52, 'Cra. 55 #77-44', 34, 6, 3, 2, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Park Barranquilla', 37, 'Cra. 52 #76-95', 42, 6, 3, 1, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Parqueadero Express', 41, 'Cra. 55 #72-55', 43, 6, 2, 1, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Estacionamiento Ágil', 33, 'Cra. 18 #No 34 - 15', 44, 7, 1, 2, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('Park & Ride', 32, 'Cl. 34 #12-48', 45, 7, 2, NULL, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL);


-- Insertar datos en la tabla "booking"
DELETE FROM "booking";
ALTER SEQUENCE booking_id_seq RESTART WITH 1;
INSERT INTO booking (check_in, check_out, user_id, parking_id, vehicle_id, created_date, deleted_date) VALUES
    ('2024-02-26 07:00:00-05', '2024-02-26 13:00:00-05', 41, 14, 16, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('2023-10-17 08:00:00-05', '2023-10-17 12:00:00-05', 7, 6, 11, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('2023-10-16 09:00:00-05', '2023-10-16 11:00:00-05', 12, 21, 2, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('2024-04-28 10:00:00-05', '2024-04-28 13:00:00-05', 24, 8, 19, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('2024-04-03 11:00:00-05', '2024-04-03 14:00:00-05', 84, 7, 12, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('2023-10-12 12:00:00-05', '2023-10-12 15:00:00-05', 89, 20, 17, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('2023-11-14 13:00:00-05', '2023-11-14 16:00:00-05', 63, 2, 5, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('2024-06-06 14:00:00-05', '2024-06-06 17:00:00-05', 89, 13, 10, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('2024-06-05 15:00:00-05', '2024-06-05 18:00:00-05', 35, 14, 3, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('2023-09-12 16:00:00-05', '2023-09-12 19:00:00-05', 36, 20, 8, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('2023-06-25 17:00:00-05', '2023-06-25 20:00:00-05', 3, 19, 13, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('2023-08-24 18:00:00-05', '2023-08-24 21:00:00-05', 98, 6, 6, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('2024-03-13 19:00:00-05', '2024-03-13 22:00:00-05', 70, 6, 18, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('2023-11-21 20:00:00-05', '2023-11-21 23:00:00-05', 37, 1, 4, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('2023-07-27 21:00:00-05', '2023-07-27 24:00:00-05', 26, 9, 14, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('2023-10-06 22:00:00-05', '2023-10-07 01:00:00-05', 38, 10, 15, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('2024-02-08 23:00:00-05', '2024-02-08 24:00:00-05', 16, 18, 16, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('2023-10-25 24:00:00-05', '2023-10-26 02:00:00-05', 7, 5, 9, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('2024-02-10 01:00:00-05', '2024-02-10 03:00:00-05', 77, 17, 7, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('2024-08-24 02:00:00-05', '2024-08-24 05:00:00-05', 65, 20, 20, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
    ('2024-02-22 03:00:00-05', '2024-02-22 05:00:00-05', 3, 1, 1, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL);


-- Insertar datos en la tabla "parking_schedule"
INSERT INTO parking_schedule (parking_id, schedule_id)
VALUES
(1, 1), 
(2, 2),
(3, 3), 
(4, 4), 
(5, 5), 
(6, 1), 
(7, 2), 
(8, 3), 
(9, 4), 
(10, 5), 
(11, 1), 
(12, 2), 
(13, 3), 
(14, 4), 
(15, 5), 
(16, 1), 
(17, 2), 
(18, 3), 
(19, 4), 
(20, 5), 
(21, 1);

-- Insertar datos en la tabla "parking_fee"
INSERT INTO parking_fee (fee_id, parking_id)
VALUES
(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1),
(1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2),
(1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3),
(1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4),
(1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5),
(1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6),
(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7),
(1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8),
(1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9),
(1, 10), (2, 10), (3, 10), (4, 10), (5, 10), (6, 10), (7, 10), (8, 10),
(1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11),
(1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12),
(1, 13), (2, 13), (3, 13), (4, 13), (5, 13), (6, 13), (7, 13), (8, 13),
(1, 14), (2, 14), (3, 14), (4, 14), (5, 14), (6, 14), (7, 14), (8, 14),
(1, 15), (2, 15), (3, 15), (4, 15), (5, 15), (6, 15), (7, 15), (8, 15),
(1, 16), (2, 16), (3, 16), (4, 16), (5, 16), (6, 16), (7, 16), (8, 16),
(1, 17), (2, 17), (3, 17), (4, 17), (5, 17), (6, 17), (7, 17), (8, 17),
(1, 18), (2, 18), (3, 18), (4, 18), (5, 18), (6, 18), (7, 18), (8, 18),
(1, 19), (2, 19), (3, 19), (4, 19), (5, 19), (6, 19), (7, 19), (8, 19),
(1, 20), (2, 20), (3, 20), (4, 20), (5, 20), (6, 20), (7, 20), (8, 20),
(1, 21), (2, 21), (3, 21), (4, 21), (5, 21), (6, 21), (7, 21), (8, 21);


-- Insertar datos en la tabla "payment_method"
DELETE FROM payment_method;
ALTER SEQUENCE payment_method_id_seq RESTART WITH 1;
INSERT INTO payment_method (description, created_date, deleted_date)
VALUES ('tarjeta', CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL );

-- Insertar datos en la tabla "points"
DELETE FROM points;
ALTER SEQUENCE points_id_seq RESTART WITH 1;
INSERT INTO points (amount, user_id, created_date, deleted_date)
VALUES
(14, 77, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
(9, 73, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
(9, 69, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
(12, 65, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
(13, 61, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
(19, 57, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
(3, 53, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
(20, 49, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
(11, 46, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
(3, 41, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
(11, 37, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
(4, 26, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
(20, 29, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
(5, 24, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
(20, 23, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
(2, 16, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
(8, 15, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
(15, 7, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
(12, 4, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
(3, 1, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL);


-- Insertar datos en la tabla "role"
DELETE FROM role;
ALTER SEQUENCE role_id_seq RESTART WITH 1;
INSERT INTO role (description, created_date, deleted_date)
VALUES
('usuario', CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
('administrador', CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL),
('gerente', CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota', NULL);


-- Insertar datos en la tabla "user_role"
INSERT INTO user_role (user_id, role_id)
VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 1),
(5, 2),
(6, 2),
(7, 1),
(8, 2),
(9, 2),
(10, 2),
(11, 2),
(12, 1),
(13, 2),
(14, 1),
(15, 1),
(16, 1),
(17, 2),
(18, 2),
(19, 1),
(20, 1),
(21, 2),
(22, 1),
(23, 1),
(24, 1),
(25, 2),
(26, 1),
(27, 2),
(28, 2),
(29, 1),
(30, 1),
(31, 2),
(32, 2),
(33, 2),
(34, 2),
(35, 1),
(36, 1),
(37, 1),
(38, 1),
(39, 1),
(40, 1),
(41, 1),
(42, 2),
(43, 2),
(44, 2),
(45, 2),
(46, 1),
(47, 1),
(48, 1),
(49, 1),
(50, 1),
(51, 1),
(52, 1),
(53, 1),
(54, 1),
(55, 1),
(56, 1),
(57, 1),
(58, 1),
(59, 1),
(60, 1),
(61, 1),
(62, 1),
(63, 1),
(64, 1),
(65, 1),
(66, 1),
(67, 1),
(68, 1),
(69, 1),
(70, 1),
(71, 1),
(72, 1),
(73, 1),
(74, 1),
(75, 1),
(76, 1),
(77, 1),
(78, 1),
(79, 1),
(80, 1),
(81, 1),
(82, 1),
(83, 1),
(84, 1),
(85, 1),
(86, 1),
(87, 1),
(88, 1),
(89, 1),
(90, 1),
(91, 1),
(92, 1),
(93, 1),
(94, 1),
(95, 1),
(96, 1),
(97, 1),
(98, 1),
(99, 1),
(100, 1);


-- Insertar datos en la tabla "bill"
DELETE FROM bill;
ALTER SEQUENCE bill_id_seq RESTART WITH 1;
INSERT INTO bill (code, vehicle_entry, vehicle_exit, total_time, points_used, total_amount, booking_id, payment_method_id, created_date)
VALUES
    ('191qa23q', '2024-02-26 07:00:00-05', '2024-02-26 13:00:00-05', '06:00:00', 18, 19644, 1, 1, current_timestamp AT TIME ZONE 'America/Bogota'),
    ('250dp65i', '2023-10-17 08:00:00-05', '2023-10-17 12:00:00-05', '04:00:00', 1, 7740, 2, 1, current_timestamp AT TIME ZONE 'America/Bogota'),
    ('268cq05v', '2023-10-16 09:00:00-05', '2023-10-16 11:00:00-05', '02:00:00', 1, 8675, 3, 1, current_timestamp AT TIME ZONE 'America/Bogota'),
    ('676pa44g', '2024-04-28 10:00:00-05', '2024-04-28 13:00:00-05', '03:00:00', 3, 16900, 4, 1, current_timestamp AT TIME ZONE 'America/Bogota'),
    ('014dp40l', '2024-04-03 11:00:00-05', '2024-04-03 14:00:00-05', '03:00:00', 4, 11098, 5, 1, current_timestamp AT TIME ZONE 'America/Bogota'),
    ('413gm17j', '2023-10-12 12:00:00-05', '2023-10-12 15:00:00-05', '03:00:00', 18, 8837, 6, 1, current_timestamp AT TIME ZONE 'America/Bogota'),
    ('332hh58u', '2023-11-14 13:00:00-05', '2023-11-14 16:00:00-05', '03:00:00', 12, 6639, 7, 1, current_timestamp AT TIME ZONE 'America/Bogota'),
    ('656ww06f', '2024-06-06 14:00:00-05', '2024-06-06 17:00:00-05', '03:00:00', 11, 17277, 8, 1, current_timestamp AT TIME ZONE 'America/Bogota'),
    ('298mu32m', '2024-06-05 15:00:00-05', '2024-06-05 18:00:00-05', '03:00:00', 16, 7419, 9, 1, current_timestamp AT TIME ZONE 'America/Bogota'),
    ('967sk28a', '2023-09-12 16:00:00-05', '2023-09-12 19:00:00-05', '03:00:00', 17, 19630, 10, 1, current_timestamp AT TIME ZONE 'America/Bogota'),
    ('872aq97q', '2023-06-25 17:00:00-05', '2023-06-25 20:00:00-05', '03:00:00', 6, 15500, 11, 1, current_timestamp AT TIME ZONE 'America/Bogota'),
    ('794vd81n', '2023-08-24 18:00:00-05', '2023-08-24 21:00:00-05', '03:00:00', 2, 9190, 12, 1, current_timestamp AT TIME ZONE 'America/Bogota'),
    ('181rc02j', '2024-03-13 19:00:00-05', '2024-03-13 22:00:00-05', '03:00:00', 8, 7876, 13, 1, current_timestamp AT TIME ZONE 'America/Bogota'),
    ('759fj13y', '2023-11-21 20:00:00-05', '2023-11-21 23:00:00-05', '03:00:00', 18, 10602, 14, 1, current_timestamp AT TIME ZONE 'America/Bogota'),
    ('248og77r', '2023-07-27 21:00:00-05', '2023-07-27 24:00:00-05', '03:00:00', 8, 17364, 15, 1, current_timestamp AT TIME ZONE 'America/Bogota'),
    ('898lr37u', '2023-10-06 22:00:00-05', '2023-10-07 01:00:00-05', '03:00:00', 2, 12527, 16, 1, current_timestamp AT TIME ZONE 'America/Bogota'),
    ('865ut23j', '2024-02-08 23:00:00-05', '2024-02-08 24:00:00-05', '01:00:00', 3, 18657, 17, 1, current_timestamp AT TIME ZONE 'America/Bogota'),
    ('631ec61e', '2023-10-25 24:00:00-05', '2023-10-26 02:00:00-05', '02:00:00', 1, 17936, 18, 1, current_timestamp AT TIME ZONE 'America/Bogota'),
    ('839pl76h', '2024-02-10 01:00:00-05', '2024-02-10 03:00:00-05', '02:00:00', 14, 18304, 19, 1, current_timestamp AT TIME ZONE 'America/Bogota'),
    ('332wx20l', '2024-08-24 02:00:00-05', '2024-08-24 05:00:00-05', '03:00:00', 4, 18926, 20, 1, current_timestamp AT TIME ZONE 'America/Bogota'),
    ('322pb80k', '2024-02-22 03:00:00-05', '2024-02-22 05:00:00-05', '02:00:00', 2, 6712, 21, 1, current_timestamp AT TIME ZONE 'America/Bogota');


-- Insertar datos en la tabla "credit_card"
DELETE FROM credit_card;
ALTER SEQUENCE credit_card_id_seq RESTART WITH 1;
INSERT INTO credit_card (card_number, cardholder_name, expiration_date, cvv, client_id, created_date)
VALUES
('5100133625743850', 'Merilyn Lamonby', '2023-06-30', '204', 1, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4041376620621', 'Lenora Alenichev', '2024-04-05', '248', 2, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4041599019023', 'Matthieu Ivankov', '2023-11-17', '738', 3, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('5038115303232870', 'Marleah Golborn', '2024-04-08', '758', 4, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('5330113528014100', 'Kalie Shea', '2023-11-27', '925', 7, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4017957921971190', 'Fina Swayton', '2023-12-19', '351', 12, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4017951480814440', 'Cosette Sweetland', '2023-06-05', '977', 14, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('5266777456879960', 'Bert McVicar', '2023-12-28', '540', 15, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('5108752778329490', 'Gordy Hamber', '2024-01-30', '491', 16, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4017955295191', 'Erhart Motherwell', '2024-01-10', '497', 19, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4017954733159380', 'Selestina Pontain', '2023-08-02', '623', 20, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('5100143262633850', 'Suellen Parminter', '2023-08-26', '349', 22, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('5010128279312890', 'Loleta Fedorski', '2024-03-06', '785', 23, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4041375671196680', 'Vonni Caldero', '2023-05-25', '278', 24, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('5543166308977660', 'Meier Wein', '2023-05-05', '499', 26, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4783972210454830', 'Nona Enston', '2023-05-27', '318', 29, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('5893058569858640', 'Cherrita Haspineall', '2023-09-16', '818', 30, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('374622097169493', 'Diann Deporte', '2023-09-07', '249', 35, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4041376589248', 'Cleveland Wheal', '2024-01-16', '731', 36, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4017958545042250', 'Carol-jean Ferreras', '2023-11-14', '659', 37, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4504208604513420', 'Ciro Symmons', '2023-12-01', '424', 38, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('337941459503370', 'Kellina Godlip', '2023-12-31', '529', 39, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4017951074251', 'Kimberlyn Dansie', '2023-09-09', '951', 40, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('5274306095935470', 'Reade Paice', '2023-06-06', '192', 41, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('5100140807025660', 'Elliot Murr', '2023-10-29', '677', 46, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('5893437481285540000', 'Lemar Cuffe', '2023-11-20', '791', 47, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4017956413704290', 'Ally Burkart', '2023-07-06', '283', 48, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('340454095175640', 'Isaak Tomkies', '2024-04-14', '876', 49, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('5100171144750000', 'Fidel Bernuzzi', '2023-12-24', '506', 50, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4041375707827430', 'Ebenezer Brosoli', '2023-09-04', '599', 51, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('374283124328733', 'Gil Shade', '2023-08-11', '922', 52, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('676115565928496000', 'Miltie Stoodale', '2023-08-24', '854', 53, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('374288895055464', 'Deloris Willgress', '2023-09-23', '667', 54, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4335882130152', 'Clevie Janc', '2024-02-06', '583', 55, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4041590170726', 'Ulrich Kneller', '2023-07-27', '709', 56, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('5048370100106160', 'Gordie Rann', '2023-11-27', '274', 57, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('5038974560183280000', 'Shermie Grundey', '2023-09-27', '335', 58, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4041379499031', 'Mill Grieg', '2023-06-02', '719', 59, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('337941761196376', 'Berti Pretley', '2023-05-20', '290', 60, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('63042932503341600', 'Kimball Fitch', '2023-08-11', '443', 61, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('6046696263539260', 'Caesar Bretelle', '2023-09-23', '235', 62, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('5002357325739610', 'Tamera Cubley', '2024-01-22', '395', 63, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('342613539504396', 'Melly Taberner', '2023-06-08', '451', 64, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4041598500753300', 'Biddie Mufford', '2023-09-25', '438', 65, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4041594305328', 'Marji Elijahu', '2023-09-27', '139', 66, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('5100148850955700', 'Andrej Matthai', '2023-10-15', '855', 67, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('374283848874152', 'Deni Hepher', '2023-11-20', '953', 68, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('676216688561356000', 'Nannie Poles', '2023-11-03', '422', 69, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('374622860513497', 'Farrell Whitehouse', '2023-12-16', '558', 70, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('604534313460636000', 'Gaylene Philippson', '2023-06-01', '121', 71, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('502007042542777000', 'Doralynne Hensmans', '2023-09-07', '511', 72, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4041377419825', 'Jody Behagg', '2023-06-08', '325', 73, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('374283642454615', 'Nevsa Casham', '2023-11-26', '933', 74, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('5318611404613900', 'Papagena Hultberg', '2024-02-22', '129', 75, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('5010121106128930', 'Diane-marie Swannick', '2023-08-15', '699', 76, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('5100175434165800', 'Raff Morilla', '2023-08-28', '794', 77, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('372301530703596', 'Abelard Etteridge', '2024-04-13', '285', 78, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4017957477995', 'Benjie Greenhouse', '2023-06-12', '663', 79, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('50207667951723000', 'Christoforo McGookin', '2024-02-20', '959', 80, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('5100998251526700', 'Sallee Dark', '2023-10-08', '784', 81, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('6761126449019040', 'Rollie Dubery', '2023-05-12', '555', 82, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('5020450808002970', 'Dalt Loosley', '2023-05-22', '803', 83, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4017951298174080', 'Fonsie Venard', '2023-07-30', '302', 84, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('337941181461657', 'Danell Massey', '2023-07-31', '871', 85, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4017958211286', 'Kahlil Anshell', '2023-12-14', '472', 86, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('372301976333064', 'Bethany Diprose', '2023-08-02', '430', 87, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4017952902658', 'Paco Dalgliesh', '2024-01-26', '378', 88, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('374369780632763', 'Ann-marie Hasslocher', '2023-06-17', '530', 89, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('5138623289163410', 'Carmon Skayman', '2023-06-29', '324', 90, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('60407984008226800', 'Randi Wiburn', '2023-12-15', '590', 91, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4041379254212220', 'Windy Pagon', '2024-03-13', '663', 92, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('5100138213334930', 'Nissie Haynesford', '2023-10-08', '744', 93, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('374622047845374', 'Fredi Alans', '2024-01-09', '176', 94, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('6762148437657530', 'Torrin Maplestone', '2024-03-12', '697', 95, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('374622893884030', 'Ruthi Andre', '2023-09-17', '981', 96, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('6762935693410480', 'Sigrid Howey', '2024-04-02', '484', 97, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('373294173410513', 'Luciana Kingsnode', '2023-12-07', '638', 98, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4041596707893', 'Averil Cullen', '2023-11-12', '941', 99, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota'),
('4017958815325310', 'Tatiana Putley', '2023-05-07', '162', 100, CURRENT_TIMESTAMP AT TIME ZONE 'America/Bogota');
