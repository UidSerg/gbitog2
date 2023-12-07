## Итоговая контрольная работа

Информация о проекте

Необходимо организовать систему учета для питомника в котором живут домашние и Pack animals.

Как сдавать проект

Для сдачи проекта необходимо создать отдельный общедоступный репозиторий(Github, gitlub, или Bitbucket). Разработку вести в этом репозитории, использовать пул реквесты на изменения. Программа должна запускаться и работать, ошибок при выполнении программы быть не должно. Программа, может использоваться в различных системах, поэтому необходимо разработать класс в виде конструктора

> Задание

Операционные системы и виртуализация (Linux)

1. Использование команды cat в Linux

- Создать два текстовых файла: "Pets"(Домашние животные) и "Pack animals"(вьючные животные), используя команду `cat` в терминале Linux. В первом файле перечислить собак, кошек и хомяков. Во втором — лошадей, верблюдов и ослов.

- Объединить содержимое этих двух файлов в один и просмотреть его содержимое.

- Переименовать получившийся файл в "Human Friends".

Пример конечного вывода после команды “ls” :

Desktop Documents Downloads HumanFriends.txt Music PackAnimals.txt Pets.txt Pictures Videos

        1  cat > Pets.txt
        2  cat > PackAnimals.txt
        3  cat Pets.txt PackAnimals.txt > HumanFriends.txt
        4  cat HumanFriends.txt 
        5  ls
        6  history


![скрин](work_1.jpg)

2. Работа с директориями в Linux

- Создать новую директорию и переместить туда файл "Human Friends".

        7  mkdir control_work
        8  mv HumanFriends.txt control_work/HumanFriends.txt
        9  cd control_work
        10  ls
        11  history

![скрин2](work_2.jpg)

3. Работа с MySQL в Linux. “Установить MySQL на вашу вычислительную машину ”

- Подключить дополнительный репозиторий MySQL и установить один из пакетов из этого репозитория.    
    
        12  sudo apt install nginx
        13  sudo apt install curl
        14  curl localhost
        15  sudo apt install mysql-server
        16  sudo mysql_secure_installation
        17  sudo mysql
            mysql>SELECT * FROM mysql.user;
            mysql>ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY '12355321';
            mysql>exit
        18  sudo mysql -u root -p
            mysql>CREATE USER 'newuser'@'localhost' IDENTIFIED BY '12pass21';
            mysql>SELECT * FROM mysql.user;
            mysql>exit
        19  sudo mysql -u newuser -p
        20  history


4. Управление deb-пакетами

- Установить и затем удалить deb-пакет, используя команду `dpkg`.

        21  wget https://download.virtualbox.org/virtualbox/7.0.10/virtualbox-7.0_7.0.10-158379~Ubuntu~jammy_amd64.deb
        22  ll
        23  sudo dpkg -i virtualbox-7.0_7.0.10-158379~Ubuntu~jammy_amd64.deb
        24  virtualbox --help

![скрин4](work_4.jpg)
        
        25  sudo dpkg -r virtualbox-7.0
        26  virtualbox --help


![скрин41](work_41.jpg)

        27  history

5. История команд в терминале Ubuntu

- Сохранить и выложить историю ваших терминальных команд в Ubuntu.

В формате: Файла с ФИО, датой сдачи, номером группы(или потока)

   [История в файле](Damchenko_S.I.4589_05.12.23.txt "Дамченко С.И дата: 05/12/23 ГР4589")

<hr/>
<hr/>

## Объектно-ориентированное программирование 

6. Диаграмма классов
- Создать диаграмму классов с родительским классом "Животные", и двумя подклассами: "Pets" и "Pack animals".
В составы классов которых в случае Pets войдут классы: собаки, кошки, хомяки, а в класс Pack animals войдут: Лошади, верблюды и ослы).
Каждый тип животных будет характеризоваться (например, имена, даты рождения, выполняемые команды и т.д)
Диаграмму можно нарисовать в любом редакторе, такими как Lucidchart, Draw.io, Microsoft Visio и других.

![Диаграмма классов](diag_animals.drawio.png)

