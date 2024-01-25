const express=require('express');
const mongoose=require('mongoose');
require('dotenv').config();
const PORT=process.env.PORT;
const app=express();



app.listen(PORT,()=>{
    console.log('Server is listening on port: '+PORT);
})