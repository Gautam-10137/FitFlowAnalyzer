const express=require('express');
const router=express.Router();
const AuthController=require('../controllers/AuthController');

// handling register route
router.post('/register',AuthController.register);

// handling login route
router.post('/login',AuthController.login)

module.exports=router;
