const db = require('../connector');

exports.podcasts=async (req,res)=>{
console.log(req.file)
let category = req.body.category
let sql = `insert into podcasts values (id+1,'${category}','${req.file.path}')`
console.log(sql)
try {
    let [result,field] = await db.execute(sql)
    console.log(result)
} catch (error) {
    console.log(error)
}
res.status(200).json({uploaded:"true",pathRecorded:`${req.file.path}`})
}
