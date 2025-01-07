"use client"
import axios from "axios";
import { useRouter } from "next/navigation"
import { useEffect, useState } from "react";
axios.defaults.withCredentials = true

export default async function RoomId({params}: any) {
    const router = useRouter();
    const [error, setError] = useState(false)
    useEffect(() => {
      const playRoom = async (id: string) => {    
        try {
          const response = await axios.post(
            `http://146.169.43.38:8080/api/play-room/${id}`
          );
          router.push('/play');
          setError(false)
        } catch (error) {
          console.error("Error playing room:", error);
          setError(true)
        }
    
      };
      playRoom(params.room_id);
    }, [error]);
    

    return (
      <div>
        {!error && 
       ( <div>
            Going to playing website...
        </div>)
        }
        {error && 
        (<div>
          Invalid room id.
        </div>)
        }
      </div>
      )
    
}