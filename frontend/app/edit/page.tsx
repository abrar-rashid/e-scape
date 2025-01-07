"use client";

import React, { useState, useEffect } from "react";
import axios from "axios";
import LoadingSpinnerSmall from "../components/LoadingSpinnerSmall";
import LoadingSpinner from "../components/LoadingSpinner";
axios.defaults.withCredentials = true

const EditEscapeRoomPage: React.FC = () => {
  const [introduction, setIntroduction] = useState<string>("");
  const [storyPhases, setStoryPhases] = useState<string[]>([]);
  const [conclusion, setConclusion] = useState<string>("");
  const [failure, setFailure] = useState<string>("");
  const [selectedPuzzles, setSelectedPuzzles] = useState<number[]>([]);
  const [solutions, setSolutions] = useState<string[]>([]);
  const [puzzleTypes, setPuzzleTypes] = useState<
    { enum: number; name: string }[]
  >([]);
  const [roomId, setRoomId] = useState('');
  const [roomName, setRoomName] = useState('');
  const [theme, setTheme] = useState<number>(0);
  const [themes, setThemes] = useState<{ enum: number; name: string }[]>([]);
  const [keywords, setKeywords] = useState<string[]>([]);
  const [difficulty, setDifficulty] = useState<string>("");
  const [length, setLength] = useState<number>(0);
  const [whitelist, setWhitelist] = useState<number[]>([]);
  const [blacklist, setBlacklist] = useState<number[]>([]);
  const [downloadUrl, setDownloadUrl] = useState<string>("");
  const [loadingIntro, setLoadingIntro] = useState(false);
  const [loadingPhase, setLoadingPhase] = useState(false);
  const [loadingConclusion, setLoadingConclusion] = useState(false);
  const [loadingFailure, setLoadingFailure] = useState(false);
  const [loadingGeneration, setLoadingGeneration] = useState(false);
  const [selectedWhitelistPuzzle, setSelectedWhitelistPuzzle] =
    useState<number>(0);
  const [selectedBlacklistPuzzle, setSelectedBlacklistPuzzle] =
    useState<number>(0);
  const [generated, setGenerated] = useState<boolean>(false);
  const [backgroundImage, setBackgroundImage] = useState<string>(
    "images/generator_bg.png"
  );
  const [editingIntro, setEditingIntro] = useState(false);
  const [editedIntro, setEditedIntro] = useState(introduction);
  const [editingConclusion, setEditingConclusion] = useState(false);
  const [editedConclusion, setEditedConclusion] = useState(introduction);
  const [editingFailure, setEditingFailure] = useState(false);
  const [editedFailure, setEditedFailure] = useState(introduction);
  const [editingIndex, setEditingIndex] = useState(-1);
  const [editedPhase, setEditedPhase] = useState("");
  const [isPublic, setIsPublic] = useState<boolean>(false);

  useEffect(() => {
    const fetchRoomState = async () => {
      try {
        const response = await axios.get(
          `http://146.169.43.38:8080/api/room-state`
        );
        console.log(response.data);
        setRoomName(response.data.name)
        setTheme(response.data.theme);
        setKeywords(response.data.keywords);
        setDifficulty(response.data.difficulty);
        setLength(response.data.length);
        setWhitelist(response.data.whitelist);
        setBlacklist(response.data.blacklist);
        setSelectedPuzzles(response.data.puzzles);
        setSolutions(response.data.solutions);
        setRoomId(response.data.id)
        setDownloadUrl(`http://146.169.43.38:8080/api/get-pdf/${response.data.id}`);
        setIntroduction(response.data.introduction);
        setStoryPhases(response.data.story_phases);
        setConclusion(response.data.conclusion);
        setFailure(response.data.failure);
        setIsPublic(response.data.is_public)
        console.log(isPublic)
      } catch (error) {
        console.error("Error fetching room state:", error);
      }
    };

    fetchRoomState();
  }, []);

  const regenerate = async () => {
    setLoadingGeneration(true);

    // // Fetch background image path based on selected theme
    // const response = await axios.get(`http://146.169.43.38:8080/api/background-image/${theme}`);
    // setBackgroundImage(response.data.url);

    try {
      const update = await axios.get(
        "http://146.169.43.38:8080/api/update-room"
      );
      var res = `http://146.169.43.38:8080/api/get-pdf/${roomId}`
      setDownloadUrl(res);
      setGenerated(true);
    } catch (error) {
      console.error("Error generating PDF:", error);
    }
    setLoadingGeneration(false);
  };

  const changeTheme = async () => {
    try {
      const response = await axios.post(
        `http://146.169.43.38:8080/api/change-theme/${theme}`
      );
      setTheme(response.data.theme);
    } catch (error) {
      console.error("Error regenerating theme:", error);
    }
  };

  const changeKeywords = async () => {
    try {
      const response = await axios.post(
        `http://146.169.43.38:8080/api/change-keywords/${keywords}`
      );
      setTheme(response.data.theme);
    } catch (error) {
      console.error("Error regenerating theme:", error);
    }
  };

  const changeDifficulty = async () => {
    try {
      const response = await axios.post(
        `http://146.169.43.38:8080/api/change-difficulty/${difficulty}`
      );
      setTheme(response.data.theme);
    } catch (error) {
      console.error("Error regenerating theme:", error);
    }
  };

  const changeLength = async () => {
    try {
      const response = await axios.post(
        `http://146.169.43.38:8080/api/change-length/${length}`
      );
      setTheme(response.data.theme);
    } catch (error) {
      console.error("Error regenerating theme:", error);
    }
  };

  const changeWhitelist = async () => {
    try {
      const response = await axios.post(
        `http://146.169.43.38:8080/api/change-whitelist/${whitelist}`
      );
      setTheme(response.data.theme);
    } catch (error) {
      console.error("Error regenerating theme:", error);
    }
  };

  const changeBlacklist = async () => {
    try {
      const response = await axios.post(
        `http://146.169.43.38:8080/api/change-blacklist/${blacklist}`
      );
      setTheme(response.data.theme);
    } catch (error) {
      console.error("Error regenerating theme:", error);
    }
  };

  const regenerateIntroduction = async () => {
    setLoadingIntro(true);
    try {
      const response = await axios.post(
        "http://146.169.43.38:8080/api/regenerate-introduction"
      );
      setIntroduction(response.data.introduction);
    } catch (error) {
      console.error("Error regenerating introduction:", error);
    }
    setLoadingIntro(false);
  };

  const regeneratePhase = async (index: number) => {
    // Regenerates story, puzzle and solution
    setLoadingPhase(true);
    try {
      // Any calls to the backend must offset the index by + 1 for phases
      const response = await axios.post(
        `http://146.169.43.38:8080/api/regenerate-story-phase/${index + 1}`
      );
      storyPhases[index] = response.data.story_phase;
      var newStoryline: string[] = storyPhases;
      newStoryline[index] = response.data.story_phase;
      setStoryPhases(newStoryline);
      changeSolution(index);
    } catch (error) {
      console.error("Error regenerating story phase:", error);
    }
    setLoadingPhase(false);
  };

  const regenerateConclusion = async () => {
    setLoadingConclusion(true);
    try {
      const response = await axios.post(
        "http://146.169.43.38:8080/api/regenerate-conclusion"
      );
      setConclusion(response.data.conclusion);
    } catch (error) {
      console.error("Error regenerating conclusion:", error);
    }
    setLoadingConclusion(false);
  };


  const regenerateFailure = async () => {
    setLoadingFailure(true);
    try {
      const response = await axios.post(
        "http://146.169.43.38:8080/api/regenerate-failure"
      );
      setFailure(response.data.failure);
    } catch (error) {
      console.error("Error regenerating failure:", error);
    }
    setLoadingFailure(false);
  };

  const changePuzzle = async (index: number, newPuzzleEnum: number) => {
    console.log(index);
    try {
      // Any calls to the backend must offset the index by 1
      await axios.post("http://146.169.43.38:8080/api/change-puzzle/", {
        phase: index + 1,
        new_puzzle: newPuzzleEnum,
      });

      // Update the selected puzzle at the specified index
      const updatedSelectedPuzzles = [...selectedPuzzles];
      updatedSelectedPuzzles[index] = newPuzzleEnum;
      setSelectedPuzzles(updatedSelectedPuzzles);
    } catch (error) {
      console.error("Error changing puzzle:", error);
    }
  };

  const changeSolution = async (index: number) => {
    try {
      // Any calls to the backend must offset the index by 1
      console.log(index)
      console.log(solutions[index])
      await axios.post("http://146.169.43.38:8080/api/change-solution/", {
        phase: index + 1,
        solution: solutions[index],
      });
      // Update the selected puzzle at the specified index
    } catch (error) {
      console.error("Error changing solution:", error);
    }
    console.log(index);
    console.log(solutions);
  };

  useEffect(() => {
    const iframe = document.getElementById("pdfPreview") as HTMLIFrameElement;
    if (iframe && downloadUrl && !loadingGeneration) {
      iframe.src = downloadUrl;
    }
  }, [loadingGeneration]);

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


  const handleToggle = async () => {
    setIsPublic(!isPublic);
    console.log(!isPublic)
    try {
      await axios.post(
        `http://146.169.43.38:8080/api/toggle-public/${!isPublic}`
      );
    } catch (error) {
      console.error("Error toggling public:", error);
    }
  }

  const handleEditIntroClick = () => {
    setEditedIntro(introduction);
    setEditingIntro(true);
  };

  const handleSaveIntroClick = async () => {
    setIntroduction(editedIntro);
    setEditingIntro(false);
    setLoadingIntro(true);
    try {
      await axios.post(
        `http://146.169.43.38:8080/api/edit-introduction/${editedIntro}`
      );
    } catch (error) {
      console.error("Error saving introduction:", error);
    }
    setLoadingIntro(false);
  };

  const handleCancelIntroClick = () => {
    setEditingIntro(false);
    // Reset edited introduction to current introduction
    setEditedIntro(introduction);
  };

  const handleChangeIntro = (e: { target: { value: React.SetStateAction<string>; }; }) => {
    setEditedIntro(e.target.value);
  };



  const handleEditPhaseClick = (index: number) => {
    setEditingIndex(index);
    setEditedPhase(storyPhases[index]);
  };

  const handleSavePhaseClick = async (index: number) => {
    setEditingIndex(-1);
    setLoadingPhase(true);
    try {
      // Any calls to the backend must offset the index by + 1 for phases
      console.log(index + 1)
      console.log(storyPhases[index])
      const response = await axios.post('http://146.169.43.38:8080/api/edit-story-phase', {
        phase: index + 1,
        text: editedPhase
      })
      storyPhases[index] = response.data.story_phase;
      var newStoryline: string[] = storyPhases;
      newStoryline[index] = response.data.story_phase;
      setStoryPhases(newStoryline);
      // changeSolution(index);
    } catch (error) {
      console.error("Error editing story phase:", error);
    }
    setLoadingPhase(false);
  };

  const handleCancelPhaseClick = (index: number) => {
    setEditingIndex(-1);
    setEditedPhase(storyPhases[index]);
  };

  const handleChangePhase = (e: { target: { value: React.SetStateAction<string>; }; }) => {
    setEditedPhase(e.target.value);
  };



  const handleEditConclusionClick = () => {
    setEditedConclusion(conclusion);
    setEditingConclusion(true);
  };


  const handleSaveConclusionClick = async () => {
    setConclusion(editedConclusion);
    setEditingConclusion(false);
    setLoadingConclusion(true);
    try {
      await axios.post(
        `http://146.169.43.38:8080/api/edit-conclusion/${editedConclusion}`
      );
    } catch (error) {
      console.error("Error saving conclusion:", error);
    }
    setLoadingConclusion(false);
  };


  const handleCancelConclusionClick = () => {
    setEditingConclusion(false);
    // Reset edited conclusion to current conclusion
    setEditedConclusion(conclusion);
  };


  const handleChangeConclusion = (e: { target: { value: React.SetStateAction<string>; }; }) => {
    setEditedConclusion(e.target.value);
  };



  const handleEditFailureClick = () => {
    setEditedFailure(failure);
    setEditingFailure(true);
  };


  const handleSaveFailureClick = async () => {
    setFailure(editedFailure);
    setEditingFailure(false);
    setLoadingFailure(true);
    try {
      await axios.post(
        `http://146.169.43.38:8080/api/edit-failure/${editedFailure}`
      );
    } catch (error) {
      console.error("Error saving failure:", error);
    }
    setLoadingFailure(false);
  };


  const handleCancelFailureClick = () => {
    setEditingFailure(false);
    setEditedFailure(failure);
  };


  const handleChangeFailure = (e: { target: { value: React.SetStateAction<string>; }; }) => {
    setEditedFailure(e.target.value);
  };



  return (
    <div
      className="flex flex-col text-white justify-center items-center min-h-screen p-20 bg-fixed bg-cover bg-center transition-all duration-300"
      style={{
        backgroundImage: `url(${backgroundImage})`,
        backgroundSize: "cover",
        backgroundPosition: "center",
        transition: "background-image 3s ease-in-out",
      }}
    >

      <header className="text-7xl font-bold text-center mt-10 mb-20 font-mono text-[#424242]">
        Edit Escape Room
      </header>

      <div className="flex justify-center items-center w-full">
        {/* Left half containing editing elements */}
        <div className="flex flex-col justify-center items-center mb-16 w-1/2 pr-5">

          {/* Room Name */}
          <div className="text-[#424242] font-bold border border-white text-xl justify-left p-2 pr-4 pl-4 rounded-md mb-6 flex flex-wrap">
            Room: {roomName}
          </div>

          {/* Introduction */}
          <div className="text-[#424242] font-bold text-xl p-2 pl-4 rounded-md mb-2 flex flex-wrap">
            <h1> Introduction </h1>
            {loadingIntro && <LoadingSpinnerSmall />}
          </div>
          <div className="bg-gray-100 p-4 rounded-md text-black mb-10">
            {editingIntro ? (
              <textarea
                value={editedIntro}
                onChange={handleChangeIntro}
                className="w-full h-40 p-2 mb-3 resize-none"
              />
            ) : (
              <p>{introduction}</p>
            )}
            <button
              onClick={regenerateIntroduction}
              className="mt-5 bg-yellow-500 hover:bg-yellow-600 text-white font-bold py-2 px-4 rounded"
              disabled={editingIntro}
            >
              Regenerate
            </button>
            {editingIntro ? (
              <div className="mt-2">
                <button
                  onClick={handleSaveIntroClick}
                  className="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded mr-2"
                >
                  Save
                </button>
                <button
                  onClick={handleCancelIntroClick}
                  className="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded"
                >
                  Cancel
                </button>
              </div>
            ) : (
              <button
                onClick={handleEditIntroClick}
                className="mt-2 ml-2 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded"
              >
                Edit
              </button>
            )}
          </div>


          {/* Phases */}
          <div className="text-[#424242] p-2 pl-4 font-bold text-xl rounded-md mb-2 flex flex-wrap">
            <h2>Phases</h2>
            {loadingPhase && <LoadingSpinnerSmall />}
          </div>

          <div className="bg-gray-100 p-10 rounded-md text-black">
            {storyPhases &&
              storyPhases.map((phase_text, index) => (
                <div
                  key={index}
                  className="bg-grey-100 p-1.5 mb-10 rounded-md text-black"
                >
                  <div className="bg-blue-100 p-2 mb-5 text-center rounded-md">
                    <h3>Phase {index + 1}</h3>
                  </div>

                  {/* <p>Puzzle: {selectedPuzzles[index + 1]?.name}</p> */}

                  <label>Puzzle:</label>
                  <select
                    onChange={(e) => {
                      if (!loadingPhase) {
                        changePuzzle(index, parseInt(e.target.value));
                      }
                    }}
                    value={selectedPuzzles[index]}
                    className="border border-gray-300 rounded-md text-center ml-4 mt-4 px-3 py-2 mb-4 w-50 text-black"
                  >
                    {selectedPuzzles[index] !== undefined && (
                      <option value={selectedPuzzles[index]}>
                        {
                          puzzleTypes.find(
                            (puzzle) => puzzle.enum === selectedPuzzles[index]
                          )?.name
                        }
                      </option>
                    )}
                    {puzzleTypes
                      .filter((puzzle) => puzzle.enum != selectedPuzzles[index])
                      .map((puzzle) => (
                        <option key={puzzle.enum} value={puzzle.enum}>
                          {puzzle.name}
                        </option>
                      ))}
                  </select>

                  <div className="flex items-center justify-center">
                    <label className="mb-2 text-black mr-4">Solution:</label>
                    <div className="flex flex-col">
                      <input
                        type="text"
                        value={solutions[index]}
                        onChange={(e) => {
                          if (!loadingPhase) {
                            // Check if loadingPhase is false
                            const inputValue = e.target.value;
                            if (inputValue.length <= 6) {
                              // Check if the input value length is less than or equal to 6
                              const updatedSolutions = [...solutions]; // Create a copy of the solutions array
                              updatedSolutions[index] = inputValue; // Update the value at the specified index
                              setSolutions(updatedSolutions); // Set the state with the updated array
                            }
                          }
                        }}
                        className="border border-gray-300 mr-2rounded-md px-3 py-2 mb-2 w-40 text-black placeholder-gray-400"
                        placeholder="Enter 6 digits"
                      />
                    </div>
                  </div>


                  <div>

                    <div key={index} className="bg-white p-3 outline-4 rounded-md mb-4">
                      {editingIndex === index ? (
                        <textarea
                          value={editedPhase}
                          onChange={handleChangePhase}
                          className="w-full h-40 mb-2"
                        />
                      ) : (
                        <div
                          className="mb-3"
                        >{storyPhases[index]}</div>
                      )}

                      <button
                        onClick={() => regeneratePhase(index)}
                        className="ml-3 bg-yellow-500 hover:bg-yellow-600 mr-2 text-white font-bold py-1 px-2 rounded"
                      >
                        Regenerate
                      </button>

                      {editingIndex === index ? (
                        <div>
                          <button
                            onClick={() => handleSavePhaseClick(index)}
                            className="bg-green-500 hover:bg-green-600 text-white font-bold py-1 px-2 mt-2 rounded mr-2"
                          >
                            Save
                          </button>
                          <button
                            onClick={() => handleCancelPhaseClick(index)}
                            className="bg-red-500 hover:bg-red-600 mb-2 text-white font-bold py-1 px-2 rounded"
                          >
                            Cancel
                          </button>
                        </div>
                      ) : (
                        <button
                          onClick={() => handleEditPhaseClick(index)}
                          className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-1 px-2 rounded"
                        >
                          Edit
                        </button>
                      )}

                    </div>

                  </div>


                </div>
              ))}
          </div>


          {/* Conclusion */}
          <div className="text-[#424242] font-bold text-xl p-2 pl-4 mt-10 rounded-md mb-2 flex flex-wrap">
            <h1> Victory </h1>
            {loadingConclusion && <LoadingSpinnerSmall />}
          </div>
          <div className="bg-gray-100 p-4 rounded-md text-black">
            {editingConclusion ? (
              <textarea
                value={editedConclusion}
                onChange={handleChangeConclusion}
                className="w-full h-40 p-2 mb-3 resize-none"
              />
            ) : (
              <p>{conclusion}</p>
            )}

            <button
              onClick={regenerateConclusion}
              className="mt-5 bg-yellow-500 hover:bg-yellow-600 text-white font-bold py-2 px-4 rounded"
            >
              Regenerate
            </button>


            {editingConclusion ? (
              <div className="mt-2">
                <button
                  onClick={handleSaveConclusionClick}
                  disabled={loadingConclusion}
                  className={`bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 mr-2 rounded ${loadingConclusion ? "cursor-not-allowed" : ""
                    }`}

                >
                  Save
                </button>
                <button
                  onClick={handleCancelConclusionClick}
                  className="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded"
                >
                  Cancel
                </button>
              </div>
            ) : (
              <button
                onClick={handleEditConclusionClick}
                className="bg-blue-500 ml-2 mt-5 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded"
              >
                Edit
              </button>
            )}
          </div>



          {/* Failure */}
          <div className="text-[#424242] font-bold text-xl p-2 pl-4 mt-10 rounded-md mb-2 flex flex-wrap">
            <h1> Failure (In Game)</h1>
            {loadingFailure && <LoadingSpinnerSmall />}
          </div>
          <div className="bg-gray-100 p-4 rounded-md text-black">
            {editingFailure ? (
              <textarea
                value={editedFailure}
                onChange={handleChangeFailure}
                className="w-full h-40 p-2 mb-3 resize-none"
              />
            ) : (
              <p>{failure}</p>
            )}

            <button
              onClick={regenerateFailure}
              className="mt-5 bg-yellow-500 hover:bg-yellow-600 text-white font-bold py-2 px-4 rounded"
            >
              Regenerate
            </button>


            {editingFailure ? (
              <div className="mt-2">
                <button
                  onClick={handleSaveFailureClick}
                  disabled={loadingFailure}
                  className={`bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 mr-2 rounded ${loadingFailure ? "cursor-not-allowed" : ""
                    }`}

                >
                  Save
                </button>
                <button
                  onClick={handleCancelFailureClick}
                  className="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded"
                >
                  Cancel
                </button>
              </div>
            ) : (
              <button
                onClick={handleEditFailureClick}
                className="bg-blue-500 ml-2 mt-5 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded"
              >
                Edit
              </button>
            )}
          </div>

{/* 
          <div className="flex items-right mt-10">
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
              <div className={`w-5 h-5 bg-blue-500 rounded-full shadow-md transform duration-300 ${isPublic ? 'translate-x-6' : ''}`} />
            </label>
            <span className="ml-2">{isPublic ? 'Room is public' : 'Room is private'}</span>
          </div> */}


          <div className="flex flex-col items-center">
            <button
              onClick={regenerate}
              className={`py-5 px-10 mt-10 mb-3 items-center rounded ${loadingGeneration
                ? "bg-gray-500 cursor-not-allowed"
                : "bg-blue-500 hover:bg-blue-600 text-white font-bold"
                }`}
              disabled={loadingGeneration}
            >
              {loadingGeneration
                ? "Generating..."
                : generated
                  ? "Save"
                  : "Save"}
            </button>
            <div className="flex items-center">
              {loadingGeneration && <LoadingSpinner />}
            </div>
          </div>

          {downloadUrl && (
            <a
              href={downloadUrl}
              className="bg-blue-500 py-5 items-center px-10 mt-5 mb-5 hover:bg-blue-600 text-white font-bold rounded"
              target="_blank"
              rel="noopener noreferrer"
            >
              Download Escape Room
            </a>
          )}

          {(
            <div className="mt-7">
              <a
                className="bg-blue-500 py-5 px-10 items-center hover:bg-blue-600 text-white font-bold rounded"
                href="play"
              >
                {" "}
                Play Escape Room!
              </a>
            </div>
          )}

          {/* My rooms button */}
          {(
            <div className="flex flex-col items-center mt-10">
              <a
                className="bg-blue-500 py-5 px-10 items-center hover:bg-blue-600 text-white font-bold rounded"
                href="rooms"
              >
                My Rooms
              </a>
            </div>
          )}
        </div>

        {/* Right half containing PDF preview */}
        <div className="w-1/2 h-full ml-10 p-5 mb-80 rounded-md">
          {downloadUrl && (
            <iframe
              id="pdfPreview"
              src={`${downloadUrl}`}
              width="100%"
              height="1800"
              title="PDF Preview"
            />
          )}
        </div>
      </div>
    </div>
  );
};

export default EditEscapeRoomPage;
