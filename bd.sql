-- создание бд
CREATE SCHEMA `Human Friends` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;

-- список команд
CREATE TABLE `human friends`.`commads` (
  `id` INT NOT NULL,
  `commad` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

-- таблица животные
CREATE TABLE `human friends`.`animals` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `birthdate` DATE NOT NULL,
  `type_animal` INT NOT NULL,
  `various_animals` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;

-- типы животных
CREATE TABLE `human friends`.`type_animal` (
  `id_t` INT NOT NULL AUTO_INCREMENT,
  `name_t` VARCHAR(45) NULL,
  PRIMARY KEY (`id_t`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;
-- заполняем
INSERT INTO `human friends`.`type_animal` (`name_t`) VALUES ('домашние');
INSERT INTO `human friends`.`type_animal` (`name_t`) VALUES ('въючные'); 

-- таблица род(вид) животных (кошка, собака, осел и тд)
CREATE TABLE `human friends`.`various_animals` (
  `id_v` INT NOT NULL AUTO_INCREMENT,
  `name_v` VARCHAR(45) NULL,
  `id_t` INT NULL,
  PRIMARY KEY (`id_v`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;
-- заполняем
INSERT INTO `human friends`.`various_animals` (`name_v`, `id_t`) VALUES ('Cat', 1),
        ('Dog', 1),
        ('Hamster', 1),
        ('Horse', 2),
        ('Camel', 2),
        ('Donkey', 2);

-- заполняем таблицу животных
INSERT INTO `human friends`.`animals` (`name`, `birthdate`, `various_animals`)
VALUES('Fido', '2020-01-01', 2),
        ('Whiskers', '2019-05-15', 1),
        ('Hammy', '2021-03-10', 3),
        ('Buddy', '2018-12-10', 2),
        ('Smudge', '2020-02-20', 1),
        ('Peanut', '2021-08-01', 3),
        ('Bella', '2019-11-11', 2),
        ('Oliver', '2020-06-30', 1),
        ('Thunder', '2015-07-21', 4),
        ('Sandy', '2016-11-03', 5),
        ('Eeyore', '2017-09-18', 6),
        ('Storm', '2014-05-05', 5),
        ('Dune', '2018-12-12', 5),
        ('Burro', '2019-01-23', 6),
        ('Blaze', '2016-02-29', 4),
        ('Sahara', '2015-08-14', 5);
        
-- список команд        
CREATE TABLE `human friends`.`commands` (
`id` INT NOT NULL AUTO_INCREMENT,
`command` VARCHAR(45) NULL,
PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;
-- заполняем
INSERT INTO `human friends`.`commands` (`command`)
VALUES ('Sit'),
        ('Stay'),
        ('Fetch'),
        ('Pounce'),
        ('Roll'),
        ('Hide'),
        ('Paw'),
        ('Bark'),
        ('Scratch'),
        ('Spin'),
        ('Meow'),
        ('Jump'),
        ('Trot'),
        ('Canter'),
        ('Gallop'),
        ('Walk'),
        ('Carry Load'),
        ('Bray'),
        ('Kick'),
        ('Run');
        
-- таблица список команд для животного    
CREATE TABLE `human friends`.`animal_comm` (
`id` INT NOT NULL AUTO_INCREMENT,
`id_com` INT NOT NULL,
`id_animal` INT NOT NULL,
PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;
-- заполняем
INSERT INTO `human friends`.`animal_comm` (`id_com`, `id_animal`)
VALUES (1,1),(2,1),(3,1),
        (1,2),(4,2),
        (5,3),(6,3),
        (1,4),(7,4),(8,4),
        (1,5),(4,5),(9,5),
        (4,6),(10,6),
        (1,7),(2,7),(5,7),
        (11,8),(9,8),(12,8),
        (13,9),(14,9),(15,9),
        (16,10),(17,10),
        (16,11),(17,11),(18,11),
        (13,12),(14,12),
        (16,13),(1,13),
        (16,14),(18,14),(19,14),
        (13,15),(12,15),(15,15),
        (16,16),(20,16);

-- без берблюдов 
select a.*, va.name_v , GROUP_CONCAT(c.command ORDER BY c.command ASC SEPARATOR ', ') as "команды " from animals a
join animal_comm ac ON ac.id_animal=a.id
join commands c ON ac.id_com=c.id
join various_animals va ON a.various_animals=va.id_v
join type_animal t ON va.id_t=t.id_t
where t.name_t="въючные" and va.name_v != "Camel"
GROUP BY a.id, a.name, a.birthdate, a.various_animals, va.name_v;
 
-- от 1-го до 3х лет с текущей даты
SELECT a.*, va.name_v AS "вид",
CONCAT(TIMESTAMPDIFF(YEAR, a.birthdate, CURDATE())," years ", TIMESTAMPDIFF(MONTH, a.birthdate, CURDATE()) % 12," months") AS "возраст" 
FROM animals a
JOIN various_animals va ON a.various_animals=va.id_v
JOIN type_animal t ON va.id_t=t.id_t
WHERE TIMESTAMPDIFF(YEAR, a.birthdate, CURDATE()) BETWEEN 1 AND 2.99;
   
-- вся инфа   
select a.id, a.name, a.birthdate, t.name_t AS "тип", va.name_v AS "вид", GROUP_CONCAT(c.command ORDER BY c.command ASC SEPARATOR ', ') as "выполняемые команды " from animals a
join animal_comm ac ON ac.id_animal=a.id
join commands c ON ac.id_com=c.id
join various_animals va ON a.various_animals=va.id_v
join type_animal t ON va.id_t=t.id_t
GROUP BY a.id, a.name, a.birthdate, a.various_animals, va.name_v;   
   
   
   