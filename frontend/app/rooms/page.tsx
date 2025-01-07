"use client";
import axios from "axios";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import '../KeyCursor.css';
import LoadingSpinner from "../components/LoadingSpinner";
axios.defaults.withCredentials = true

const Rooms: React.FC = () => {
  const router = useRouter();
  const [roomIds, setRoomIds] = useState<string[]>([]);
  const [roomNames, setRoomNames] = useState<string[]>([]);
  const [publicRoomIds, setPublicRoomIds] = useState<string[]>([]);
  const [publicRoomNames, setPublicRoomNames] = useState<string[]>([]);
  const [deleted, setDeleted] = useState(false);
  const [loggedIn, setLoggedIn] = useState(true);
  const [loading, setLoading] = useState(false);
  const [keyPosition, setKeyPosition] = useState({ x: 0, y: 0 });
  const [backgrounds, setBackgrounds] = useState<{ [roomId: string]: string }>({});

  useEffect(() => {
    const fetchMyRooms = async () => {
      const rooms = await myRooms();
      if (rooms == null) {
        setLoggedIn(false);
      } else {
        setRoomIds(rooms.map((room: { _id: string; }) => room._id))
        setRoomNames(rooms.map((room: { name: string; }) => room.name))
        // Fetch backgrounds for each room theme
        const backgroundsData: { [key: string]: string } = {};
        for (const room of rooms) {
          const response = await fetch(`http://146.169.43.38:8080/api/background-image/${room.theme}`);
          const data = await response.json();
          backgroundsData[room._id] = data.url; // Assuming the response contains a URL for the background image
        }
        setBackgrounds(backgroundsData);
        console.log(backgroundsData)
      }
    }

    fetchMyRooms()

    if (deleted) {
      setDeleted(false)
    }
  }, [deleted, loggedIn]);


  useEffect(() => {
    const fetchPublicRooms = async () => {
      const rooms = await publicRooms();
      if (rooms == null) {
        setLoggedIn(false);
      } else {
        setPublicRoomIds(rooms.map((room: { _id: string; }) => room._id))
        setPublicRoomNames(rooms.map((room: { name: string; }) => room.name))
        // Fetch backgrounds for each room theme
        const backgroundsData: { [key: string]: string } = {};
        for (const room of rooms) {
          const response = await fetch(`http://146.169.43.38:8080/api/background-image/${room.theme}`);
          const data = await response.json();
          backgroundsData[room._id] = data.url; // Assuming the response contains a URL for the background image
        }
        setBackgrounds(backgroundsData);
        console.log(backgroundsData)

      }
    }

    fetchPublicRooms()

    if (deleted) {
      setDeleted(false)
    }
  }, [deleted, loggedIn]);




  // useEffect(() => {
  //   // Reset cursor style to default behavior
  //   document.body.style.cursor = 'auto';

  //   return () => {
  //     document.body.style.cursor = 'auto';
  //   };
  // }, []);

  useEffect(() => {
    const handleMouseMove = (event: { pageX: number; pageY: number }) => {
      setKeyPosition({ x: event.pageX - 15, y: event.pageY - 15 });
    };

    document.addEventListener('mousemove', handleMouseMove);

    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
    };
  }, []);

  const myRooms = async () => {
    try {
      const response = await axios.get(
        "http://146.169.43.38:8080/api/my-rooms"
      );
      return response.data.rooms
    } catch (error) {
      console.error('Error retrieving rooms:', error);

    }
  }


  const publicRooms = async () => {
    try {
      const response = await axios.get(
        "http://146.169.43.38:8080/api/public-rooms"
      );
      return response.data.rooms
    } catch (error) {
      console.error('Error retrieving rooms:', error);

    }
  }


  const getPDFPath = async (id: string) => {
    setLoading(true)
    try {
      const response = `http://146.169.43.38:8080/api/get-pdf/${id}`
      window.open(response, '_blank');
    } catch (error) {
      console.error('Error retrieving pdf:', error);
    }
    setLoading(false)
  }

  const deleteRoom = async (id: string) => {
    setLoading(true)
    try {
      const response = await axios.post(
        `http://146.169.43.38:8080/api/delete-room/${id}`
      );
      setDeleted(true)
    } catch (error) {
      console.error("Error deleting room:", error);
    }
    setLoading(false)
  };

  const editRoom = async (id: string) => {
    setLoading(true)

    try {
      const response = await axios.post(
        `http://146.169.43.38:8080/api/edit-room/${id}`
      );
      resetCursorStyle()
      router.push('/edit');
    } catch (error) {
      console.error("Error playing room:", error);
    }
    setLoading(false)

  };

  const playRoom = async (id: string) => {
    setLoading(true)

    try {
      const response = await axios.post(
        `http://146.169.43.38:8080/api/play-room/${id}`
      );
      resetCursorStyle()
      router.push('/play');
    } catch (error) {
      console.error("Error playing room:", error);
    }
    setLoading(false)

  };

  function resetCursorStyle() {
    // Reset cursor style to default behavior
    document.body.style.cursor = 'auto';

    // Cleanup function to revert cursor style when component unmounts
    return () => {
      document.body.style.cursor = 'auto';
    };
  }



  if (!loggedIn) {
    return <div className="flex flex-col justify-center items-center h-screen">Not logged in</div>
  }


  return (
    <div className="bg-[#FFFFF0] text-[#424242] min-h-screen">

      <div className="container mx-auto">
        <a href="/rooms">
          <img
            src="e-scape-logo.svg"
            alt="logo"
            style={{ width: "250px", height: "auto", position: "relative", top: 60, left: 0}}
          />
        </a>

        {/* Logout */}
        <div className=" text-l text-right mb-8">
          <a
            href="/"
            className="bg-[#424242] hover:bg-blue-600 text-white font-bold py-2 px-4 rounded"
          >
            Log out
          </a>
        </div>
        {/* Title */}
        <h1 className="text-4xl font-bold mb-8 mt-8">My Rooms</h1>

        {/* Create New Room button */}
        <div className=" text-xl text-right mb-8">
          <a
            href="generate"
            className="bg-[#424242] hover:bg-blue-600 text-white font-bold py-2 px-4 rounded"
          >
            Create New Room
          </a>
        </div>

        {loading && <LoadingSpinner />}

        {roomIds.length > 0 ? (
          roomIds.map((roomId, index) => (
            <div key={roomId} className="border-2 border-[#424242] rounded-lg p-4 mb-8 relative flex justify-between items-center" style={{ background: `url(${backgrounds[roomId]})`, backgroundPosition: 'center'}}>
              <p className="bg-[#424242] text-white rounded py-2 px-4 font-semibold mb-0">Room {index + 1}: {roomNames[index]}</p>
              <div>
                <button
                  onClick={() => deleteRoom(roomId)}
                  className="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded mr-2"
                >
                  Delete
                </button>

                <button
                  onClick={() => editRoom(roomId)}
                  className="bg-[#424242] hover:bg-blue-600 text-white font-bold py-2 px-4 rounded mr-2"
                  rel="noopener noreferrer"
                >
                  Edit
                </button>

                <button
                  onClick={() => getPDFPath(roomId)}
                  className="bg-[#424242] hover:bg-blue-600 text-white font-bold py-2 px-4 rounded mr-2"
                  rel="noopener noreferrer"
                >
                  Download
                </button>

                <button
                  onClick={() => playRoom(roomId)}
                  className="bg-[#424242] hover:bg-blue-600 text-white font-bold py-2 px-4 rounded "
                >
                  Play
                </button>
              </div>
            </div>
          ))
        ) : (
          <div className="border-2 border-white rounded-lg p-4 items-center" >
            <p className="text-center text-2xl">No rooms</p>
          </div>
        )}

        <h1 className="text-4xl font-bold mb-8 mt-24">Public Rooms</h1>

        <div>
          {publicRoomIds.length > 0 ? (
            publicRoomIds.map((roomId, index) => (
              <div key={roomId} className="border-2 border-[#424242] rounded-lg p-4 mb-8 relative flex justify-between items-center" style={{ background: `url(${backgrounds[roomId]})`, backgroundPosition: 'center' }}>
                <div className="rounded bg-[#424242] text-white py-2 px-4 font-semibold mb-0">Room {index + 1}: {publicRoomNames[index]}</div>
                <div>
                  <button
                    onClick={() => playRoom(roomId)}
                    className="bg-[#424242] hover:bg-blue-600 text-white font-bold py-2 px-4 rounded "
                  >
                    Play
                  </button>
                </div>
              </div>
            ))
          ) : (
            <div className="border-2 border-white rounded-lg p-4 items-center" >
              <p className="text-center text-2xl">No public rooms</p>
            </div>
          )}


        </div>


      </div>
      <div className="key" style={{ left: keyPosition.x, top: keyPosition.y }}></div>
    </div>
  );


};

export default Rooms;