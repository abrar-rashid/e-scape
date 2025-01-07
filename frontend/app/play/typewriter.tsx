"use client";
import React, { useEffect, useState } from 'react';

type TypewriterTextProps = {
  text: string;
  typingSpeed?: number;
  cursorBlinkSpeed?: number;
};

const TypewriterText: React.FC<TypewriterTextProps> = ({ text, typingSpeed = 30, cursorBlinkSpeed = 500}) => {
  const [displayText, setDisplayText] = useState('');
  const [currentIndex, setCurrentIndex] = useState(0);
  const [showCursor, setShowCursor] = useState(true);
  const textArray = text.split('').map((char) => (char === '\\n' ? '\n' : char));

  useEffect(() => {
    console.log(textArray)
    if (currentIndex < textArray.length) {
      const timeout = setTimeout(() => {
        setDisplayText((prevText) => prevText + textArray[currentIndex]);
        setCurrentIndex((prevIndex) => prevIndex + 1);
      }, typingSpeed);

      return () => clearTimeout(timeout);
    }
  }, [currentIndex, textArray, typingSpeed]);



  return (
    <div>
      <span id="typewriter-text" className="text-[1.4rem] whitespace-pre-wrap text-[#424242]">{displayText}</span>
      {currentIndex < text.length && showCursor && <span className="cursor" />}
    </div>
  );
};

export default TypewriterText;