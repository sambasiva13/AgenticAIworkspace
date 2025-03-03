from configparser import ConfigParser

class config:
    def __init__(self,config_file="./src/langgragphagenticai/ui/uiconfigfile.ini"):
        self.config=ConfigParser()
        self.config.read(config_file)

    def get_llm_option(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ") # If there are muliple options it reads one by one seperated by ,
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")
    
    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")