-- Export des données de SQLite vers PostgreSQL
-- Généré le 2025-06-14 10:47:08

-- Données pour la table sqlite_sequence
TRUNCATE TABLE sqlite_sequence RESTART IDENTITY CASCADE;
INSERT INTO sqlite_sequence (name, seq) VALUES ('django_migrations', 62);
INSERT INTO sqlite_sequence (name, seq) VALUES ('account_emailaddress', 10);
INSERT INTO sqlite_sequence (name, seq) VALUES ('django_admin_log', 101);
INSERT INTO sqlite_sequence (name, seq) VALUES ('django_content_type', 24);
INSERT INTO sqlite_sequence (name, seq) VALUES ('auth_permission', 96);
INSERT INTO sqlite_sequence (name, seq) VALUES ('auth_group', 6);
INSERT INTO sqlite_sequence (name, seq) VALUES ('auth_user', 19);
INSERT INTO sqlite_sequence (name, seq) VALUES ('django_site', 1);
INSERT INTO sqlite_sequence (name, seq) VALUES ('socialaccount_socialapp', 0);
INSERT INTO sqlite_sequence (name, seq) VALUES ('socialaccount_socialaccount', 0);
INSERT INTO sqlite_sequence (name, seq) VALUES ('auth_group_permissions', 109);
INSERT INTO sqlite_sequence (name, seq) VALUES ('auth_user_groups', 10);
INSERT INTO sqlite_sequence (name, seq) VALUES ('hotel_floor', 9);
INSERT INTO sqlite_sequence (name, seq) VALUES ('hotel_roomtype', 21);
INSERT INTO sqlite_sequence (name, seq) VALUES ('hotel_depense', 8);
INSERT INTO sqlite_sequence (name, seq) VALUES ('hotel_room', 27);
INSERT INTO sqlite_sequence (name, seq) VALUES ('userAccount_profil', 16);
INSERT INTO sqlite_sequence (name, seq) VALUES ('hotel_coupon', 0);
INSERT INTO sqlite_sequence (name, seq) VALUES ('hotel_facture', 0);
INSERT INTO sqlite_sequence (name, seq) VALUES ('hotel_booking', 35);
INSERT INTO sqlite_sequence (name, seq) VALUES ('hotel_payment', 5);
INSERT INTO sqlite_sequence (name, seq) VALUES ('hotel_reservation', 10);

-- Données pour la table auth_group_permissions
TRUNCATE TABLE auth_group_permissions RESTART IDENTITY CASCADE;
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (1, 1, 1);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (2, 1, 2);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (3, 1, 3);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (4, 1, 4);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (5, 1, 5);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (6, 1, 6);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (7, 1, 7);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (8, 1, 8);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (9, 1, 9);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (10, 1, 10);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (11, 1, 11);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (12, 1, 12);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (13, 1, 13);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (14, 1, 14);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (15, 1, 15);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (16, 1, 16);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (17, 1, 17);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (18, 1, 18);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (19, 1, 19);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (20, 1, 20);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (21, 1, 21);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (22, 1, 22);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (23, 1, 23);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (24, 1, 24);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (25, 1, 25);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (26, 1, 26);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (27, 1, 27);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (28, 1, 28);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (29, 1, 29);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (30, 1, 30);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (31, 1, 31);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (32, 1, 32);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (33, 1, 33);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (34, 1, 34);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (35, 1, 35);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (36, 1, 36);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (37, 1, 37);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (38, 1, 38);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (39, 1, 39);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (40, 1, 40);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (41, 1, 41);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (42, 1, 42);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (43, 1, 43);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (44, 1, 44);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (45, 1, 45);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (46, 1, 46);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (47, 1, 47);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (48, 1, 48);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (49, 1, 49);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (50, 1, 50);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (51, 1, 51);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (52, 1, 52);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (53, 1, 53);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (54, 1, 54);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (55, 1, 55);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (56, 1, 56);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (57, 1, 57);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (58, 1, 58);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (59, 1, 59);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (60, 1, 60);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (61, 1, 61);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (62, 1, 62);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (63, 1, 63);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (64, 1, 64);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (65, 1, 65);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (66, 1, 66);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (67, 1, 67);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (68, 1, 68);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (69, 1, 69);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (70, 1, 70);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (71, 1, 71);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (72, 1, 72);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (73, 1, 73);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (74, 1, 74);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (75, 1, 75);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (76, 1, 76);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (77, 1, 77);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (78, 1, 78);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (79, 1, 79);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (80, 1, 80);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (81, 3, 68);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (82, 3, 72);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (83, 3, 76);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (84, 3, 77);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (85, 3, 78);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (86, 3, 79);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (87, 3, 80);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (88, 3, 60);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (89, 2, 57);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (90, 2, 60);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (91, 2, 64);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (92, 2, 68);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (93, 2, 72);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (94, 2, 76);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (95, 2, 77);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (96, 2, 78);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (97, 2, 80);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (98, 4, 64);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (99, 4, 68);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (100, 4, 72);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (101, 4, 76);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (102, 4, 77);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (103, 4, 13);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (104, 4, 16);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (105, 4, 80);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (106, 4, 81);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (107, 4, 84);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (108, 4, 57);
INSERT INTO auth_group_permissions (id, group_id, permission_id) VALUES (109, 4, 60);

