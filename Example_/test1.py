import main
domain_animal = main.Domain("Animalia")

kingdom_chordata = main.Kingdom("Chordata")
domain_animal.kingdoms.append(kingdom_chordata)

phylum_aves = main.Phylum("Aves")
kingdom_chordata.phyla.append(phylum_aves)

class_passeriformes = main.AnimalClass("Passeriformes")
phylum_aves.classes.append(class_passeriformes)

order_coraciiformes = main.Order("Coraciiformes")
class_passeriformes.orders.append(order_coraciiformes)

family_corvidae = main.Family("Corvidae")
order_coraciiformes.families.append(family_corvidae)

genus_pica = main.Genus("Pica")
family_corvidae.genera.append(genus_pica)

species_eurasian_magpie = main.Species("Eurasian Magpie", 250, genus_pica, 60, 20)
genus_pica.species.append(species_eurasian_magpie)

species_eurasian_magpie.add_property("Habitat", "Woodlands")
species_eurasian_magpie.add_property("Diet", "Omnivorous")
species_eurasian_magpie.add_property("Conservation Status", "Least Concern")

animal_encyclopedia = main.AnimalEncyclopedia()
animal_encyclopedia.add_domain(domain_animal)

with open("animal_data.txt", "w") as file:
    file.write("Animal Encyclopedia\n\n")
    file.write("Domain: " + domain_animal.name + "\n")
    file.write("Kingdom: " + kingdom_chordata.name + "\n")
    file.write("Phylum: " + phylum_aves.name + "\n")
    file.write("Class: " + class_passeriformes.name + "\n")
    file.write("Order: " + order_coraciiformes.name + "\n")
    file.write("Family: " + family_corvidae.name + "\n")
    file.write("Genus: " + genus_pica.name + "\n")
    file.write("Species: " + species_eurasian_magpie.name + "\n\n")
    file.write("Additional Properties:\n")
    for property_name, property_value in species_eurasian_magpie.additional_properties.items():
        file.write("- " + property_name + ": " + str(property_value) + "\n")

