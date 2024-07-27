""" falcon_wizard.py

    Math_Wings is an interative latex mathematics chatbot for math research, problem solving,
    learning, teaching, plotting, and paper writing. Math_Wings is build on the AI71's
    tiiuae/falcon-180B-chat.

"""

from ai71 import AI71
import os
from wand.read_write import read_write_class
from wand.speech_rec import speech_rec
from wand.cmdline_colors import colors
# from wand.text_to_speech import text_to_speech

# from wand.cmdline_colors import cmdline_colors
# from wand.rag_base import rag_base

# -------------------------------------------------------------------------------------------------
class math_wings:
    '''
    A class for managing the MATH_WINGS falcon chatbot and its toolset.
    '''

    def __init__(self):
        """
        Default Constructor
        """
        # get path
        self.current_dir = os.getcwd()
        # get api key path
        self.read_json_path_construct = os.path.join(self.current_dir, "FALCON_API_KEY.json")
        
        self.colors_instance = colors()
        self.color_dict = self.colors_instance.get_colors()
        
        # init read_write_class and get api key
        self.read_write_class_instance = read_write_class()
        # collect api key from json
        self.api_key_dict = self.read_write_class_instance.read_json_dict(self.read_json_path_construct)
        # get api key from dictionary
        self.COLLECTED_API_KEY = self.api_key_dict["$(falcon_api_key.developer_custom)"]
        
        #TODO SETUP SPEECH TO SPEECH TOOLS
        #TODO SETUP MATH RESEARCH TOOLS
        #TODO SETUP MATH RAG FOR FORMULAS AND PROBLEM SOLVING
        
        #TODO SETUP DUCKDUCKGO SEARCH API FOR MATH RESEARCH AND REFERENCE -> FEED RAG
        #TODO BUILD JAVA GUI FRONTEND
        
        #TODO SETUP MATPLOT LIB PLOTTING TOOL FROM LEOLEOJAMES/DIVISOR_WAVE_PRIME_&_COMPOSITE_COMPLEX_ANALYSIS
        #TODO SPEECH TO PLOT, TEXT FORMULA TO PLOT, SCREENSHOT LLAVA TO FORMULA TO PAPER PROBLEM SOLVER AND PLOT
        #TODO SETUP VISION MODEL FOR MATH FORMULA TRANSCRIPTION
        
        # start wand
        self.speech_rec_instance = speech_rec(self.color_dict)
 
    def start_client(self):
        """
        """
        self.AI71_API_KEY = f"{self.COLLECTED_API_KEY}"
        self.client = AI71(self.AI71_API_KEY)
        
    def system_prompt_set(self):
        """
        """
        # Streaming chatbot:
        self.messages = [{"role": "system", "content": "You are a helpful mathematics assistant. Please respond to the user with latex notation representation to solve the math."}]
        
    def chatbot_main(self):
        """ the main method for executing the chatbot loop
        """     
        while True:
            content = input(f"User:")
            self.messages.append({"role": "user", "content": content})
            print(f"Falcon:", sep="", end="", flush=True)
            content = ""

            for chunk in self.client.chat.completions.create(
                messages=self.messages,
                model="tiiuae/falcon-180B-chat",
                stream=True,
            ):
                delta_content = chunk.choices[0].delta.content
                if delta_content:
                    print(delta_content, sep="", end="", flush=True)
                    content += delta_content
            
            self.messages.append({"role": "assistant", "content": content})
            print("\n")
    
# -------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    """ 
    The main loop for the math_wings_instance. It uses a state machine for user command injection.
    """
    # init class
    math_wings_instance = math_wings()
    
    # start client
    math_wings_instance.start_client()
    
    # get system prompt
    math_wings_instance.system_prompt_set()
    
    # start chatbot
    math_wings_instance.chatbot_main()