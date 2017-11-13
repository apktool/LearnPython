
# Get IP proxy

[proxy](https://www.us-proxy.org/)

```shell
cat temp.txt | awk -F '[\t]' '{print "http"" ""http://"$1":"$2" "$7}' > proxies/ipproxy.txt 
```

[kuaidaili](http://www.kuaidaili.com/free/)

```shell
cat temp.txt | awk -F '[\t]' '{print "http"" ""http://"$1":"$2}' > proxies/ipproxy.txt
```

[xicidaili](http://www.xicidaili.com/)

```shell
cat temp.txt | awk -F '[\t]' '{print "http"" ""http://"$2":"$3}' > proxies/ipproxy.txt
```

# SQL

```sql
CREATE DATABASE testDB;

CREATE TABLE `bilibili_anime_info` (
    `uuid` VARCHAR(37),
    `mid` VARCHAR(11) DEFAULT NULL,
    `season_id` INT(10) DEFAULT NULL,
    `title` VARCHAR(45) DEFAULT NULL,
    `brief` VARCHAR(300) DEFAULT NULL,
    `favorites` INT(10) DEFAULT NULL,
	`total_count` INT(3) DEFAULT NULL, 
    `is_finish` TINYINT(1) DEFAULT NULL,
    `last_ep_index` INT(100) DEFAULT NULL,
    `newest_ep_index` INT(100) DEFAULT NULL,
    `cover` VARCHAR(300) DEFAULT NULL,
    `share_url` VARCHAR(100) DEFAULT NULL,
    `evaluate` VARCHAR(100) DEFAULT NULL,
    PRIMARY KEY (`uuid`)
)  ENGINE=MYISAM DEFAULT CHARSET=UTF8;
```
