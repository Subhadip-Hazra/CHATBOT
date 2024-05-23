import React from 'react'

const Grittings = () => {
    return (
        <div>
            <div className="flex justify-center mt-36 -space-x-2 overflow-hidden gap-5">
                <img
                    title="default photo url"
                    className="inline-block h-16 w-16 rounded-full ring-2 ring-white"
                    src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                    alt="Default user profile"
                />
            </div>
            <div className='flex justify-center px-10'>
            <p className='text-xl font-mono mt-14 text-center font-bold'>How can I assist you Today ? </p> 

            </div>
        </div>
    )
}

export default Grittings
