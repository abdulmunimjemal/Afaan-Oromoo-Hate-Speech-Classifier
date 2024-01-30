class StopwordRemover:
    DEFAULT_STOPWORDS = {
        'aanee', 'agarsiisoo', 'akka', 'akki',  'akkam', 'akkasumas', 'akkum', 'akkuma', 'ala', 'ala', 'alatti', 'alatti', 'alla', 'amma', 'amma', 'ammo', 'ammoo', 'an', 'an', 'ana', 'anee', 'ani', 'ani', 'ati', 'bira', 'bira', 'booda', 'booddee', 'dabalatees', 'dhaan', 'dudduuba', 'dugda', 'dura', 'duuba', 'duuba', 'eega', 'eegana', 'Eegasii', 'ennaa', 'erga', 'ergii', 'f', 'faallaa', 'fagaatee', 'fi', 'fi', 'fullee', 'fuullee', 'gajjallaa', 'gama', 'gama', 'gararraa', 'garas', 'garuu', 'giddu', 'gidduu', 'gidduu', 'gubbaa', 'gubbaa', 'ha', 'hamma', 'hanga', 'henna', 'hoggaa', 'hogguu', 'hoo', 'illee', 'immoo', 'inin', 'innaa', 'inni', 'Inni', 'irra', 'Irra', 'irraa', 'irraan', 'isa', 'Isaa', 'isaaf', 'Isaaf', 'isaan', 'isaani', 'isaanii', 'isaaniitiin', 'isaanirraa', 'Isaanirraa', 'isaanitti', 'isaatiin', 'isarraa', 'isatti', 'Isatti', 'isee', 'Iseen', 'ishee', 'ishii', 'Ishii', 'ishiif', 'Ishiif', 'ishiin', 'ishiirraa', 'Ishiirraa', 'ishiitti', 'isii', 'Isii', 'isiin', 'Isiin', 'isin', 'Isin', 'isini', 'isinii', 'isiniif', 'isiniin', 'isinirraa', 'isinitti', 'ittaanee', 'itti', 'Itti', 'Ittuu', 'itumallee', 'ituu', 'ituullee', 'jala', 'Jala', 'jara', 'Jara', 'jechaan', 'jechoota', 'jechuu', 'jechuun', 'kan', 'Kan', 'kana', 'Kana', 'kanaa', 'kanaaf', 'kanaafi', 'Kanaafuu', 'kanaan', 'kanaatti', 'karaa', 'Kee', 'keenna', 'Keenna', 'keenya', 'Keenya', 'keessa', 'Keessa', 'keessan', 'Keessan', 'keessatti', 'Keessatti', 'Kiyya', 'Koo', 'Kun', 'lafa', 'lama', 'Malee', 'manna', 'maqaa', 'moo', 'na', 'Na', 'naa', 'naaf', 'Naaf', 'naan', 'naannoo', 'narraa', 'Narraa', 'natti', 'Natti', 'nu', 'Nu', 'nuhi', 'nurraa', 'Nurraa', 'nuti', 'Nuti', 'nutti', 'nuu', 'nuuf', 'nuun', 'nuy', 'odoo', 'ofii', 'oggaa', 'oo', 'osoo', 'otoo', 'otumallee', 'otuu', 'otuullee', 'saaniif', 'sadii', 'sana', 'Sana', 'saniif', 'si', 'sii', 'siif', 'siin', 'Siin', 'Silaa', 'simmoo', 'sinitti', 'siqee', 'sirraa', 'sitti', 'Sitti', 'Sun', 'Ta‟ullee', 'tahullee', 'tahullee', 'tahuyyu', 'tahuyyuu', 'tana', 'Tanaaf', 'tanaafi', 'Tanaafuu', 'tawullee', 'teenya', 'Teenya', 'teessan', 'tiyya', 'too', 'tti', 'Tun', 'Utuu', 'waahee', 'waan', 'Waan', 'waggaa', 'wajjin', 'warra', 'Warra', 'woo', 'yammuu', 'yemmuu', 'Yeroo', 'yommii', 'Yommuu', 'Yoo', 'yookaan', 'Yookaan', 'yookiin', 'yoolinimoo', 'Yoom'
        'agarsiisa', 'mulhisa', 'ni', 'hin', 'haa', 'jiru', 'irratti','ture', 'gaafa','oromoo','amaaraa','jedhee','nama','waliin','taanee','mitii','abiy','wal', 'h', 'jedhu', 'jedhe', 'tokkoo', 'tokko', 'tae', 'keessaa', 'bakka', 'yaa', 'gabaase', 'beeksiseera', 'yaadatama', 'Feesbuukii', 'Feesbuukii', 'odeeffannoo', 'subiskiraayib', 'godha', 'godhaa', 'hordofaa', 'mulhisa', 'hi'
    }

    def __init__(self, stopwords=None):
        
        if stopwords is None or len(stopwords) == 0:
            stopwords = self.DEFAULT_STOPWORDS
        self.stopwords = {stopword.lower() for stopword in stopwords}
        

    def remove_stopwords(self, tokens: iter) -> list:
        filtered_tokens = [
            token for token in tokens if token.lower() not in self.stopwords
            ]
        
        return filtered_tokens


def main():
    # Example usage without providing custom stopwords (uses default stopwords)
    tokens = "mana hidhaa kana keessatti akki nuti itti qabu".split()
    stopword_remover_default = StopwordRemover()
    filtered_tokens_default = stopword_remover_default.remove_stopwords(tokens)
    print(filtered_tokens_default)

    # Example usage with custom stopwords
    custom_stopwords = {"nuti"}
    stopword_remover_custom = StopwordRemover(custom_stopwords)
    filtered_tokens_custom = stopword_remover_custom.remove_stopwords(tokens)
    print(filtered_tokens_custom)

if __name__ == "__main__":
    main()