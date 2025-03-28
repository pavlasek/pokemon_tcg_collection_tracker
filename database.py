"""database mock object"""
import csv

class PokemonDatabase:

    def __init__(self, path):
        self.elite_trainer_boxes_file = "{path}/elite_trainer_boxes.csv".format(path)
        self.booster_boxes_file = "{path}/booster_boxes.csv".format(path)

        elite_trainer_boxes = self.create_elite_trainer_boxes_dict(self.elite_trainer_boxes_file)
        booster_boxes = self.create_booster_boxes_dict(self.booster_boxes_file)


    def create_elite_trainer_boxes_dict(self, etb_file):
        pass

    def create_booster_boxes_dict(self, bb_file):

        pass

    def show_all_products(self):
        print(">> ALL OF THE SEALED PRODUCTS <<")
        self.show_booster_boxes(self)
        self.show_elite_trainer_boxes(self)
        pass

    def show_elite_trainer_boxes(self):
        print("ALL OF THE ETBs:")
        pass

    def show_booster_boxes(self):
        print("ALL OF THE BBs:")
        pass

