from enum import Enum


class CorpusType(Enum):
    """
    Enum class representing the available corpora in the ORACC project.
    """

    ED12 = "ed12"
    ED3A = "ed3a"
    ED3B = "ed3b"
    EBLA = "ebla"
    OAKK = "oakk"
    UR3 = "ur3"
    LAGASH2 = "lagash2"
    OLDBAB = "oldbab"
    EARLYLIT = "earlylit"
    LITERARY = "literary"
    ROYAL = "royal"
    PRAXIS = "praxis"
    PRAXIS_UDUGHUL = "praxis_udughul"
    PRAXIS_VARIA = "praxis_varia"

    def get_download_url(self):
        """
        Returns the download URL for the given corpus.

        Raises:
          ValueError: If the corpus is invalid.
        """
        if self is CorpusType.ED12:
            return "http://oracc.museum.upenn.edu/json/epsd2-admin-ed12.zip"
        elif self is CorpusType.ED3A:
            return "http://oracc.museum.upenn.edu/json/epsd2-admin-ed3a.zip"
        elif self is CorpusType.ED3B:
            return "http://oracc.museum.upenn.edu/json/epsd2-admin-ed3b.zip"
        elif self is CorpusType.EBLA:
            return "http://oracc.museum.upenn.edu/json/epsd2-admin-ebla.zip"
        elif self is CorpusType.OAKK:
            return "http://oracc.museum.upenn.edu/json/epsd2-admin-oakk.zip"
        elif self is CorpusType.UR3:
            return "http://oracc.museum.upenn.edu/json/epsd2-admin-ur3.zip"
        elif self is CorpusType.LAGASH2:
            return "http://oracc.museum.upenn.edu/json/epsd2-admin-lagash2.zip"
        elif self is CorpusType.OLDBAB:
            return "http://oracc.museum.upenn.edu/json/epsd2-admin/oldbab.zip"
        elif self is CorpusType.EARLYLIT:
            return "http://oracc.museum.upenn.edu/json/epsd2-earlylit.zip"
        elif self is CorpusType.LITERARY:
            return "http://oracc.museum.upenn.edu/json/epsd2-literary.zip"
        elif self is CorpusType.ROYAL:
            return "http://oracc.museum.upenn.edu/json/epsd2-royal.zip"
        elif self is CorpusType.PRAXIS:
            return "http://oracc.museum.upenn.edu/json/epsd2-praxis.zip"
        elif self is CorpusType.PRAXIS_UDUGHUL:
            return "http://oracc.museum.upenn.edu/json/epsd2-praxis-udughul.zip"
        elif self is CorpusType.PRAXIS_VARIA:
            return "http://oracc.museum.upenn.edu/json/epsd2-praxis-varia.zip"
        else:
            raise ValueError("Invalid corpus")
