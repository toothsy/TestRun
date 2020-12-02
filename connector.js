const mysql = require('mysql2');
const connection = mysql.createPool({
    host: "localhost",
    user: "test",
    password: "481526",
    database: "bookSouls",
    port:"3306",
    connectTimeout:"15000" 
})
module.exports = connection.promise();