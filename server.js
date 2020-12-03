const express = require('express')
const app = express()
const port = process.env.PORT|| 3000
const ga = require('./controllers/getArticles')
app.get('/getArticles',ga.getArticles)
app.get('/',(req,res)=>{res.send("please go to /getArticles")})
app.listen(port, () => console.log(`Example app listening on port ${port}!`))
