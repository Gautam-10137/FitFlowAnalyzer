const express=require('express');
const router=express.Router();
const AuthRoutes=require('./authRoutes');

router.use('/auth',AuthRoutes);

module.exports=router;