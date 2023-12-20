import React, { useEffect, useState, useRef } from 'react'; // Include useRef here

import PROBLEM from "../ontrack-images/problem.png";
import DIRTYBOY from "../ontrack-images/dirty.png";
import "../styles/problem.css";

export default function Problem() {
  const [isVisible, setIsVisible] = useState(false);
  const problemRef = useRef();

  useEffect(() => {
    const observer = new IntersectionObserver(entries => {
      const [entry] = entries;
      setIsVisible(entry.isIntersecting);
    }, {
      threshold: 0.1 // Corrected comment: triggers when 1% of the target is visible
    });

    const currentRef = problemRef.current;
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
    <div ref={problemRef} className={isVisible ? "divided-section smooth-appear" : "divided-section force-transparent"}>
        <>
          <div className="divided-left">
            <h1><span>4,500,000</span></h1>
            <h2>Passenger hours of railway delay each year are caused by {' '}
                <span>black precipitate.</span>
            </h2>
            <img src={DIRTYBOY} alt="dirty track" />
          </div>
          <div className="divided-right">
            <img src={PROBLEM} alt="problem" />
            <h1><span>$316M</span></h1>
            <h2>Of revenue lost due to delays <span>per year.</span></h2>
          </div>
        </>
    </div>
  );
}
