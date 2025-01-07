"use client";

import React, { useEffect, useState } from 'react';
import Link from '@/node_modules/next/link';
import { useRouter } from 'next/navigation';
export const dynamic = 'auto', dynamicParams = true, revalidate = 0


// Displays the user interface things like inputs and links logic happens here
//  - client side so useEffect and useState can be used

// Variables passed in from [stage]/page.tsx that can be used here
interface StageProps {
  currentStage: number;
  puzzleSols: string[];
}


const InputPage: React.FC<StageProps> = ({currentStage, puzzleSols}) => {
  // useState are state variables that can be accessed by other components
  const introStage = 0;
  const router = useRouter();
  const timeInSeconds = 300;

  const [userInput, setUserInput] = useState('');
  const [colour, setColour] = useState('#000');
  const [nextStage, setNextStage] = useState('');
  const [showContinue, setShowContinue] = useState(false);
  const [timer, setTimer] = useState(timeInSeconds)
  const [inputAnimation, setInputAnimation] = useState('')
  // useEffect allows something to happen as soon as page loads before anything else is done e.g. setting hyperlinks
  useEffect(() => {
    if (+currentStage === introStage) {  // Show continue if it is intro 
      setShowContinue(true)
    }

    if (+currentStage === puzzleSols.length){ // On final puzzle set link to finish page
      setNextStage(`/play/finish`)
    }
    else{ // else link to next puzzle stage
      setNextStage(`/play/${+currentStage + +1}`)
    }
    // Timer to countdown 'timer' seconds
    if (showContinue) return;
    const interval = setInterval(() => {
      setTimer(prevTimeLeft => {
        if (prevTimeLeft === 0) { // Redirect to failure page when timer runs out
          clearInterval(interval)
          router.push('/play/fail')
          return 0
        } else {
          return prevTimeLeft - 1
        }
      })
    }, 1000)
    return () => clearInterval(interval)
  }, [showContinue]);
  
  const minutes = Math.floor(timer / 60);
  const seconds = timer % 60;

  const handleSubmit = async () => {
    if ((userInput) === (puzzleSols[currentStage-1])) { // turns input green and converts submit button to next button
      setColour('#006600')
      setInputAnimation('fadeIn 1s ease-in')
      setShowContinue(true)
    } else { // turns input red for a couple of seconds and then clears the input
      setInputAnimation('shake 0.2s ease-in-out 0s 2')
      setColour('#C80B0B')
      setTimeout(() => {
        setUserInput('');
        setInputAnimation('');
        setColour('#000')
      }, 1000);
    }
  };

  const isIntro = +currentStage === 0;  // Used when deciding later whether to show the submit textbox and/or the coninue button
  return (
    <div className="py-1 sticky bottom-0 fade">
      {!isIntro && (
        <div>
          {
          !showContinue &&
          <div>
            <div className="timer-bar">
              <div className="bar" style={{
                animation: `animate-bar ${timeInSeconds}s ease-in`,
              }}>
              </div>
            </div>
            <div className="timer-text font-bold"
                style={{
                  animation: `time-colour ${timeInSeconds}s ${timer < 10 ? ', blink 0.5s infinite' : ''}`,
                }}>
              TIME LEFT: {minutes.toString().padStart(2, '0')}:{seconds.toString().padStart(2, '0')}
            </div>
          </div>
          }
          <div>
            <input
              className='input-style w-[60vw] h-[5rem]'
              style={{
                color: colour,
                animation: inputAnimation,
              }}
              value={userInput}
              onChange={(event) => setUserInput(event.target.value)}
              maxLength={6}
              pattern="[0-9]{6}"
              placeholder=" ______"
              onKeyDown={(event) => {
                if (event.key === 'Enter') {
                  handleSubmit();
                }
              }}
            />
          </div>
          {!isIntro && !showContinue && ( // Only render the submit button if it's not the intro and showContinue is false
            <button
              style={{
                padding: '10px 20px',
                fontSize: '16px',
                color: '#000',
                marginRight: '10px',
                cursor: 'pointer',
                backgroundColor: 'transparent',
                fontWeight: 'bold',
              }}
              onClick={handleSubmit}
            >
              SUBMIT
            </button>
          )}
        </div>
      )}
      {(isIntro || showContinue) && (
        <div>
          <a className="text-[#FF0000] hover:text-[#C80B0B]"
            href={nextStage}
            style={{
              padding: '10px 20px',
              fontSize: '5vh',
              borderRadius: '0',
              cursor: 'pointer',
              fontWeight: 'bold',
              animation: 'fadeIn 5s ease-in',
            }}
          >
            CONTINUE
          </a>
        </div>
      )}
    </div>
  );
};

export default InputPage;
