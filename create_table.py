import pymysql

schema_name = "freedb_devops"

# Establishing a connection to DB
conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_lalala', passwd='P!?k!gbS*5QXnU8', db=schema_name)
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Inserting data into table
statementToExecute = "CREATE TABLE `"+schema_name+"`.`project`(`id` VARCHAR(36) NOT NULL,`name` VARCHAR(45) NOT NULL, PRIMARY KEY (`id`), `Create_Date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);"
cursor.execute(statementToExecute)

cursor.close()
conn.close()
