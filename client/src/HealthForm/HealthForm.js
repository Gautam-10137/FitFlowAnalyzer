import React, { useState } from 'react';
import axios from 'axios';
import DialogBox from '../dialogBox/DialogBox';
const HealthForm = () => {
   const [user,setUser]=useState({
    Gender:'',
    Age:0,
    Occupation:'',
    Sleep_Duration:'',
    Quality_of_Sleep:0,
    Physical_Activity_Level:0,
    Stress_Level:0,
    BMI_Category:'',
    Blood_Pressure:'127/80',
    Heart_Rate:70,
    Daily_Steps:0
   })

   const [title,setTitle]=useState('');
   const [showResult,setShowResult]=useState(false);

   const occupationCategory=['Software Engineer', 'Doctor', 'Sales Representative', 'Teacher',
   'Nurse', 'Engineer', 'Accountant', 'Scientist', 'Lawyer',
   'Salesperson', 'Manager'];

   const handleInputChange=(e)=>{
    const {name,value}=e.target;

    setUser({
        ...user,
        [name]:value
    });
   }
   const scrollToBottom = (e) => {
    e.preventDefault();
    window.scrollTo({
      top: document.documentElement.scrollHeight,
      behavior: 'smooth' 
    });
  };
   const handleSubmit= async (e)=>{
        e.preventDefault();
        try{
            const formData=new FormData();
            for (const key in user){
                formData.append(key,user[key]);
            } 
            const response= await axios.post('http://127.0.0.1:5000/predict',formData);
            const disorder=response.data.sleep_disorder;
            if(disorder===0){
                setTitle('No Sleep Disorder');
            }
            else if(disorder===1){
                setTitle('Insomnia');
            }
            else{
                setTitle('Sleep Apnea');
            }
            setShowResult(true);
           
        }
        catch(error){
            console.error('error: ',error.message);
        }
   }
  return (
    <div className='w-1/2 mx-auto border-2 p-2 bg-green-100 mb-2 rounded-md shadow-lg'>
      <div className=' mx-auto text-lg  '>
        <form  >
            <div className='mb-4'>
                <label>Gender:</label>
                <select value={user.Gender} className='border-2 ' onChange={(e)=>setUser({...user,Gender:e.target.value})}>
                   <option value='' disabled>Select Gender</option>
                   <option value='Male'>Male</option>
                   <option value='Female'>Female</option>
                </select>
            </div>
            <div className='mb-4'>
                <label>Age:</label>
                <input
                   type='number'
                   name='Age'
                   value={user.Age}
                   onChange={(e)=>{handleInputChange(e)}}
                   className='border-2 '
                 >
                </input>
            </div>
            <div className='mb-4'>
                <label>Occupation:</label>
                <select value={user.Occupation} className='border-2 '  onChange={(e)=>setUser({...user,Occupation:e.target.value})}>
                    <option value='' disabled>Select Occupation</option>
                    {
                        occupationCategory.map((occupation,index)=>(
                             <option key={index} value={occupation}>{occupation}</option>
                        ))
                    }
                    
                </select>
            </div>
            <div className='mb-4'>
                <label>Sleep Duration(hours):</label>
                <input
                   type='text'
                   value={user.Sleep_Duration}
                   name='Sleep_Duration'
                   onChange={(e)=>handleInputChange(e)}
                   className='border-2'
                >
                </input>
            </div>
            <div className='mb-4'>
                <label>Quality of Sleep:</label>
                <select value={user.Quality_of_Sleep} className='border-2' onChange={(e)=>setUser({...user,Quality_of_Sleep:e.target.value})}>
                    <option value={0} disabled> Select</option>
                   { Array.from({length:10},(_,index)=>index+1).map((level,index)=>(
                          <option key={index} value={level}>{level} </option>
                   ))}
                </select>
            </div>
            <div className='mb-4'>
                <label>Physical Activity Level(minutes):</label>
                <input
                  type='number'
                  value={user.Physical_Activity_Level}
                  name='Physical_Activity_Level'
                  onChange={(e)=>handleInputChange(e)}
                  className='border-2'
                >     
                </input>
            </div>
            <div className='mb-4'>
                <label>Stress Level:</label>
                <select value={user.Stress_Level} className='border-2' onChange={(e)=>setUser({...user,Stress_Level:e.target.value})}>
                    <option value={0} disabled>Select</option>
                    {
                        Array.from({length:10},(_,index)=>index+1).map((level,index)=>(
                            <option key={index} value={level}> {level}</option>
                        ))
                    }
                </select>
            </div>
            <div className='mb-4'>
                <label>BMI Category:</label>
                <select value={user.BMI_Category} className='border-2' onChange={(e)=>setUser({...user,BMI_Category:e.target.value})}>
                    <option value='' disabled>Select</option>
                    <option value='Underweight'>Underweight</option>
                    <option value='Normal'>Normal</option>
                    <option value='Overweight'>Overweight</option>
                </select>
            </div>
            <div className='mb-4'>
                <label>Blood Pressure:</label>
                <input
                  type='number'
                  className='border-2'
                  value={user.Blood_Pressure.split('/')[0]}
                  onChange={(e)=>{
                    setUser({
                        ...user,
                        Blood_Pressure:e.target.value+'/'+user.Blood_Pressure.split('/')[1]
                    });
                  }}

                ></input>
                <span className=' text-xl'>/</span>
                <input
                  type='number'
                  className='border-2'
                  value={user.Blood_Pressure.split('/')[1]}
                  onChange={(e)=>{
                    setUser({
                        ...user,
                        Blood_Pressure:user.Blood_Pressure.split('/')[0] +'/'+e.target.value
                    });
                  }}
                >
                </input>
            </div>
            <div className='mb-4'>
                <label>Heart Rate:</label>
                <input
                   type='number'
                   name='Heart_Rate'
                   value={user.Heart_Rate}
                   onChange={(e)=>handleInputChange(e)}
                   className='border-2 '
                >
                </input>
            </div>
            <div className='mb-4'>
                <label>Daily Steps:</label>
                <input
                   type='number'
                   name='Daily_Steps'
                   value={user.Daily_Steps}
                   onChange={(e)=>handleInputChange(e)}
                   className='border-2 '
                >
                </input>
            </div>
            <button  className=' bg-white border-2 border-slate-400 hover:bg-slate-200  mx-20 w-32 rounded-md' onClick={(e)=>handleSubmit(e)}> Get Result</button>
            {showResult && <button className=' bg-white border-2 border-slate-400 hover:bg-slate-200 rounded-md w-32' onClick={(e)=>scrollToBottom(e)}>Show</button>}
        </form>
      </div>
      { 
         showResult && <DialogBox title={title} setShowResult={setShowResult}/>
      }
    </div>
  )
}

export default HealthForm
