import React, { useState, useEffect, useRef } from 'react';
import '../styles/intro.css';
import ROBIT from '../ontrack-images/robit.png';
import CLEAN from '../ontrack-images/cleanyclean.png';

export default function Introduction() {
    const [isVisible, setIsVisible] = useState(false);
    const introRef = useRef();

    useEffect(() => {
        const observer = new IntersectionObserver(entries => {
            // Get the first entry
            const [entry] = entries;
            // Update state based on visibility
            setIsVisible(entry.isIntersecting);
        }, {
            threshold: .01 // The callback will trigger only when 100% of the target is visible
        });

        const currentRef = introRef.current;
        if (currentRef) {
            observer.observe(currentRef);
        }

        return () => {
            if (currentRef) {
                observer.disconnect();
            }
        };
    }, []);

    return (
        <div className="intro-wrapper" ref={introRef}>
            { isVisible &&
            <>
            <h1><a>Introducing OnTrack</a></h1>
            <img className="robit" src={ROBIT} alt="robit" />
            <h2>This special little fella cleans approximately <a>69%</a> of black precipitate off of railways while stinky, <a style={{"color": "limegreen"}}>stinky</a> 	&#129326; powerwashers only clean up to <a>-20%</a> </h2>
            <img className="cleany-boi" src={CLEAN} alt="clean boi"/>
            </>}
        </div>
    );
}
