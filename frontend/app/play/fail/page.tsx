// Displays the failure page of the escape room once timer runs out - can navigate back to landing page
import '../styles/styles.css';
import { im_fell_english_sc } from "../../fonts";
import TypewriterText from '../typewriter';
import { getRoom } from '../getRoom';

export default async function FailurePage() {
  const room = await getRoom(1);
  const conclusion = room ? room.failure : 'Room has not been generated yet'
    return (
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
              > RETRY
              </a>
            </div>
        </div>
      </div>
    );
  }