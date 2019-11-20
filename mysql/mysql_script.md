## link

https://jasperxu.github.io/gorm-zh/database.html#m



## gorm操作



```go
import (
    "github.com/jinzhu/gorm"
    _ "github.com/jinzhu/gorm/dialects/mysql"
)

func main() {
  db, err := gorm.Open("mysql", "user:password@/dbname?charset=utf8&parseTime=True&loc=Local")
  defer db.Close()
}
```



```go
package scripts

import (
	"fmt"
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/mysql"
	"time"
)

var (
	MySQLClient *gorm.DB
)

const (
	USERNAME        = ""
	PASSWORD        = ""
	NETWORK         = "tcp"
	SERVER          = "127.0.0.1"
	PORT            = 3306
	DATABASE        = ""
	maxOpenConns    = 100
	maxIdleConns    = 15
	connMaxLifeTime = 3600 * time.Second
)

func initMySQL() {
	conn := fmt.Sprintf("%s:%s@%s(%s:%d)/%s?parseTime=true&loc=Local", USERNAME, PASSWORD, NETWORK, SERVER, PORT, DATABASE)
	db, err := gorm.Open("mysql", conn)
	if err != nil {
		fmt.Printf("gorm Open failed, err: %s", err)
	}
	
	MySQLClient = db
	MySQLClient.SingularTable(true)
	MySQLClient.DB().SetMaxOpenConns(maxOpenConns)
	MySQLClient.DB().SetMaxIdleConns(maxIdleConns)
	MySQLClient.DB().SetConnMaxLifetime(connMaxLifeTime)
}
```

