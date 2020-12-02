const db = require('../connector');
exports.getArticles = async (req,res)=>{
    sql = `select * from quickies `
    
    try {
        const   [result,fields] = await db.execute(sql)
        console.log(result);
        res.status(200).json(result)
        
    } catch (error) {
        console.log(error)
    
    }
}
