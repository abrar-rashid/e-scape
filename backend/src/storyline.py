from guidance import assistant, gen, models, system, user
from openai import OpenAI
from src.pages.pageTypes import PuzzleType, Difficulty

client = OpenAI()

gpt = models.OpenAI("gpt-3.5-turbo")

# puzzles = ["cipher", "text", "numerical", "passphrase", "maze", "morse code"]
puzzles = [member.name for member in PuzzleType]


class Storyline():
    def __init__(self, theme, keywords, difficulty, length, current_puzzles):
        # Initialise context
        self.gpt = models.OpenAI("gpt-3.5-turbo")
        self.theme = theme
        self.keywords = keywords
        self.difficulty = difficulty
        self.length = length
        self.current_puzzles = current_puzzles
        self.context = f"""Craft an enthralling and suspenseful storyline that
        will be used for an escape room adventure but you cannot say that.
        The storyline must be thematically inspired by an
        overarching theme and the adventure should span across multiple puzzle
        phases, each corresponding to a unique scenario for each puzzle.
        You want to engage me as the participants
        personally and you can use and include a diverse range of narrative
        elements and tools to engage us. The narrative should
        build anticipation and curiosity, encouraging us as players
        to explore and uncover the secrets within each phase. Create
        a seamless chronological and logical flow between puzzles,
        ensuring they align with the overarching theme.
        You can introduce twists and surprises to keep
        players on their toes, and you must provide opportunities for
        interactive and immersive experiences through the introduction
        and descriptions of unique story characters inspired by the
        overarching theme and given keyphrases.
        Always speak to me in the second person and from the perspective of
        someone who knows me very well and is a character from the world of the
        given overarching theme and given keyphrases. There will be a total
        of {self.length} puzzle phases.
        The overarching theme will be '{self.theme.name}'. You must
        craft the storyline to match the difficulty of """
        match difficulty:
            case Difficulty.EASY:
                self.context += "'amateur'"
            case Difficulty.MEDIUM:
                self.context += "'intermediate'"
            case Difficulty.HARD:
                self.context += "'professional'"
        self.context += """ and you must use language that is fitting
        for someone of that level of expertise in the field of
        the overarching theme and given keyphrases.
        The story must be thematically
        inspired by the following given keyphrases which you must use
        the knowledge you have of them to expand on them to improve
        the immersiveness of the narrative: {"""\
            + ", ".join(self.keywords)
        with system():
            self.txt = self.gpt + self.context\
                + """} and the story must have 1 very unique impending
                threat which you must create and name and you must
                use the overarching theme and given keyphrases for inspiration
                in making the threat.
                The named threat must be creatively structured to fit the
                overall narrative and you must creatively explain what
                exactly the threat is in detail, but you must not
                directly use the word "threat". You must speak to me in an
                emotionally charged and urgent manner and you must
                try to creatively explain everything to me."""

    def generate_introduction(self):
        with user():
            self.txt += """Begin the narrative with
            a concise and intriguing exposition and creative
            introduction for our adventure, letting me know your name and
            who you are. You must explain where
            we are and what has happened so far to get to
            this starting point of our adventure, and you must explain
            the named threat to the adventure, ensuring that the
            threat as well as the plot is unique and is
            thematically related to the overarching theme and
            also uses as many of the given keyphrases as possible.
            You must only provide 2 expertly written sentences."""
        with assistant():
            self.txt += gen("introduction")
        self.introduction = self.txt["introduction"]
        return self.txt["introduction"]

    def generate_phases(self):
        for i in range(1, self.length + 1):
            with user():
                puzzle = PuzzleType(self.current_puzzles[i - 1]).get_name()
                if i == 1:
                    self.txt += f"""Remember how the story began which was:
                    '{self.introduction}', """
                if i > 1:
                    self.txt += f"""Remember the previous part
                    of the story which was: '{self.txt[f'phase {i-1}']}', """
                self.txt += f"""Write phase {i} of our adventure with a title
                in the format 'Phase <i>: <name of phase>/n/n', and you must
                creatively emphasize a sense of urgency which you must
                explain creatively that relates to the overarching theme,
                and you can use one of the given keyphrases to help create a
                very short subplot for this specific phase.
                The puzzle will be a {puzzle} based puzzle and you
                must creatively hint at the method of solving the puzzle
                using the current scenario.
                Do not include or use the words "{puzzle}"
                or any other puzzle types
                in the phase, you must instead replace the word with a creative
                description that matches the story at this phase.
                Link the reason for solving this puzzle to the
                specific and unique problem scenario in this exact
                phase of the adventure. Ensure this phase logically continues
                from the previous part of the story without referring to the
                specific thing we had to do in the previous part.
                You must only provide 2 sentences."""
            with assistant():
                self.txt += gen(f"phase {i}")
        self.phases = [self.txt[f'phase {i}']
                       for i in range(1, self.length + 1)]
        return self.phases

    def generate_conclusion(self):
        with user():
            self.txt += """Conclude our adventure with an
            emotional and satisfying resolution which you must
            creatively craft to match the overarching theme and descibes
            how exactly I defeat the named threat in detail
            and what I used to do it.
            Ensure that what happens here logically continues
            from the previous part of the story, but do not refer to any
            specific thing we had to do in the previous part.
            Ensure it uniquely explains any unanswered questions
            and that it leaves me with a sense of
            accomplishment and satisfaction that also provides me with
            rewards for completing
            all the challenging puzzles and encourages me to try
            it again someday. You must only provide 3 sentences."""
        with assistant():
            self.txt += gen("conclusion")
        self.conclusion = self.txt["conclusion"]
        return self.conclusion

    def generate_failure(self):
        with user():
            self.txt += """Write the ending of our adventure
            by concluding our adventure
            with a sad and dissapointing resolution where you describe how
            exactly I lost to the named threat and what it did in detail.
            Write the conclusion in a way that
            leaves us with a sense of anguish and sorrow for not being
            able to finish one of the puzzles in time, even
            though you know that I am more than capable of solving
            them as I have the perfect
            skillset but was just unfortunate this time. Ensure that you
            creatively write the ending using the context of the overarching
            theme and the given keyphrases but provide a hint
            of encouragement that I can win if I just attempt it once more.
            You must only provide 3 sentences."""
        with assistant():
            self.txt += gen("failure")
        self.failure = self.txt["failure"]
        return self.failure

    def regenerate_puzzle_phase(self, phase_number, new_puzzle):
        with user():
            self.txt += f"""Regenerate phase {phase_number}
                of the story text which was: '{self.phases[phase_number-1]}',
                and the puzzle that it referred to with
                a {new_puzzle} puzzle whilst ensuring
                it still makes logical sense and that
                it fits in with the surrounding parts of the text.
                Do not include anything that shows this was regenerated.
                Do not include or use the words "{new_puzzle}"
                or any other puzzle types anywhere in this phase,
                you must instead replace the words with a creative
                description that matches the story at this phase.
                Edit the title to thematically match
                the new puzzle but you must
                retain the title's original formatting.
                You must only provide 2 sentences."""
        with assistant():
            self.txt += gen(f"new phase {phase_number}")
        self.phases[phase_number - 1] = self.txt[f"new phase {phase_number}"]
        return self.phases[phase_number - 1]
