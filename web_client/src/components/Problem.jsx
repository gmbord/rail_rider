import React from 'react'

import PROBLEM from "../ontrack-images/problem.png"
import DIRTYBOY from "../ontrack-images/dirty.png"
import "../styles/problem.css"

export default function Problem() {
  return (
    <>
    <div className="divided-section">
        <div className="divided-left">
            <h1><a>4,500,000</a></h1>
            <h2>Passenger hours of railway delay each year are caused by {' '}
                <a>black precipitate.</a>
            </h2>
            <img src={DIRTYBOY} alt="dirty track" />
        </div>
        <div className="divided-right">
            <img src={PROBLEM} alt="problem" />
            <h1><a>$316M</a></h1>
            <h2>Of revenue lost due to delays <a>per year.</a></h2>
        </div>
    </div>
    </>
  )
}
