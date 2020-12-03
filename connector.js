const mysql = require('mysql2');
const connection = mysql.createPool({
    host: "bovjj5ckvtapvajqrfos-mysql.services.clever-cloud.com",
    user: "uquazjpy4t4uxomq",
    password: "uquazjpy4t4uxomq",
    database: "bovjj5ckvtapvajqrfos",
    port:"3306",
    connectTimeout:"15000" 
})
module.exports = connection.promise();