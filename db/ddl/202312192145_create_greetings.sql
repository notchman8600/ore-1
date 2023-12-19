-- ユーザーテーブルの作成
create table greetings(
    id int PRIMARY KEY AUTO_INCREMENT,
    user_id int,
    comment text not null,
    created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) DEFAULT CHARSET = utf8mb4 ENGINE = InnoDB;

-- 適当な挨拶を作成
insert into
    greetings(user_id, comment)
values
    (1, 'こんにちは');

insert into
    greetings(user_id, comment)
values
    (2, 'こんばんは');