7. Работа с MySQL (Задача выполняется в случае успешного выполнения задачи “Работа с MySQL в Linux. “Установить MySQL на вашу машину”

7.1. После создания диаграммы классов в 6 пункте, в 7 пункте база данных "Human Friends" должна быть структурирована в соответствии с этой диаграммой. Например, можно создать таблицы, которые будут соответствовать классам "Pets" и "Pack animals", и в этих таблицах будут поля, которые характеризуют каждый тип животных (например, имена, даты рождения, выполняемые команды и т.д.). 
7.2   - В ранее подключенном MySQL создать базу данных с названием "Human Friends".
- Создать таблицы, соответствующие иерархии из вашей диаграммы классов.
- Заполнить таблицы данными о животных, их командах и датами рождения.

 ``` 
 ## создадим БД
 CREATE SCHEMA `Human Friends` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci ;

 ## таблица типов животных (домашние, вьючные)
 
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

## таблица род(вид) животных (кошка, собака, осел и тд)

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

## таблица команд

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

## таблица животных

CREATE TABLE `human friends`.`animals` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `birthdate` DATE NOT NULL,
  `various_animals` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;
-- заполним данные
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

## таблица животные - команды

CREATE TABLE `human friends`.`animal_comm` (
`id` INT NOT NULL AUTO_INCREMENT,
`id_com` INT NOT NULL,
`id_animal` INT NOT NULL,
PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;
-- заполним данные
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

```
   - Удалить записи о верблюдах и объединить таблицы лошадей и ослов.
```
select a.*, va.name_v , GROUP_CONCAT(c.command ORDER BY c.command ASC SEPARATOR ', ') as "команды " from animals a
join animal_comm ac ON ac.id_animal=a.id
join commands c ON ac.id_com=c.id
join various_animals va ON a.various_animals=va.id_v
join type_animal t ON va.id_t=t.id_t
where t.name_t="въючные" and va.name_v != "Camel"
GROUP BY a.id, a.name, a.birthdate, a.various_animals, va.name_v;
```
   - Создать новую таблицу для животных в возрасте от 1 до 3 лет и вычислить их возраст с точностью до месяца.

 ```
SELECT a.*, va.name_v AS "вид",
CONCAT(TIMESTAMPDIFF(YEAR, a.birthdate, CURDATE())," years ", TIMESTAMPDIFF(MONTH, a.birthdate, CURDATE()) % 12," months") AS "возраст" 
FROM animals a
JOIN various_animals va ON a.various_animals=va.id_v
JOIN type_animal t ON va.id_t=t.id_t
WHERE TIMESTAMPDIFF(YEAR, a.birthdate, CURDATE()) BETWEEN 1 AND 2.99;
 ```  
   - Объединить все созданные таблицы в одну, сохраняя информацию о принадлежности к исходным таблицам.
<table>
    <thead>
        <tr>
            <th>id</th>
            <th>Name</th>
            <th>Type</th>
            <th>birthdate</th>
            <th>Commands</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">1</td>
            <td align="center">Fido</td>
            <td align="center">Dog</td>
            <td align="center">2020-01-01</td>
            <td align="left">Sit, Stay, Fetch</td>
        </tr>
        <tr>
            <td align="center">2</td>
            <td align="center">Whiskers</td>
            <td align="center">Cat</td>
            <td align="center">2019-05-15</td>
            <td align="left">Sit, Pounce</td>
        </tr>
        <tr>
            <td align="center">3</td>
            <td align="center">Hammy</td>
            <td align="center">Hamster</td>
            <td align="center">2021-03-10</td>
            <td align="left">Roll, Hide</td>
        </tr>
        <tr>
            <td align="center">4</td>
            <td align="center">Buddy</td>
            <td align="center">Dog</td>
            <td align="center">2018-12-10</td>
            <td align="left">Sit, Paw, Bark</td>
        </tr>
    </tbody>
</table>
и тд., полная таблица в задании.

```
select a.id, a.name, a.birthdate, t.name_t AS "тип", va.name_v AS "вид", GROUP_CONCAT(c.command ORDER BY c.command ASC SEPARATOR ', ') as "выполняемые команды " from animals a
join animal_comm ac ON ac.id_animal=a.id
join commands c ON ac.id_com=c.id
join various_animals va ON a.various_animals=va.id_v
join type_animal t ON va.id_t=t.id_t
GROUP BY a.id, a.name, a.birthdate, a.various_animals, va.name_v;  
```
> Файл с SQL запросами: [запросы SQL](bd.sql "запросы SQL")

<hr/>
<hr/>

### 8. ООП и Java

- Создать иерархию классов в Java, который будет повторять диаграмму классов созданную в задаче 6(Диаграмма классов) .

9. Программа-реестр домашних животных
- Написать программу на Java, которая будет имитировать реестр домашних животных. 
Должен быть реализован следующий функционал:
    
9.1. Добавление нового животного
- Реализовать функциональность для добавления новых животных в реестр.       
 Животное должно определяться в правильный класс (например, "собака", "кошка", "хомяк" и т.д.)

9.2. Список команд животного
- Вывести список команд, которые может выполнять добавленное животное (например, "сидеть", "лежать").
        
9.3. Обучение новым командам
- Добавить возможность обучать животных новым командам.

9.4 Вывести список животных по дате рождения
9.5. Навигация по меню
- Реализовать консольный пользовательский интерфейс с меню для навигации между вышеуказанными функциями.
10. Счетчик животных
Создать механизм, который позволяет вывести на экран общее количество созданных животных любого типа (Как домашних, так и вьючных), то есть при создании каждого нового животного счетчик увеличивается на “1”. 