-- Données pour la table auth_user_groups
TRUNCATE TABLE auth_user_groups RESTART IDENTITY CASCADE;
INSERT INTO auth_user_groups (id, user_id, group_id) VALUES (1, 1, 1);
INSERT INTO auth_user_groups (id, user_id, group_id) VALUES (4, 12, 4);
INSERT INTO auth_user_groups (id, user_id, group_id) VALUES (6, 14, 2);

-- Données pour la table account_emailaddress
TRUNCATE TABLE account_emailaddress RESTART IDENTITY CASCADE;
INSERT INTO account_emailaddress (id, verified, primary, user_id, email) VALUES (6, 0, 1, 12, 'grace@gmail.com');
INSERT INTO account_emailaddress (id, verified, primary, user_id, email) VALUES (8, 0, 1, 14, 'espe@gmail.com');

-- Données pour la table auth_group
TRUNCATE TABLE auth_group RESTART IDENTITY CASCADE;
INSERT INTO auth_group (id, name) VALUES (1, 'admin');
INSERT INTO auth_group (id, name) VALUES (2, 'sécrétaire');
INSERT INTO auth_group (id, name) VALUES (3, 'client');
INSERT INTO auth_group (id, name) VALUES (4, 'gérant');
INSERT INTO auth_group (id, name) VALUES (5, 'ménagère');
INSERT INTO auth_group (id, name) VALUES (6, 'caissière');

-- Données pour la table auth_user
TRUNCATE TABLE auth_user RESTART IDENTITY CASCADE;
INSERT INTO auth_user (id, password, last_login, is_superuser, username, last_name, email, is_staff, is_active, date_joined, first_name) VALUES (1, 'pbkdf2_sha256$260000$fYRLSe7yst3hzzUjykaF38$TTkaoexGaD2hGH7MSs/XF2evALnkU5T7sGCa/bKKNtU=', '2025-06-14 08:06:31.865336', 1, 'admin', '', 'angezanou00@gmail.com', 1, 1, '2022-03-18 02:33:07', '');
INSERT INTO auth_user (id, password, last_login, is_superuser, username, last_name, email, is_staff, is_active, date_joined, first_name) VALUES (12, 'pbkdf2_sha256$260000$pldfJM5Sr1ufJ6XSHEny4s$YtmwtZlGVUZ+tduobMWAjpbGomRjBKGEf4vzOo9sLko=', '2023-09-16 06:57:01.562798', 0, 'zbgl', '', 'grace@gmail.com', 0, 1, '2022-06-12 22:14:07.993228', '');
INSERT INTO auth_user (id, password, last_login, is_superuser, username, last_name, email, is_staff, is_active, date_joined, first_name) VALUES (14, 'pbkdf2_sha256$260000$iyTGPylDSeBMsYzBORh4Ye$in7+8ZXVYkajzFa6qd5QO8MnVhrqHsE0f4bePuum6WQ=', '2023-09-14 08:09:40.699207', 0, 'espe', '', 'espe@gmail.com', 0, 1, '2022-06-12 22:18:37.998275', '');
INSERT INTO auth_user (id, password, last_login, is_superuser, username, last_name, email, is_staff, is_active, date_joined, first_name) VALUES (19, 'pbkdf2_sha256$260000$ZtOVfd9TKJqSbg2wT0sIua$YtgitARn/lg38g/HDx8uneOWKTS+BHFFl+UZwILXGWo=', NULL, 1, 'lesage', '', 'angezanou00@gmail.com', 1, 1, '2025-06-10 19:13:15.674323', '');

