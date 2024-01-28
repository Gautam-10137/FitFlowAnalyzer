import React from 'react'
import { Link } from 'react-router-dom'
const Headers = () => {
  return (
    <div>
      <nav className=' bg-slate-50 w-full h-10 text-xl text-center'>
        <div className=' text-2xl font-bold  bg-green-200 '>FitFlowAnalyzer</div>
        <div className=''>
               {/* About */}
        </div>
        {/* <div className='flex space-x-4 mx-2'>
            <div className=' bg-white'> <Link to="/login">Login</Link></div>
            <div><Link to="/register">Register</Link></div>
        </div> */}
        
      </nav>
    </div>
  )
}

export default Headers
