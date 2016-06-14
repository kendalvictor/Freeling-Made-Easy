
class Options:

    def __init__(self, output_type, language, numr, dtr, qrp, ner, nec, mwd, phe):
        """
        :param output_type: string "tagging" or "morfo"
        :param language: string "en" - for english or "es" - for spanish
        :param numr:
        :param dtr:
        :param qrp:
        :param ner:
        :param nec:
        :param mwd:
        :param phe:
        """
        self.output_type = output_type
        self.language = language
        self.numr = numr
        self.dtr = dtr
        self.qrp = qrp
        self.ner = ner
        self.nec = nec
        self.mwd = mwd
        self.phe = phe
