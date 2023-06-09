class Animal:
    def __init__(self, name, weight, parent_group, height, lifespan):
        self.name = name
        self.weight = weight
        self.parent_group = parent_group
        self.height = height
        self.lifespan = lifespan
        self.additional_properties = {}

    def add_property(self, property_name, property_value):
        self.additional_properties[property_name] = property_value

    def remove_property(self, property_name):
        if property_name in self.additional_properties:
            del self.additional_properties[property_name]

    def search_by_property(self, property_name, value):
        if property_name in self.additional_properties:
            if isinstance(value, (int, float)):
                if isinstance(self.additional_properties[property_name], (int, float)):
                    return self.additional_properties[property_name] == value
                elif isinstance(self.additional_properties[property_name], str):
                    return False  # Property is of type string, cannot compare with numeric value
            elif isinstance(value, str):
                if isinstance(self.additional_properties[property_name], str):
                    return value in self.additional_properties[property_name]
                elif isinstance(self.additional_properties[property_name], (int, float)):
                    return False  # Property is of numeric type, cannot search with string value
        return False  # Property not found or incompatible types

    def print_group_hierarchy(self, indent=0):
        print(" " * indent + self.name)
        for subgroup in self.subgroups:
            subgroup.print_group_hierarchy(indent + 4)


class Species(Animal):
    def __init__(self, name, weight, parent_group, height, lifespan):
        super().__init__(name, weight, parent_group, height, lifespan)
        self.subgroups = []

    def add_subgroup(self, subgroup):
        self.subgroups.append(subgroup)

    def remove_subgroup(self, subgroup):
        if subgroup in self.subgroups:
            self.subgroups.remove(subgroup)

    def print_group_hierarchy(self, indent=0):
        print(" " * indent + self.name)
        for subgroup in self.subgroups:
            subgroup.print_group_hierarchy(indent + 4)


class AnimalEncyclopedia:
    def __init__(self):
        self.domains = []

    def add_domain(self, domain):
        self.domains.append(domain)

    def remove_domain(self, domain):
        if domain in self.domains:
            self.domains.remove(domain)

    def search_species_by_weight(self, weight):
        result = []
        for domain in self.domains:
            for kingdom in domain.kingdoms:
                for phylum in kingdom.phyla:
                    for animal_class in phylum.classes:
                        for order in animal_class.orders:
                            for family in order.families:
                                for genus in family.genera:
                                    for species in genus.species:
                                        if species.weight == weight:
                                            result.append(species)
        return result

    def search_species_by_lifespan(self, lifespan):
        result = []
        for domain in self.domains:
            for kingdom in domain.kingdoms:
                for phylum in kingdom.phyla:
                    for animal_class in phylum.classes:
                        for order in animal_class.orders:
                            for family in order.families:
                                for genus in family.genera:
                                    for species in genus.species:
                                        if species.lifespan == lifespan:
                                            result.append(species)
        return result

    def print_species_hierarchy(self, species_name, indent=0):
        for domain in self.domains:
            for kingdom in domain.kingdoms:
                for phylum in kingdom.phyla:
                    for animal_class in phylum.classes:
                        for order in animal_class.orders:
                            for family in order.families:
                                for genus in family.genera:
                                    for species in genus.species:
                                        if species.name == species_name:
                                            print(" " * indent + species.name)
                                            return


class Domain:
    def __init__(self, name):
        self.name = name
        self.kingdoms = []


class Kingdom:
    def __init__(self, name):
        self.name = name
        self.phyla = []


class Phylum:
    def __init__(self, name):
        self.name = name
        self.classes = []


class AnimalClass:
    def __init__(self, name):
        self.name = name
        self.orders = []


class Order:
    def __init__(self, name):
        self.name = name
        self.families = []


class Family:
    def __init__(self, name):
        self.name = name
        self.genera = []


class Genus:
    def __init__(self, name):
        self.name = name
        self.species = []


class Species:
    def __init__(self, name, weight, parent_group, height, lifespan):
        self.name = name
        self.weight = weight
        self.parent_group = parent_group
        self.height = height
        self.lifespan = lifespan