import React from 'react'

const Footer = () => {
  return (
    <div className="h-16 flex items-center justify-center">
      <p className="text-center">Copyright &copy; {new Date().getFullYear()}</p>
    </div>
  )
}

export default Footer
