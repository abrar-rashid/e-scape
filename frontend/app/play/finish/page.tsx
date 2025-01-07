import { getRoom } from '../getRoom';
import '../styles/styles.css';
import { im_fell_english_sc } from "../../fonts";
import TypewriterText from '../typewriter';


// Displays the final conclusion of the escape room once all puzzles are solved - can navigate back to landing page

export default async function FinishPage() {
    const room = await getRoom(1);
    const conclusion = room ? room.conclusion : 'Room has not been generated yet'
    return(
      <div>
        <div className="background-image" style={{backgroundImage: `url(../../../${room ? room.theme_url : 'images/background.png'})`}}></div>
        <div className={`${im_fell_english_sc.className} flex flex-col justify-center items-center h-screen fade`}>
              <div className={`div-background max-w-[120ch] mx-2 overflow-y-auto`}>
                <TypewriterText text={conclusion} />
              </div>
            <div className="p-9 animate-pulse">
              <a
              className="text-red-600 hover:text-red-700 font-bold text-5xl box-border p-1 border-4 border-dashed rounded-lg border-red-600 hover:border-red-700"
              href="/play"
              > PLAY AGAIN
              </a>
            </div>
        </div>
      </div>
    );
  }