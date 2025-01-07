import InputPage from './input_page';
import '../styles/styles.css';
import { im_fell_english_sc } from "../../fonts";
import { getRoom } from '../getRoom';
import TypewriterText from '../typewriter';


// Params is an abject that contains the specific [stage] number at any page which is useful in determining which stage we are on
//  - passed through to InputPage to handle logic surrounding it
export default async function Stage({params}: any) {
    const room = await getRoom(1); 
    const story = room ? room.story_phases : [''];
    const sols = room ? room.solutions : ['']
    if (room) {
        story.unshift(room.introduction);
        story.push(room.conclusion);
    }
    console.log(sols)
    const storyAtStage = story[params.stage].replace(/\/n\/n/g, '')
    if (params.stage < 0 || params.stage >= story.length-1) { // Dont allow out of bounds page accesses
        console.error('Invalid stage number:', params.stage);
        return <div className="flex flex-col justify-center items-center h-screen">Invalid stage: {params.stage}</div>;
    }
    const justify = params.stage > 0 ? 'justify-center' : 'justify-center' // position text at top only for intro
    return(
        <div>
            <div className="background-image" style={{backgroundImage: `url(../../../${room ? room.theme_url : 'images/background.png'})`}}></div>
            <div className={`${im_fell_english_sc.className} flex flex-col py-5 ${justify} items-center h-screen  overflow-y-auto`} >
                <div className={`div-background max-w-[120ch] mx-2 overflow-y-auto fade`}>
                    <TypewriterText text={storyAtStage} />
                </div>
                
                <InputPage currentStage={params.stage} puzzleSols={sols}/>

            </div>
        </div>
    );
  }