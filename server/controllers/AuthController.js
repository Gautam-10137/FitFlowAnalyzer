const User=require('../models/User');
const bcrypt=require('bcryptjs');
const jwt=require('jsonwebtoken');
const Config=require('../Config');

const register=(req,res)=>{
    try{
         const {username,email,password}=req.body;

         const newUser=new User({username,email,password});
         bcrypt.genSalt(10,(err,salt)=>{
            bcrypt.hash(newUser.password,salt,(err,hashed)=>{
                newUser.password=hashed;

                newUser
                    .save()
                    .then()
                    .catch(err=>console.error(err));
            })
         })
         res.status(200).json(newUser);

    }
    catch(error){
        res.status(500).json({message:"Registration Failed",error:error.message});
    }
}

const login=(req,res)=>{
    try{
         const {username,email,password}=req.body;

         User.findOne({username}).then((user)=>{
            if(!user) return res.status(400).json({message:"User not found!"});

            bcrypt.compare(password,user.password,(err,isMatch)=>{
                if(!isMatch) return res.status(400).json({message:'Password Incorrect'});
                const payload={id:user.id,username:user.username};
                const token=jwt.sign(payload,Config.secret,{'expiresIn':'1h'});
                return res.status(200).json({token:`Bearer ${token}`});
            });
           
         });
    }
    catch(error){
        res.status(500).json({message:'Login Failed',error:error.message});
    }
}

module.exports={register,login};