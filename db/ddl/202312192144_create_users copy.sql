-- ユーザーテーブルの作成
create table users(
    id int PRIMARY KEY AUTO_INCREMENT,
    user_name varchar(255),
    email varchar(255),
    created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_name)
) DEFAULT CHARSET = utf8mb4 ENGINE = InnoDB;

-- 適当なユーザーを作成
insert into
    users(user_name, email)
values
    ('dora', 'hoge@example.com');

insert into
    users(user_name, email)
values
    ('doraemon', 'piyo@example.com');