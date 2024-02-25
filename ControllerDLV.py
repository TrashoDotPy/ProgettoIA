from embasp.platforms.desktop.desktop_handler import DesktopHandler
from embasp.specializations.dlv2.desktop.dlv2_desktop_service import DLV2DesktopService
from embasp.languages.asp.asp_input_program import ASPInputProgram
import platform

class ControllerDLV:
    def __init__(self):
        self.facts = ""

        operating_system = platform.system()
        supported = ["Linux","Windows","Darwin"]

        if operating_system in supported:
            dlv_path = "dlv/dlv-2-" + operating_system
        else:
            raise ValueError("Operating system not supported")
        
        self.handler = DesktopHandler(DLV2DesktopService(dlv_path))

        programFixed = ASPInputProgram()
        programFixed.add_files_path("dlv/rules.txt")
        self.handler.add_program(programFixed)
        
        self.programVariable = ASPInputProgram()
        self.handler.add_program(self.programVariable)
    
    def getSolution(self):
        result = self.handler.start_sync()
        answersets = result.get_answer_sets()

        for answerset in answersets:
            return str(answerset)

    def set_DLV(self):
        self.programVariable.clear_all()
        self.programVariable.add_program(self.facts)

    def set_facts(self, facts):
        self.facts = facts