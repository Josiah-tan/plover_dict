# from datetime import datetime

class Config1:
    def __init__(self, highlighting, file_name):
        self.highlighting = highlighting
        self.file_name = file_name

    def initPost(self, obj, clippy):
        clippy.state.output_file_name = self.file_name
        clippy.state.efficiency_symbol = "*"
        clippy.state.max_pad_efficiency = 5
        clippy.state.max_pad_english = 15
        if not self.highlighting:
            clippy.state.colors = {}

        if self.file_name == "clippy.txt":
            clippy.extremity.start_pre_sources.set()
            clippy.extremity.stop_pre_sources.set()

    def startPost(self, obj, clippy):
        if self.file_name == "clippy.txt":
            clippy.translations.sources.set("Retro")
            clippy.distillations.sources.set()
            clippy.formatting.sources.set(
                    ["Retro", {
                        "colorscheme": "gruvbox",
                        "mode": "defaultSuggest"}])


config = [
        Config1(True, "clippy_2.org"),
        Config1(True, "clippy.txt")
        ]

# config = [
#         Config1(True, "clippy_2.org"),
#         Config1(False, "clippy_2.org")
#         ]

# class Config:
#     def __init__(self):
#         self.file_name = "clippy_2.org"
#
#     def initPost(self, obj, clippy):
#         clippy.state.output_file_name = self.file_name
#         clippy.state.efficiency_symbol = "*"
#         clippy.state.max_pad_efficiency = 5
#         clippy.state.max_pad_english = 15
#         clippy.state.colors = {}
#
# config = Config()

# def initPost(obj, clippy):
#     clippy.state.output_file_name = "clippy_2.org"
#     clippy.state.efficiency_symbol = "*"
#     clippy.state.max_pad_efficiency = 5
#     clippy.state.max_pad_english = 15
#     clippy.state.colors = {}

# def onTranslateSuggest(obj, clippy):
#     clippy.formatting.org.defaultSuggest(obj, clippy)
#     clippy.formatting.minimalSuggest(obj, clippy)
#     clippy.formatting.retro.suggest(obj, clippy)
#     clippy.formatting.org.debugSuggest(obj, clippy)
#     clippy.formatting.org.minimalSuggest(obj, clippy)
#     clippy.formatting.gruvbox.debugSuggest(obj, clippy)


# def onStrokedPost(obj, clippy):
#     print(f"stroke = {obj.stroke}")


# def onTranslatePre(obj, clippy):
#     print(f"old = {obj.old}")
#     print(f"new = {obj.new}")
#     print(f"translations  = {clippy.engine.translator_state.translations[-10:]}")
    # interesting thing from user 2
    # print(f"Action = {clippy.engine.translator_state.translations[-1].formatting}")


# def startPost(obj, clippy):
#     pass
# some builtin stuff (this is the default so you don't need to set it)
    # clippy.distillations.sources.set(
            #         ["Repeat", {"num": 1}])
    # clippy.formatting.sources.set(
    #         ["Org", {"colorscheme": "gruvbox", "mode": "defaultSuggest"}],
    #         ["Org", {"colorscheme": "gruvbox", "mode": "minimalSuggest"}],
    #         ["Org", {"colorscheme": "gruvbox", "mode": "debugSuggest", "colors": {
    #             "suggestions": "neutral_purple",
    #             "stroked": "neutral_aqua",
    #             "english": "neutral_orange",
    #             "efficiency_symbol": lambda efficiency_symbol: [
    #                 "bright_green", "bright_purple", "bright_blue",
    #                 "bright_orange", "bright_red"
    #                 ][min(len(efficiency_symbol.strip())-1, 4)],
    #             "*": "gray",
    #             ">": "gray",
    #             # "pad_efficiency": background support needed
    #             # "pad_english": background
    #             "source": "gray"
    #             }}],
    #         )
