import React, { useState, useEffect, useRef } from 'react';
import '../styles/intro.css';
import ROBIT from '../ontrack-images/robit.png';
import CLEAN from '../ontrack-images/cleanyclean.png';

export default function Introduction() {
    const [isVisible, setIsVisible] = useState(false);
    const introRef = useRef();

    useEffect(() => {
        const observer = new IntersectionObserver(entries => {
            const [entry] = entries;
            setIsVisible(entry.isIntersecting);
        }, {
            threshold: 0.01 // Corrected comment: triggers when 1% of the target is visible
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
                <h1><span>Introducing OnTrack</span></h1>
                <img className="robit" src={ROBIT} alt="robit" />
                <h2>
                    This special little fella cleans approximately 
                    <span> 69%</span> of black precipitate off of railways while stinky, 
                    <span style={{ color: "limegreen" }}> stinky</span> 
                    <span role="img" aria-label="face with tongue">&#129326;</span> powerwashers only clean up to 
                    <span> -20%</span>
                </h2>
                <img className="cleany-boi" src={CLEAN} alt="clean boi"/>
            </>}
        </div>
    );
}
