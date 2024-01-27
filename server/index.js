const express=require('express');
const mongoose=require('mongoose');
const bodyParser=require('body-parser');
const cors=require('cors');
require('dotenv').config();
const PORT=process.env.PORT;
const app=express();


app.use(bodyParser.urlencoded({extended:false}));
app.use(bodyParser.json());

app.use(cors({
    origin:'http://localhost:3000',
    method:['GET','POST']
}));

app.listen(PORT,()=>{
    console.log('Server is listening on port: '+PORT);
})