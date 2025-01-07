"use client";

import { useState, useEffect } from "react";
import axios from "axios";
import LoadingSpinner from "../components/LoadingSpinner";
import QuantityBox from "../components/QuantityBox";
import TagInput from "../components/TagInput";
axios.defaults.withCredentials = true

const GeneratorPage: React.FC = () => {
  const [roomName, setRoomName] = useState<string>("");
  const [theme, setTheme] = useState<number>(0);
  const [themes, setThemes] = useState<{ enum: number; name: string }[]>([]);
  const [keywords, setKeywords] = useState<string[]>([]);
  const [difficulty, setDifficulty] = useState<number>(0);
  const [length, setLength] = useState<number>(1);
  const [whitelist, setWhitelist] = useState<number[]>([]);
  const [blacklist, setBlacklist] = useState<number[]>([]);
  const [downloadUrl, setDownloadUrl] = useState<string>("");
  const [loading, setLoading] = useState(false);
  const [selectedWhitelistPuzzle, setSelectedWhitelistPuzzle] =
    useState<number>(0);
  const [selectedBlacklistPuzzle, setSelectedBlacklistPuzzle] =
    useState<number>(0);
  const [puzzleTypes, setPuzzleTypes] = useState<
    { enum: number; name: string }[]
  >([]);
  const [generated, setGenerated] = useState<boolean>(false);
  const [backgroundImage, setBackgroundImage] = useState<string>(
    "images/generator_bg.png"
  );
  const [isPublic, setIsPublic] = useState<boolean>(false);

  const generate = async () => {
    setLoading(true);

    // Fetch background image path based on selected theme
    const response = await axios.get(
      `http://146.169.43.38:8080/api/background-image/${theme}`
    );
    setBackgroundImage(response.data.url);

    try {
      const response = await axios.post(
        "http://146.169.43.38:8080/api/generate-room",
        {
          roomName: roomName,
          theme: theme,
          keywords: keywords,
          difficulty: difficulty,
          length: length,
          whitelist: whitelist,
          blacklist: blacklist,
          isPublic: isPublic
        }
      );
      setDownloadUrl(`http://146.169.43.38:8080/api/get-pdf/${response.data.id}`);
      setGenerated(true);
    } catch (error) {
      console.error("Error generating PDF:", error);
    }
    setLoading(false);
  };

  const handleToggle = () => {
    setIsPublic(!isPublic);
  }

  useEffect(() => {
    const fetchThemes = async () => {
      try {
        const response = await axios.get("http://146.169.43.38:8080/api/themes");
        const types: { enum: number; name: string }[] = response.data.names.map(
          (name: string, index: number) => ({
            enum: index + 1,
            name: name,
          })
        );
        setThemes(types);
      } catch (error) {
        console.error("Error fetching themes:", error);
      }
    };

    fetchThemes();
  }, []);

  useEffect(() => {
    const fetchPuzzleTypes = async () => {
      try {
        const response = await axios.get(
          "http://146.169.43.38:8080/api/puzzle-types"
        );
        const types: { enum: number; name: string }[] = response.data.names.map(
          (name: string, index: number) => ({
            enum: index + 1,
            name: name,
          })
        );
        setPuzzleTypes(types);
      } catch (error) {
        console.error("Error fetching puzzle types:", error);
      }
    };

    fetchPuzzleTypes();
  }, []);

  const handleAddPuzzleType = (type: number, listType: string) => {
    if (listType === "whitelist") {
      setWhitelist([...whitelist, type]);
    } else {
      setBlacklist([...blacklist, type]);
    }
  };

  const handleRemovePuzzleType = (type: number, listType: string) => {
    if (listType === "whitelist") {
      setWhitelist(whitelist.filter((puzzle) => puzzle !== type));
    } else {
      setBlacklist(blacklist.filter((puzzle) => puzzle !== type));
    }
  };

  const handleWhitelistChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setSelectedWhitelistPuzzle(parseInt(e.target.value));
    setWhitelist((prevWhitelist) =>
      prevWhitelist.filter((puzzle) => puzzle !== parseInt(e.target.value))
    );
  };

  const handleBlacklistChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setSelectedBlacklistPuzzle(parseInt(e.target.value));
    setBlacklist((prevBlacklist) =>
      prevBlacklist.filter((puzzle) => puzzle !== parseInt(e.target.value))
    );
  };

  useEffect(() => {
    if (selectedWhitelistPuzzle) {
      handleAddPuzzleType(selectedWhitelistPuzzle, "whitelist");
      setSelectedWhitelistPuzzle(0);
    }
  }, [selectedWhitelistPuzzle]);

  useEffect(() => {
    if (selectedBlacklistPuzzle) {
      handleAddPuzzleType(selectedBlacklistPuzzle, "blacklist");
      setSelectedBlacklistPuzzle(0);
    }
  }, [selectedBlacklistPuzzle]);

  return (
    <div
      className="flex space-x-4 flex-col justify-top items-center h-screen text-[#424242]"
      style={{
        backgroundImage: `url(${backgroundImage})`,
        backgroundSize: "cover",
        backgroundPosition: "center",
        transition: "background-image 3s ease-in-out", // Smooth transition
        cursor: 'auto',
        zIndex: '-5',
        position: 'fixed',
        inset: '0',
        overflowY: 'auto',
      }}
      >


      <div className="flex space-x-4 flex-col items-center justify-center">
        <a href="/rooms" className="mt-10">
          <img
            src="e-scape-logo.svg"
            alt="logo"
            style={{ width: "250px", height: "auto"}}
          />
        </a>
        <header className="text-7xl font-bold text-center mt-5 mb-20 font-mono text-[#424242]">
          Create Your Escape Room
        </header>

        <div>

          <div className="mb-5">
            <input
              type="text"
              id="roomName"
              value={roomName}
              onChange={(e) => setRoomName(e.target.value)}
              className="border border-gray-300 rounded-md text-center px-3 py-2 w-80 text-[#424242] placeholder-gray-400"
              placeholder="Enter room name"
            />
          </div>

          <select
            value={theme}
            onChange={(e) => setTheme(parseInt(e.target.value))}
            className="border border-gray-300 text-center rounded-md px-3 py-2 mb-4 w-80 text-[#424242]"
          >
            <option value={0}>Select Theme</option>
            {themes.map((t) => (
              <option key={t.enum} value={t.enum}>
                {t.name}
              </option>
            ))}
          </select>

          <TagInput tags={keywords} onChange={setKeywords} />

          <select
            value={difficulty}
            onChange={(e) => setDifficulty(parseInt(e.target.value))}
            className="border border-gray-300 text-center rounded-md px-3 py-2 mb-4 w-80 text-[#424242]"
          >
            <option value={0}>Select Difficulty</option>
            <option value={1}>Kids</option>
            <option value={2}>Adults</option>
            <option value={3}>Experts</option>
          </select>

          {/* <Button onClick={() => {generate()}} variant="contained">Hello world</Button> */}

          <div>
            {/* Length input */}
            <label>Number of Puzzles:</label>
            <QuantityBox value={length} onChange={setLength} />
          </div>

          <div>
            {/* Whitelist dropdown */}
            <label>Add to Whitelist:</label>
            <select
              onChange={handleWhitelistChange}
              value={selectedWhitelistPuzzle}
              className="border border-gray-300 rounded-md text-center ml-4 mt-4 px-3 py-2 mb-4 w-50 text-[#424242]"
            >
              <option value="">Select Puzzle Type</option>
              {puzzleTypes
                .filter((puzzle) => !whitelist.includes(puzzle.enum) && !blacklist.includes(puzzle.enum))
                .map((puzzle) => (
                  <option key={puzzle.enum} value={puzzle.enum}>
                    {puzzle.name}
                  </option>
                ))}
            </select>

            {/* Whitelist container */}
            <div className="flex flex-col items-start">
              <label className="mb-2">Whitelist:</label>
              <div className="whitelist-container overflow-auto max-h-40 max-w-80">
                {whitelist.map((puzzleValue, index) => {
                  const puzzle = puzzleTypes.find(
                    (p) => p.enum === puzzleValue
                  );
                  if (!puzzle) return null; // Skip if puzzle is not found
                  return (
                    <div
                      key={index}
                      className="inline-block ml-2 mb-2 px-3 py-1 bg-white rounded text-[#424242]"
                    >
                      {puzzle.name}
                      <button
                        onClick={() =>
                          handleRemovePuzzleType(puzzleValue, "whitelist")
                        }
                        className="ml-1 text-xs text-gray-500"
                      >
                        X
                      </button>
                    </div>
                  );
                })}
              </div>
            </div>
          </div>

          <div>
            {/* Blacklist dropdown */}
            <label>Add to Blacklist:</label>
            <select
              onChange={handleBlacklistChange}
              value={selectedBlacklistPuzzle}
              className="border border-gray-300 rounded-md ml-5 mt-5 text-center px-3 py-2 mb-4 w-50 text-[#424242]"
            >
              <option value="">Select Puzzle Type</option>
              {puzzleTypes
                .filter((puzzle) => !blacklist.includes(puzzle.enum) && !whitelist.includes(puzzle.enum))
                .map((puzzle) => (
                  <option key={puzzle.enum} value={puzzle.enum}>
                    {puzzle.name}
                  </option>
                ))}
            </select>

            {/* Blacklist container */}
            <div className="flex flex-col items-start max-w-full">
              <label className="mb-2">Blacklist:</label>
              <div className="blacklist-container overflow-auto max-h-40 max-w-80">
                {blacklist.map((puzzleValue, index) => {
                  const puzzle = puzzleTypes.find(
                    (p) => p.enum === puzzleValue
                  );
                  if (!puzzle) return null; // Skip if puzzle is not found
                  return (
                    <div
                      key={index}
                      className="inline-block ml-2 mb-2 px-3 py-1 bg-white rounded text-[#424242]"
                    >
                      {puzzle.name}
                      <button
                        onClick={() =>
                          handleRemovePuzzleType(puzzleValue, "blacklist")
                        }
                        className="ml-1 text-xs text-gray-500"
                      >
                        X
                      </button>
                    </div>
                  );
                })}
              </div>
            </div>
          </div>

          <div className="flex items-center mt-4 mb-6">
            <input
              type="checkbox"
              id="toggle"
              className="sr-only"
              checked={isPublic}
              onChange={handleToggle}
            />
            <label
              htmlFor="toggle"
              className={`flex items-center justify-between w-12 h-6 bg-gray-300 rounded-full p-1 transition duration-300 ${isPublic ? 'bg-blue-500' : ''
                }`}
            >
              <div className={`w-5 h-5 bg-[#424242] rounded-full shadow-md transform duration-300 ${isPublic ? 'translate-x-6' : ''}`} />
            </label>
            <span className="ml-2">{isPublic ? 'Room is public' : 'Room is private'}</span>
          </div>


          <div>
            {/* Generate button */}
            <div className="flex flex-col items-center mb-5 mt-5">
              <button
                onClick={generate}
                className={`py-2 px-4 rounded ${loading
                  ? "bg-gray-500 cursor-not-allowed"
                  : theme != 0 && difficulty != 0
                    ? "bg-blue-500 hover:bg-blue-600 text-white font-bold"
                    : "bg-gray-300"
                  }`}
                disabled={loading || theme === 0 || difficulty === 0}
              >
                {loading ? "Generating..." : generated ? "Generate Again" : "Generate Escape Room"}
              </button>
              {loading && <LoadingSpinner />}
            </div>



            {/* Download button */}
            {downloadUrl && (
              <a
                href={downloadUrl}
                className="bg-[#424242] hover:bg-blue-600 mb-10 text-white font-bold py-2.5 px-4 rounded"
                target="_blank"
                rel="noopener noreferrer"
              >
                Download Escape Room
              </a>
            )}

            {/* Edit button */}
            {generated && (
              <div className="flex flex-col items-center mt-5 mb-3">
                <a
                  className="bg-[#424242] hover:bg-blue-600 text-white font-bold py-2.5 px-4 rounded"
                  href="edit"
                >
                  Edit Room
                </a>
              </div>
            )}

            {/* Play button */}
            {generated && (
              <div className="flex flex-col items-center mb-3">
                <a
                  className="bg-[#424242] hover:bg-blue-600 text-white font-bold py-2.5 px-4 rounded"
                  href="play"
                >
                  Play Escape Room!
                </a>
              </div>
            )}
          </div>

          {/* My rooms button */}
          <div className="flex flex-col items-center mb-5">
            <a
              className="bg-[#424242] hover:bg-blue-600 text-white font-bold py-2.5 px-4 rounded"
              href="rooms"
            >
              My Rooms
            </a>
          </div>

        </div>
      </div>
    </div >
  );
};

export default GeneratorPage;
