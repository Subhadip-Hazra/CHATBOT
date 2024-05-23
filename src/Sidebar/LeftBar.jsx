import React from 'react'
import { MdOutlinePowerSettingsNew, MdSettings } from "react-icons/md";
import { FaHistory } from "react-icons/fa";


const LeftBar = () => {
    return (
        <div>
            <div className='w-20 h-screen fixed border hidden sm:block'>
            <div className='flex justify-center mt-20'>
                    <FaHistory className='w-6 h-7' />
                </div>
                <div className='flex justify-center relative mt-16 top-1/2'>
                    <MdSettings className='w-10 h-7' />
                </div>
                <div className='flex justify-center relative mt-10 top-1/2'>
                    <MdOutlinePowerSettingsNew className='w-10 h-7' />

                </div>

            </div>

        </div>
    )
}
export default LeftBar