
# Get IP proxy

[proxy](https://www.us-proxy.org/)

```shell
cat temp.txt | awk -F '[\t]' '{print "http"" ""http://"$1":"$2" "$7}' > proxies/ipproxy.txt 
```

[kuaidaili](http://www.kuaidaili.com/free/)

```shell
cat temp.txt | awk -F '[\t]' '{print "http"" ""http://"$1":"$2}' > proxies/ipproxy.txt
```

# SQL

```sql
CREATE DATABASE testDB;


CREATE TABLE `bilibili_user_info` (
    `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
    `mid` VARCHAR(11) DEFAULT NULL,
    `name` VARCHAR(45) DEFAULT NULL,
    `sex` VARCHAR(11) DEFAULT NULL,
    `face` VARCHAR(200) DEFAULT NULL,
    `coins` INT(11) DEFAULT NULL,
    `regtime` VARCHAR(45) DEFAULT NULL,
    `spacesta` INT(11) DEFAULT NULL,
    `birthday` VARCHAR(45) DEFAULT NULL,
    `place` VARCHAR(45) DEFAULT NULL,
    `description` VARCHAR(45) DEFAULT NULL,
    `article` INT(11) DEFAULT NULL,
    `fans` INT(11) DEFAULT NULL,
    `friend` INT(11) DEFAULT NULL,
    `attention` INT(11) DEFAULT NULL,
    `sign` VARCHAR(300) DEFAULT NULL,
    `attentions` TEXT,
    `level` INT(11) DEFAULT NULL,
    `exp` INT(11) DEFAULT NULL,
    PRIMARY KEY (`id`)
)  ENGINE=MYISAM DEFAULT CHARSET=UTF8;
```