-- Données pour la table hotel_floor
TRUNCATE TABLE hotel_floor RESTART IDENTITY CASCADE;
INSERT INTO hotel_floor (id, name, description, number, status, created_at, updated_at) VALUES (9, 'Pas d''etage', 'Cet etage indique qu''il n''y a pas d''étage', 0, 'actif', '2023-09-14 16:49:48.524830', '2023-09-14 16:49:48.524872');

-- Données pour la table hotel_roomtype
TRUNCATE TABLE hotel_roomtype RESTART IDENTITY CASCADE;
INSERT INTO hotel_roomtype (id, name, description, numberAdult, numberChildren, price, created_at, updated_at) VALUES (18, 'Junior', 'Ce type de chambre represente les chambre standard', 3, 1, 12500, '2023-09-14 16:52:01.570299', '2023-09-14 16:52:01.570347');
INSERT INTO hotel_roomtype (id, name, description, numberAdult, numberChildren, price, created_at, updated_at) VALUES (19, 'senior', 'senior', 5, 3, 15000, '2023-09-14 17:01:56.094917', '2025-06-11 19:49:42.553198');
INSERT INTO hotel_roomtype (id, name, description, numberAdult, numberChildren, price, created_at, updated_at) VALUES (20, 'mini-suite', 'mini-suite', 4, 2, 25000, '2023-09-14 17:02:48.299538', '2025-06-11 19:49:29.119718');

-- Données pour la table hotel_depense
TRUNCATE TABLE hotel_depense RESTART IDENTITY CASCADE;
INSERT INTO hotel_depense (id, title, description, amount, date, created_at, updated_at, spent_by_id) VALUES (7, 'achat de compléments', 'Nous avons achetés des produits en compléments de ce qui manquait', 5000, '2022-06-17', '2022-06-17 20:57:39.107319', '2022-06-17 20:57:39.107394', 6);

-- Données pour la table hotel_room
TRUNCATE TABLE hotel_room RESTART IDENTITY CASCADE;
INSERT INTO hotel_room (id, number, created_at, updated_at, floor_id, type_id, status) VALUES (12, 'CH1', '2023-09-14 16:52:33.465171', '2023-09-14 16:52:33.465214', 9, 18, 'lp');
INSERT INTO hotel_room (id, number, created_at, updated_at, floor_id, type_id, status) VALUES (13, 'ch2', '2023-09-14 17:06:50.048166', '2025-06-11 19:53:20.166167', 9, 18, 'ls');
INSERT INTO hotel_room (id, number, created_at, updated_at, floor_id, type_id, status) VALUES (14, 'CH3', '2023-09-14 17:08:11.082803', '2023-09-14 17:08:11.082838', 9, 18, 'lp');
INSERT INTO hotel_room (id, number, created_at, updated_at, floor_id, type_id, status) VALUES (15, 'CH3', '2023-09-14 17:08:56.105272', '2023-09-14 17:08:56.105311', 9, 18, 'lp');
INSERT INTO hotel_room (id, number, created_at, updated_at, floor_id, type_id, status) VALUES (16, 'CH4', '2023-09-14 17:09:16.971960', '2023-09-14 17:09:16.972003', 9, 18, 'lp');
INSERT INTO hotel_room (id, number, created_at, updated_at, floor_id, type_id, status) VALUES (17, 'CH5', '2023-09-14 17:09:41.544951', '2023-09-14 17:09:41.545010', 9, 18, 'lp');
INSERT INTO hotel_room (id, number, created_at, updated_at, floor_id, type_id, status) VALUES (18, 'CH6', '2023-09-14 17:10:03.414226', '2023-09-14 17:10:03.414263', 9, 18, 'lp');
INSERT INTO hotel_room (id, number, created_at, updated_at, floor_id, type_id, status) VALUES (19, 'CH7', '2023-09-14 17:10:24.045849', '2023-09-14 17:10:24.045887', 9, 18, 'lp');
INSERT INTO hotel_room (id, number, created_at, updated_at, floor_id, type_id, status) VALUES (20, 'CH8', '2023-09-14 17:10:46.820092', '2023-09-14 17:10:46.820129', 9, 18, 'lp');
INSERT INTO hotel_room (id, number, created_at, updated_at, floor_id, type_id, status) VALUES (21, 'CH9', '2023-09-14 17:11:09.364360', '2023-09-14 17:11:09.364424', 9, 19, 'lp');
INSERT INTO hotel_room (id, number, created_at, updated_at, floor_id, type_id, status) VALUES (22, 'CH10', '2023-09-14 17:11:34.943643', '2025-06-11 23:17:11.712305', 9, 19, 'og');
INSERT INTO hotel_room (id, number, created_at, updated_at, floor_id, type_id, status) VALUES (23, 'CH11', '2023-09-14 17:11:54.785934', '2025-06-11 19:54:04.274351', 9, 19, 'ls');
INSERT INTO hotel_room (id, number, created_at, updated_at, floor_id, type_id, status) VALUES (24, 'CH12', '2023-09-14 17:12:21.715975', '2025-06-11 19:54:00.267516', 9, 19, 'ls');
INSERT INTO hotel_room (id, number, created_at, updated_at, floor_id, type_id, status) VALUES (25, 'CH14', '2023-09-14 17:12:57.241957', '2025-06-11 19:53:56.773057', 9, 19, 'ls');
INSERT INTO hotel_room (id, number, created_at, updated_at, floor_id, type_id, status) VALUES (26, 'CH15', '2023-09-14 17:13:24.800664', '2025-06-11 23:17:17.165353', 9, 20, 'og');
INSERT INTO hotel_room (id, number, created_at, updated_at, floor_id, type_id, status) VALUES (27, 'CH16', '2023-09-14 17:13:53.037629', '2025-06-11 19:53:50.086698', 9, 20, 'ls');

