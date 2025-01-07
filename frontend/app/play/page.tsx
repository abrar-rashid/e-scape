import './styles/styles.css';
import { im_fell_english_sc } from "../fonts";
import { getPDF } from './getRoom';
import axios from 'axios';
axios.defaults.withCredentials = true

export default async function PlayingWebsite() {
    const res = await getPDF();
    const pdfUrl = res ? res : '/play'

    return(
      <div className={`${im_fell_english_sc.className} flex flex-col justify-center items-center h-screen background-image`}>
        {/* <p>Playing Website Landing Page</p> */}
        <div className="text-7xl p-5 rounded-lg font-bold text-center mb-7 text-[#424242]">
          Play the Escape Room
        </div>
          <div className="p-4 mb-5 hover:bg-gradient-to-l from-gray-200 to-transparent rounded">
            <a
            target="_blank"
            rel="noopener noreferrer"
            href={pdfUrl}
            className="text-red-600 hover:text-red-700 font-bold text-5xl"
            > Download PDF
            <p className="text-xl">Get the Puzzles</p>
            </a>
          </div>

        <div className="p-4 hover:bg-gradient-to-l from-gray-200 to-transparent rounded">
          <a
          className="text-red-600 hover:text-red-700 font-bold text-5xl"
          href="/play/0"
          > Play
          <p className="text-xl">Begin Your Adventure</p>
          </a>
        </div>

      </div>
    );
  }