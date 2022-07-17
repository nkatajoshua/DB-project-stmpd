CREATE TABLE `artists` (
  `Artist_id` integer,
  `Artsit_name` text
);

CREATE TABLE `releases` (
  `Artist2_id` integer,
  `Track2_id` integer,
  `Album2_id` integer,
  `Genre2_id` integer
);

CREATE TABLE `tracks` (
  `Track_id` integer,
  `Track_name` TEXT
);

CREATE TABLE `albums` (
  `Album_id` integer,
  `Album_name` text
);

CREATE TABLE `genre` (
  `Genre_id` integer,
  `Genre_name` TEXT
);

ALTER TABLE `artists` ADD FOREIGN KEY (`Artist_id`) REFERENCES `releases` (`Track2_id`);

ALTER TABLE `tracks` ADD FOREIGN KEY (`Track_id`) REFERENCES `releases` (`Album2_id`);

ALTER TABLE `albums` ADD FOREIGN KEY (`Album_id`) REFERENCES `releases` (`Genre2_id`);

ALTER TABLE `genre` ADD FOREIGN KEY (`Genre_id`) REFERENCES `releases` (`Artist2_id`);
