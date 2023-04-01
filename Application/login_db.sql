create database MLlogin;
use MLlogin;
CREATE TABLE login_tbl (
  id INT AUTO_INCREMENT PRIMARY KEY,
  usrname VARCHAR(255) NOT NULL,
  passwrd VARCHAR(255) NOT NULL);
INSERT INTO login_tbl (usrname, passwrd)
VALUES ('abhay', 'hellomoto');
INSERT INTO login_tbl (usrname, passwrd)
VALUES ('admin', '1234');
