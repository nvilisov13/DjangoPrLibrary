INSERT INTO "library_BooksAuthors" ("id", "first_name", "last_name") VALUES
	(1, 'Стивен', 'Кинг'),
	(2, 'Роберт', 'Гелбрэйт'),
	(3, 'Колин', 'Маккалоу'),
	(4, 'Джеймс', 'Боуэн'),
	(5, 'Джордж', 'Оруэлл'),
	(6, 'Джордан', 'Белфорт'),
	(7, 'Кассандра', 'Клэр'),
	(8, 'Энтони', 'Берджесс'),
	(9, 'Стивен', 'Чбоски'),
	(10, 'Джоджо', 'Мойес'),
	(11, 'Александр', 'Дюма');


INSERT INTO "library_Books" ("id", "name", "description", "author_id") VALUES
	(1, 'Страна радости', 'Мистика, 2013', 1),
	(2, 'Зов кукушки', 'Детектив, 2013', 2),
	(3, 'Поющие в терновике', 'Классика, 1977', 3),
	(4, 'Мир глазами кота Боба', 'Драма, 2013', 4),
	(5, '1984', 'Антиутопия, 1949', 5),
	(6, 'Волк с Уолл-стрит', 'Автобиография, 2007', 6),
	(7, 'Город потерянных душ', 'Фентези, 2012', 7),
	(8, 'Заводной апельсин', 'Антиутопия, 1962', 8),
	(9, 'Хорошо быть тихоней', 'Современная литература, 1999', 9),
	(10, 'Корабль невест', 'Современная литература, 2005', 10),
	(11, 'Граф Монте-Кристо', 'Приключенческий роман, классика французской литературы, 1844', 11),
	(12, 'Три мушкетёра', 'Роман, 1844', 11),
	(13, 'Двадцать лет спустя', 'Историко-приключенческий роман, 1845', 11),
	(14, 'Чёрный тюльпан', 'Роман, 1850', 11),
	(15, 'Виконт де Бражелон, или Десять лет спустя', 'Роман, 1850', 11),
	(16, 'Королева Марго', 'Исторический роман, 1845', 11),
	(17, 'Графиня де Монсоро', 'Роман, 1846', 11),
	(18, 'История Щелкунчика', 'Фикшн, 1844', 11),
	(19, 'Ожерелье королевы', 'Проза, 1849', 11),
	(20, 'Две Дианы', 'Фикшн, 1846', 11),
	(21, 'Pauline', 'Ужасы, 1838', 11),
	(22, 'El Hombre de La Mascara de Hierro', 'Фикшн, 1847', 11);


INSERT INTO "library_Readers" ("id", "first_name", "last_name", "phone") VALUES
	(1, 'Олег', 'Щенин', '954650600'),
	(2, 'Георгий', 'Арцишевский', '980650980'),
	(3, 'Марина', 'Верясова', '946540877'),
	(4, 'Эмилия', 'Кравчук', '984065404'),
	(5, 'Александр', 'Татаринов', '987054044'),
	(6, 'Вероника', 'Камбарова', '987011221'),
	(7, 'Глеб', 'Ярцев', '989074787'),
	(8, 'Владимир', 'Луковников', '980745111'),
	(9, 'Олег', 'Гребенщиков', '984044848'),
	(10, 'Кристина', 'Павленко', '654012121'),
	(11, 'Валерий', 'Ситников', '406504650'),
	(12, 'Евгений', 'Нусинов', '406065466'),
	(13, 'Никита', 'Бекетов', NULL),
	(14, 'Михаил', 'Червяков', NULL),
	(15, 'Михаил', 'Гриненко', NULL),
	(16, 'Алексей', 'Бестужев', NULL),
	(17, 'Дмитрий', 'Рыбалкин', NULL),
	(18, 'Артем', 'Горбунов', NULL),
	(19, 'Евгений', 'Стариков', NULL),
	(20, 'Дмитрий', 'Гентофт', NULL),
	(21, 'Андрей', 'Стрекалов', NULL),
	(22, 'Максим', 'Ильяхов', NULL);


INSERT INTO "library_MarksBooks" ("id", "mark", "date_issue", "reader_id", "book_id") VALUES
	(1, 3, '1993-01-23', 11, 10),
	(2, 2, '1993-02-21', 16, 9),
	(3, 4, '1994-03-05', 15, 16),
	(4, 2, '1994-04-16', 8, 14),
	(5, 3, '1994-07-27', 2, 22),
	(6, 3, '1994-11-28', 14, 20),
	(7, 1, '1995-01-23', 4, 6),
	(8, 1, '1995-05-21', 21, 7),
	(9, 5, '1995-09-25', 3, 15),
	(10, 5, '1995-12-15', 15, 10),
	(11, 4, '1996-03-29', 15, 3),
	(12, 5, '1996-08-30', 7, 10),
	(13, 3, '1997-02-15', 16, 21),
	(14, 1, '1997-04-18', 9, 12),
	(15, 2, '1997-06-19', 1, 17),
	(16, 3, '1998-02-03', 14, 1),
	(17, 4, '1998-05-14', 16, 2),
	(18, 3, '1998-08-19', 6, 4),
	(19, 3, '1999-01-21', 17, 19),
	(20, 5, '1999-02-17', 6, 22),
	(21, 3, '1999-07-18', 8, 13),
	(22, 1, '1999-12-19', 3, 17),
	(23, 1, '2000-01-09', 12, 2),
	(24, 1, '2000-04-14', 22, 20),
	(25, 4, '2000-06-15', 21, 3),
	(26, 2, '2001-02-16', 8, 4),
	(27, 5, '2001-06-17', 2, 2),
	(28, 5, '2001-11-08', 4, 10),
	(29, 5, '2002-01-19', 1, 14),
	(30, 4, '2002-09-20', 5, 11),
	(31, 2, '2003-01-21', 6, 22),
	(32, 3, '2003-08-22', 4, 7),
	(33, 4, '2004-03-12', 14, 2),
	(34, 2, '2004-09-15', 3, 11),
	(35, 3, '2004-11-18', 15, 14);


INSERT INTO "library_BooksReaders" ("id", "book_id", "reader_id") VALUES
	(1, 10, 4),
	(2, 4, 2),
	(3, 1, 1),
	(4, 3, 11),
	(5, 2, 16),
	(6, 12, 9),
	(7, 18, 20),
	(8, 8, 13),
	(9, 5, 17),
	(10, 14, 19),
	(11, 20, 22),
	(12, 9, 15),
	(13, 21, 3),
	(14, 15, 8),
	(15, 16, 12),
	(16, 17, 5),
	(17, 7, 6),
	(18, 13, 7),
	(19, 19, 8);
