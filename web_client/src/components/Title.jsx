import React from 'react'

import LOGO from "../ontrack-images/ontrack.png"
import LITTLEBUDDY from "../ontrack-images/TRAIN.png"
import "../styles/title.css"

export default function Title() {
  return (
    <div className="title-wrapper">
        <div className="revealing-title">
            <img className="little-buddy" src={LITTLEBUDDY} alt="buddy" />
        </div>
        <img className="title-image" src={LOGO} alt="On track logo" />
    </div>
  )
}
