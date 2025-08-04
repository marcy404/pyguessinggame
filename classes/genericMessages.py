class Messages:
    @staticmethod
    def separator(char:str="-", times:int=10)->str:
        sep = char * times
        return sep

    @staticmethod
    def banner(title:str)->str:
        bannerSep = Messages.separator(times=len(title) + 2)
        banner = f"{bannerSep}\n {title}\n{bannerSep}"
        return banner