const express = require('express')
const multer = require('multer');
const pu = require('./controllers/podacastUpload')
const ga = require('./controllers/getArticles')
const app = express()
const port = process.env.PORT|| 3000

app.use('/podcasts',express.static('podcasts'))
app.use(express.urlencoded({extended:true}))

const storageOptions = multer.diskStorage({
    destination:(req,file,callback)=>{
        callback(null,'./podcasts/')
     },
    filename:(req,file,callback)=>{
        callback(null,new Date().toString()+file.originalname)
     }
})
const upload = multer({storage:storageOptions})
app.get('/getArticles',ga.getArticles)
app.get('/',(req,res)=>{res.redirect('/getArticles')})
app.post('/podcasts',upload.single('podcast'),pu.podcasts)
app.listen(port, () => console.log(`Example app listening on port ${port}!`))
