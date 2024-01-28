const express=require('express');
const mongoose=require('mongoose');
const bodyParser=require('body-parser');
const cors=require('cors');
require('dotenv').config();
const PORT=process.env.PORT;
const ApiRoutes=require('./routes/routes');
const app=express();

mongoose.connect('mongodb+srv://pahwagautam47:8689014713@cluster0.ple4jr3.mongodb.net/?retryWrites=true&w=majority');

const db=mongoose.connection;

db.once('open',()=>{
    console.log('Connected to MongoDB');
})

app.use(bodyParser.urlencoded({extended:false}));
app.use(bodyParser.json());



app.use(cors({
    origin:'http://localhost:3000',
    method:['GET','POST']
}));

app.use('/api',ApiRoutes);
app.listen(PORT,()=>{
    console.log('Server is listening on port: '+PORT);
})