import axios from 'axios'
axios.defaults.withCredentials = true
import { cookies } from "next/headers";

// Displays the page and calls the input page which runs on client and handles all logic 
//  - all APi calls should happen here so it is rendered server-side and is fed into client side pages
//  - square brackets used in [stage] allows dynamic linking to handle differing numbers of stages

export const getRoom = async (getTheme: number = 0) => {
    try {
        const response = await axios.get('http://146.169.43.38:8080/api/room-state', {
          headers: {
            'Cookie': cookies().toString(),
        }
        });
        const res = response.data
        if (getTheme == 1) {
            const response2 = await axios.get(`http://146.169.43.38:8080/api/background-image/${parseInt(res.theme)}`, {
              headers: {
                'Cookie': cookies().toString(),
            }
            });
            res['theme_url'] = response2.data.url;
        }
        return res
    } catch (error) {
        console.error('Error retrieving room data:', error);
    }
}

export const getPDF = async () => {
    try {
      const response = "http://146.169.43.38:8080/api/get-playing-game-pdf"
      return response
    } catch (error) {
      console.error("Error generating PDF:", error);
    }
  };