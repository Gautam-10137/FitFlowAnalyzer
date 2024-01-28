import React, { useState } from 'react'

const DialogBox = (props) => {
   

    const closeDialog=()=>{
        props.setShowResult(false);
    }
  return (
    <div>
      
       
       
            <div className='w-1/3 mx-auto bg-slate-100 mt-10 mb-10 shadow-lg rounded-md  '>

                <div className=' flex justify-between  '>
                    <div className='text-xl'>Status:</div> 
                    <button onClick={closeDialog}> &times; </button>
                </div>
            <div className='text-xl font-semibold text-center'>
                {
                    props.title==='Insomnia'?<a className='hover:bg-slate-200 hover:rounded-md hover:shadow-lg' href="https://my.clevelandclinic.org/health/diseases/12119-insomnia" target="_blank" rel="noopener noreferrer"> Insomnia</a>
                    :props.title==='Sleep Apnea'?<a className='hover:bg-slate-200 hover:rounded-md hover:shadow-lg' href="https://my.clevelandclinic.org/health/diseases/8718-sleep-apnea" target='_blank' rel="noopener noreferrer">Sleep Apnea</a>:'No Sleep Disorder'

                }
                
            </div>
            </div>
        
       
    </div>
  )
}

export default DialogBox
