-- Отримати всі завдання певного користувача. Використайте SELECT для отримання завдань конкретного користувача за його user_id.

select u.email, t.* from tasks as t
left join public.users u on u.id = t.user_id
where u.id = 50;

-- Вибрати завдання за певним статусом. Використайте підзапит для вибору завдань з конкретним статусом, наприклад, 'new'.
select s.name, t.* from tasks as t
left join public.status s on s.id = t.status_id
where status_id in (select id from status where name in ('new', 'in progress'));

-- Оновити статус конкретного завдання. Змініть статус конкретного завдання на 'in progress' або інший статус.
update tasks set status_id = (select id from status where name = 'new') 
where id = 1;

-- Отримати список користувачів, які не мають жодного завдання. Використайте комбінацію SELECT, WHERE NOT IN і підзапит.
-- delete from tasks where user_id = 20
select u.* from users as u
where u.id not in (select user_id from tasks);

-- Додати нове завдання для конкретного користувача. Використайте INSERT для додавання нового завдання.
insert into tasks (title, description, status_id, user_id) values ('Нове завдання', 'Опис', 1, 20);

-- Отримати всі завдання, які ще не завершено. Виберіть завдання, чий статус не є 'завершено'.

select s.name, t.* from tasks as t
   left join public.status s on s.id = t.status_id
   where t.status_id not in (select id from status where name = 'completed');

-- Видалити конкретне завдання. Використайте DELETE для видалення завдання за його id.
delete from tasks where id = 1001;

-- Знайти користувачів з певною електронною поштою. Використайте SELECT із умовою LIKE для фільтрації за електронною поштою.
select * from users where email like '%john%';

-- Оновити ім'я користувача. Змініть ім'я користувача за допомогою UPDATE.
update users set fullname = 'goit user1' where id = 1

-- Отримати кількість завдань для кожного статусу. Використайте SELECT, COUNT, GROUP BY для групування завдань за статусами.
select s.name, count(t.*) as count from tasks as t
    left join public.status s on s.id = t.status_id
    group by s.name;

-- Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти. Використайте SELECT з умовою LIKE в поєднанні з JOIN, щоб вибрати завдання, призначені користувачам, чия електронна пошта містить певний домен (наприклад, '%@example.com').
select * from users where email like '%@example.com';

-- Отримати список завдань, що не мають опису. Виберіть завдання, у яких відсутній опис.
select * from tasks where description is null;

-- Вибрати користувачів та їхні завдання, які є у статусі 'in progress'. Використайте INNER JOIN для отримання списку користувачів та їхніх завдань із певним статусом.
select users.fullname, status.name, tasks.title from users
inner join tasks on users.id = tasks.user_id
inner join status on tasks.status_id = status.id
where status.name = 'in progress';

-- Отримати користувачів та кількість їхніх завдань. Використайте LEFT JOIN та GROUP BY для вибору користувачів та підрахунку їхніх завдань.
select users.fullname, count(tasks.id) as task_count from users
left join tasks on users.id = tasks.user_id
group by users.fullname;