-- Données pour la table userAccount_profil
TRUNCATE TABLE userAccount_profil RESTART IDENTITY CASCADE;
INSERT INTO userAccount_profil (id, avatar, phone, name, email, created_at, updated_at, user_id, address, department, dob, firstname, gender, idNumber, idType, role_id, domicile, father, id_delivered_by, job, mother, nationnalite, id_delivered_at, place_of_birth, id_delivered_place) VALUES (5, 'avatars/usericon.png', '0747277080', 'Zanou', 'grace@gmail.com', '2022-06-12 22:24:36.543509', '2022-06-12 23:39:25.107035', 12, 'Yamoussoukro', NULL, '2004-06-02', 'Grace Lauraine', 'femme', 'C56780987567', 'cni', 4, NULL, NULL, '2023-09-20 16:06:33.011143+00:00', NULL, NULL, NULL, '2023-09-20', NULL, '');
INSERT INTO userAccount_profil (id, avatar, phone, name, email, created_at, updated_at, user_id, address, department, dob, firstname, gender, idNumber, idType, role_id, domicile, father, id_delivered_by, job, mother, nationnalite, id_delivered_at, place_of_birth, id_delivered_place) VALUES (6, 'avatars/usericon.png', '+3345678765567', 'Zannou', 'espe@gmail.com', '2022-06-12 22:26:25.861782', '2022-06-12 23:39:11.137702', 14, 'Le mans', NULL, '2004-06-02', 'esperance', 'femme', 'C567809876545', 'cni', 2, NULL, NULL, '2023-09-20 16:06:33.011143+00:00', NULL, NULL, NULL, '2023-09-20', NULL, '');
INSERT INTO userAccount_profil (id, avatar, phone, name, email, created_at, updated_at, user_id, address, department, dob, firstname, gender, idNumber, idType, role_id, domicile, father, id_delivered_by, job, mother, nationnalite, id_delivered_at, place_of_birth, id_delivered_place) VALUES (13, 'avatars/usericon.png', '0787572030', 'Zanou', 'angezanou00@gmail.com', '2023-09-20 15:40:31.201724', '2023-09-20 16:32:23.254837', 1, '00225', 'Cote d''Ivoire', '2023-09-20', 'Ange Aymar', 'homme', 'CI845120515', 'cni', 1, 'maison de moi', 'Papa de moi', 'derriere ma piece', 'travail de moi', 'maman de moi', 'ma nationnalité', '2023-09-20', 'Abidjan', 'Abidjan');
INSERT INTO userAccount_profil (id, avatar, phone, name, email, created_at, updated_at, user_id, address, department, dob, firstname, gender, idNumber, idType, role_id, domicile, father, id_delivered_by, job, mother, nationnalite, id_delivered_at, place_of_birth, id_delivered_place) VALUES (16, 'avatars/usericon.png', '0787572030', 'Zanou', 'angezanou00@gmail.com', '2025-06-10 19:24:54.014776', '2025-06-10 19:24:54.014776', NULL, 'Yopougon keneya pharmacie la maison blanche', NULL, '1999-01-10', 'Ange Aymar', 'homme', 'ci05465586255', 'cni', 3, 'Cocody angré', 'Zanou Marcel', 'goh coulibaly', 'Informaticien', 'Velah Claudine', 'ivoirienne', '2025-01-03', 'gopoupleu', 'abidjan');

