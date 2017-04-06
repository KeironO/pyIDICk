import json, numpy as np

class Element(object):
    with open("./data/periodic_table.json") as pt_file:
        periodic_table = json.load(pt_file)

    def __init__(self, symbol, count):
        self.symbol = symbol
        self.count = count
        self.atomic_weight = self._get_atomic_weight(symbol)
        self.isotopic_weights = self._get_isotopic_weight(symbol)
        self.atomic_charge = self._get_atomic_charge(symbol)
        self.ratios = self._get_ratios(symbol)

    def calculate_weight(self):
        return self.atomic_weight * float(self.count)

    def _get_ratios(self, symbol):
        return self.periodic_table[symbol]["isotopic_ratio"]

    def _get_atomic_charge(self, symbol):
        return self.periodic_table[symbol]["atomic_charge"]

    def _get_atomic_weight(self, symbol):
        isotopic_weight = self._get_isotopic_weight(symbol)
        ratios = self.periodic_table[symbol]["isotopic_ratio"]
        return float(np.matrix(ratios) * np.transpose(np.matrix(isotopic_weight)))

    def _get_isotopic_weight(self, symbol):
        return self.periodic_table[symbol]["isotopic_weight"]


    def remove_element(self, count):
        self.count -= count

    def add_element(self, count):
        self.count += count