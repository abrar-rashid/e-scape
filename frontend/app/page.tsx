"use client";
import React, { useEffect, useRef, useState } from 'react';
import axios from "axios";
import { useRouter } from 'next/navigation';
import './KeyCursor.css';
import LoadingSpinner from "./components/LoadingSpinner";
import { FaEye, FaEyeSlash } from 'react-icons/fa';

axios.defaults.withCredentials = true

const LoginPage: React.FC = () => {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [creatorId, setCreatorId] = useState('')
  const [loggedIn, setLoggedIn] = useState('Not Logged In')
  const [isLoggedIn, setIsLoggedIn] = useState(false)
  const [loginFailed, setLoginFailed] = useState(false)
  const [hasSignedUp, setHasSignedUp] = useState(false)
  const router = useRouter();
  const [keyPosition, setKeyPosition] = useState({ x: 0, y: 0 });
  const [loading, setLoading] = useState(false)
  const [loadingSignUp, setLoadingSignUp] = useState(false)
  const [passwordError, setPasswordError] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [buttonColor, setButtonColor] = useState('bg-blue-400');
  const [buttonText, setButtonText] = useState('Sign Up');

  const passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]*$/;

  const login = async () => {
    setLoading(true)
    try {
      const response = await axios.post(
        "http://146.169.43.38:8080/api/login",
        {
          email: email,
          password: password,
        }
      );
      setCreatorId(response.data.creator_id)
      setLoggedIn('Successfully Logged In')
      setIsLoggedIn(true)
      setLoginFailed(false)
      setHasSignedUp(false)

    } catch (error) {
      setLoginFailed(true)
      console.error('Error retrieving login:', error);
    }
    setLoading(false)
  }

  const signUp = async () => {
    setLoadingSignUp(true);
    try {
      // Password validation
      // if (!passwordRegex.test(password)) {
      //   setPasswordError('Password must contain at least 8 characters, including at least one number, one uppercase and one lowercase letter.');
      //   throw new Error('Invalid password');
      // }

      const response = await axios.post(
        "http://146.169.43.38:8080/api/sign-up",
        {
          email: email,
          password: password,
        }
      );
      setCreatorId(response.data.creator_id);
      setLoggedIn('Successfully Logged In');
      setHasSignedUp(true);
      setLoginFailed(false);
      setPasswordError(''); // Reset password error if sign-up is successful
    } catch (error) {
      console.error('Error signing up:', error);
    }
    setLoadingSignUp(false);
  }

  const togglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  useEffect(() => {
    if (email && password) {
      setButtonColor('bg-green-500');
      setButtonText('Sign Up');
    }
    // else if (email && password) {
    //   setButtonColor('bg-blue-500')
    // }
    else {
      setButtonColor('bg-blue-400');
      setButtonText('Sign Up');
    }
  }, [email, password, passwordRegex]);

  useEffect(() => {
    const handleMouseMove = (event: { clientX: number; clientY: number; }) => {
      setKeyPosition({ x: event.clientX - 15, y: event.clientY - 15 });
    };

    document.addEventListener('mousemove', handleMouseMove);

    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
    };
  }, []);


  useEffect(() => {
    if (isLoggedIn || hasSignedUp) {
      router.push('/rooms');
    }
  }, [isLoggedIn, hasSignedUp]);


  return (
    <div className="flex flex-col items-center text-[#424242] justify-center pb-40 min-h-screen bg-[#FFFFE5] onMouseMove={handleMouseMove}">
      <div className="title-box rounded-md font-bold text-2xl p-2 mt-10">
        <div>
          <img src="e-scape-logo.svg"
            alt="logo"
            style={{ width: "350px", height: "auto" }}
          />
        </div>
      </div>
      <div className="p-8 rounded-lg shadow-md border-4 border-[#424242] mt-5">
        <h3 className="text-xl font-semibold mb-4">Login or Sign Up</h3>
        <div className="mb-4">
          <input
            type="email"
            placeholder="Username or email"
            className="w-full text-black px-4 py-2 rounded-lg border border-[#424242] focus:outline-none focus:border-blue-500"
            onChange={(event) => setEmail(event.target.value)}
            value={email}
          />
        </div>



        <div className="relative">
          <input
            type={showPassword ? 'text' : 'password'}
            placeholder="Password"
            className="w-full text-black px-4 py-2 mb-4 rounded-lg border border-[#424242] focus:outline-none focus:border-blue-500 pr-10"
            onChange={(event) => setPassword(event.target.value)}
            value={password}
          />
          <div className="absolute inset-y-3.5 right-0 items-center pr-3">
            {showPassword ? (
              <FaEyeSlash
                className="text-gray-500 cursor-pointer"
                onClick={togglePasswordVisibility}
              />
            ) : (
              <FaEye
                className="text-gray-500 cursor-pointer"
                onClick={togglePasswordVisibility}
              />
            )}
          </div>
        </div>


        <div
          className='items-center text-white'>
          <button
            type="submit"
            className={`w-full py-2 rounded-lg transition duration-300 ${email && password
              ? "bg-[#424242] text-white hover:bg-blue-600"
              : "bg-[#424242] cursor-not-allowed"
              }`}
            onClick={login}
            disabled={!email || !password || loading}
          >
            {loading ? "Logging In..." : "Log In"}
          </button>

          <div>
            <button
              type="submit"
              className={`w-full py-2 mt-4 rounded-lg transition duration-300 ${buttonColor} text-white`}
              onClick={signUp}
              disabled={!email || !password || loading}
            >
              {loadingSignUp ? "Signing Up..." : buttonText}
            </button>
          </div>

          {loading && <LoadingSpinner />}
        </div>


        {isLoggedIn && (
          <div className="text-green-500 mt-4">Logged in successfully!</div>
        )}

        {loginFailed && (
          <div className="text-red-400 mt-4">Incorrect username or password!</div>
        )}

        {passwordError && (
          <div className="text-red-400 mt-4 w-60 flex items-center justify-center mx-auto">{passwordError}</div>
        )}

        {hasSignedUp && (
          <div className="text-green-500 mt-4">Signed up successfully!</div>
        )}

      </div>
      <div className="key" style={{ left: keyPosition.x, top: keyPosition.y }}></div>
    </div>
  );


};

export default LoginPage;