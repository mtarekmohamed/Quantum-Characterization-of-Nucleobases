import numpy as np
import sys


def read_xyz(file_path):
    """
    Read XYZ file and return atom coordinates.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
        num_atoms = int(lines[0])
        atom_lines = lines[2:]
        
        coordinates = []
        atom_types = []
        for line in atom_lines:
            parts = line.split()
            atom_types.append(parts[0])
            coordinates.append([float(parts[1]), float(parts[2]), float(parts[3])])

        return np.array(coordinates), atom_types

def write_xyz(file_path, coordinates, atom_types):
    """
    Write atom coordinates to XYZ file.
    """
    num_atoms = len(coordinates)
    with open(file_path, 'w') as file:
        file.write(str(num_atoms) + '\n')
        file.write('\n')
        for i in range(num_atoms):
            file.write(f'{atom_types[i]} {coordinates[i][0]} {coordinates[i][1]} {coordinates[i][2]}\n')

def calculate_distance(coord1, coord2):
    """
    Calculate the Euclidean distance between two sets of coordinates.
    """
    return np.linalg.norm(coord1 - coord2)

def translate_structure(coordinates, translation_vector):
    """
    Translate a structure by a given vector.
    """
    return coordinates + translation_vector

def main(file_path, percent_translation):
    # Read XYZ file
    coordinates, atom_types = read_xyz(file_path)

    # Split the coordinates into two molecules
    coordinates1 = coordinates[0:12]
    coordinates2 = coordinates[12:]

    # Calculate the distance between the centers of mass of the two molecules
    center_of_mass1 = np.mean(coordinates1, axis=0)
    center_of_mass2 = np.mean(coordinates2, axis=0)
    distance = calculate_distance(center_of_mass1, center_of_mass2)
    print(distance)

    # Translate the second molecule by a certain percentage of the calculated distance
    translation_vector = (center_of_mass2 - center_of_mass1) * (percent_translation / 100)
    translated_coordinates2 = translate_structure(coordinates2, translation_vector)

    # Combine the translated molecule with the original coordinates of the first molecule
    translated_coordinates = np.concatenate([coordinates1, translated_coordinates2], axis=0)

    # Write the translated structure to a new XYZ file
    output_filename = "trial.xyz"
    write_xyz(output_filename, translated_coordinates, atom_types)

    print(f"Translation completed. Translated structure saved to {output_filename}")

if __name__ == "__main__":
    xyz_file = "U-U_optimized.xyz"
    percent_translation = -5  # Adjust as needed

    main(xyz_file, percent_translation)

