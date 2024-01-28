import React from 'react'
import Headers from '../header/Headers'
import HealthForm from '../HealthForm/HealthForm'

const Home = () => {
  return (
    <div>
      <Headers/>
      
      <div className='mx-auto w-max mt-10 text-2xl  font-semibold '>Check Your Sleep Health</div>
      <HealthForm/>
      

    </div>
  )
}

export default Home