-- Données pour la table hotel_payment
TRUNCATE TABLE hotel_payment RESTART IDENTITY CASCADE;
INSERT INTO hotel_payment (id, amount, status, type, created_at, updated_at, booking_id) VALUES (1, 15000, 'dp', 'espece', '2025-06-13 10:40:35.418848', '2025-06-13 10:40:35.418848', 35);
INSERT INTO hotel_payment (id, amount, status, type, created_at, updated_at, booking_id) VALUES (2, 15000, 'dp', 'espece', '2025-06-13 10:44:17.404737', '2025-06-13 10:44:17.404737', 35);
INSERT INTO hotel_payment (id, amount, status, type, created_at, updated_at, booking_id) VALUES (3, 5000, 'dp', 'espece', '2025-06-13 11:40:55.771250', '2025-06-13 11:40:55.771250', 32);
INSERT INTO hotel_payment (id, amount, status, type, created_at, updated_at, booking_id) VALUES (4, 1000, 'pj', 'espece', '2025-06-13 12:33:38.318805', '2025-06-13 12:33:38.318805', 31);
INSERT INTO hotel_payment (id, amount, status, type, created_at, updated_at, booking_id) VALUES (5, 5000, 'dp', 'espece', '2025-06-13 12:36:45.957098', '2025-06-13 12:36:45.957098', 30);

-- Données pour la table hotel_booking
TRUNCATE TABLE hotel_booking RESTART IDENTITY CASCADE;
INSERT INTO hotel_booking (id, checkIn, checkOut, status, created_at, updated_at, coupon_id, guest_id, recorded_by_id, room_id, reference, totalPrice, payment, adults, children, amountPaid, amountDue) VALUES (30, '2025-06-10 12:00:00', '2025-06-11 12:00:00', 'dt', '2025-06-10 19:26:27.063440', '2025-06-13 12:36:45.952199', NULL, 16, 13, 27, '1786aa8dc5', 25000, 'espece', 1, 0, 5000, 20000);
INSERT INTO hotel_booking (id, checkIn, checkOut, status, created_at, updated_at, coupon_id, guest_id, recorded_by_id, room_id, reference, totalPrice, payment, adults, children, amountPaid, amountDue) VALUES (31, '2025-06-11 22:27:00', '2025-06-12 13:59:00', 'pj', '2025-06-11 22:27:38.267557', '2025-06-13 12:33:38.313894', NULL, 16, 13, 22, 'eb6f9407bb', 30000, 'espece', 2, 0, 1000, 29000);
INSERT INTO hotel_booking (id, checkIn, checkOut, status, created_at, updated_at, coupon_id, guest_id, recorded_by_id, room_id, reference, totalPrice, payment, adults, children, amountPaid, amountDue) VALUES (32, '2025-06-11 22:28:00', '2025-06-12 22:28:00', 'pj', '2025-06-11 22:29:13.839872', '2025-06-13 11:40:55.764405', NULL, 16, 13, 26, '5aba1d6013', 50000, 'espece', 1, 0, 5000, 45000);
INSERT INTO hotel_booking (id, checkIn, checkOut, status, created_at, updated_at, coupon_id, guest_id, recorded_by_id, room_id, reference, totalPrice, payment, adults, children, amountPaid, amountDue) VALUES (35, '2025-06-11 23:37:00', '2025-06-12 23:37:00', 'pj', '2025-06-11 23:38:03.382165', '2025-06-13 10:44:17.396401', NULL, 16, 13, 21, '861b29c36f', 30000, 'espece', 1, 0, 15000, 15000);

-- Données pour la table hotel_reservation
TRUNCATE TABLE hotel_reservation RESTART IDENTITY CASCADE;
INSERT INTO hotel_reservation (id, reference, checkIn, checkOut, created_at, updated_at, guest_id, recorded_by_id, room_id, status) VALUES (10, 'f5e794fa95', '2025-06-11 22:28:00', '2025-06-12 22:28:00', '2025-06-11 22:28:57.692967', '2025-06-11 22:31:28.200865', 16, 13, 26, 'confirmée');
