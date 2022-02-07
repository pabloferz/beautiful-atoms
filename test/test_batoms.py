import pytest
from batoms.batom import Batom
from batoms.batoms import Batoms
from batoms.butils import removeAll
import numpy as np

def test_empty():
from batoms.butils import removeAll
from batoms.batoms import Batoms
import numpy as np
removeAll()
h2o = Batoms('h2o')

def test_batoms():
    """
    """
from batoms.butils import removeAll
from batoms.batoms import Batoms
import numpy as np
removeAll()
h2o = Batoms('h2o', species = ['O', 'H', 'H'], 
            positions= [[0, 0, 0.40], [0, -0.76, -0.2], [0, 0.76, -0.2]])

def test_batoms_show():
from ase.build import molecule
from batoms.batoms import Batoms
from batoms.butils import removeAll
removeAll()
c2h6so = molecule('C2H6SO')
c2h6so = Batoms('c2h6so', from_ase = c2h6so)
c2h6so.show = [0, 0 ,0, 0, 0, 1, 1, 1, 1 ,1]

def test_batom():
from batoms.butils import removeAll
from batoms.batoms import Batoms
import numpy as np
removeAll()
h2o = Batoms('h2o', species = ['O', 'H', 'H'], 
            positions= [[0, 0, 0.40], [0, -0.76, -0.2], [0, 0.76, -0.2]])
h2o[1].scale = 1
h2o[1].show = 0
h2o[1].show = 1
h2o[1].species = 'Cl'

def test_batoms_occupy():
from batoms.butils import removeAll
from batoms.batoms import Batoms
import numpy as np
removeAll()
h2o = Batoms('h2o', species = ['O', 'H', 'H'], 
            species_props={'O':{'elements': {'O':0.8, 'N': 0.2}}, 
                           'H':{'elements': {'H': 0.8}}}, 
            positions= [[0, 0, 0.40], [0, -0.76, -0.2], [0, 0.76, -0.2]])


def test_batoms_species():
h2o.species['O'] = {'elements': {'O':0.3, 'Cl':0.3}}

def test_batoms():
    """
    """
from batoms.butils import removeAll
from batoms.batoms import Batoms
import numpy as np
removeAll()
h2o = Batoms('h2o', species = ['O', 'H', 'H'], 
            positions= [[0, 0, 0.40], [0, -0.76, -0.2], [0, 0.76, -0.2]])
# properties
h2o.pbc = True
assert h2o.pbc
h2o.cell = [3, 3, 3]
h2o.repeat([2, 2, 2])
h2o.scale = 0.5
h2o.model_style = 1
assert (h2o.model_style == 1).any()
h2o.translate([0, 0, 2])
assert np.allclose(h2o[0].position, np.array([[0, 0, 2.4]]))
# h2o.rotate(math.pi/2.0, 'Z')
#
def test_batoms_copy():
from batoms.butils import removeAll
from batoms import Batoms
import numpy as np
removeAll()
h2o = Batoms('h2o', species = ['O', 'H', 'H'], 
            positions= [[0, 0, 0.40], [0, -0.76, -0.2], [0, 0.76, -0.2]],
            pbc = True,
            cell = [3, 3, 3])
h2o_2 = h2o.copy('h2o_2')
# assert isinstance(h2o_2, Batoms)
h2o_2 = Batom('h2o_2')
#
# delete
del h2o_2['h2o_2_atom_H'][[0]]
assert len(h2o_2['h2o_2_atom_H']) == 1

#
def test_replace():
from batoms.butils import removeAll
from batoms.batoms import Batoms
import numpy as np
removeAll()
h2o = Batoms('h2o', species = ['O', 'H', 'H'], 
            positions= [[0, 0, 0.40], [0, -0.76, -0.2], [0, 0.76, -0.2]])
h2o.translate([2, 2, 2])
h2o.cell = [5, 5, 5]
h2o.pbc = True
h2o.replace(0, 'C')
h2o.model_style = 1

def test_pbc():
from batoms.batoms import Batoms
from ase.build import molecule
from batoms.butils import removeAll
removeAll()
h2o = molecule('H2O')
h2o.pbc = True
h2o.center(3)
# h2o = h2o*[20, 20, 20]
h2o = Batoms('h2o', from_ase=h2o)

def test_batoms():
    """
    """

assert isinstance(h2o, Batom)
assert len(h2o.species) == 2
assert len(h2o) == 3

def test_from_batom():
from batoms.batom import Batom
from batoms.batoms import Batoms
from batoms.butils import removeAll
removeAll()
h = Batom(name = 'atom_H', species = 'H', positions = [[0, -0.76, -0.2], [0, 0.76, -0.2]])
h1 = Batom(name = 'atom_H_1', species = 'H', positions = [[1, -0.76, -0.2], [1, 0.76, -0.2]])
o = Batom(name = 'atom_O', species = 'O', positions = [[0, 0, 0.40]])
h2o = Batoms('h2o', [h, o, h1])
assert isinstance(h2o, Batoms)
assert len(h2o.species) == 2
assert len(h2o) == 5


def test_from_batoms():
from batoms.butils import removeAll
from batoms import Batoms
removeAll()
h2o = Batoms('h2o', species = ['O', 'H', 'H'], 
            species_props={'O':{'elements': {'O':0.8, 'N': 0.2}}, 
                           'H':{'elements': {'H': 0.8}}}, 
            positions= [[0, 0, 0.40], [0, -0.76, -0.2], [0, 0.76, -0.2]])
test = Batoms(load = 'h2o')
assert isinstance(h2o, Batoms)
assert len(h2o.species) == 2
assert len(h2o) == 3
h2o.translate([2, 0, 0])

def test_batoms_metaball():
    """
    """
    from batoms.butils import removeAll
    from batoms import Batoms
    removeAll()
    h2o = Batoms('h2o', {'O': [[5, 0, 0.40]], 
                        'H': [[5, -0.76, -0.2], [5, 0.76, -0.2]]},
                    shape = 3)

def test_render():
    from batoms.butils import removeAll
    from batoms import Batoms
    removeAll()
    h2o = Batoms('h2o', {'O': [[0, 0, 0.40]], 'H': [[0, -0.76, -0.2], [0, 0.76, -0.2]]})
    h2o.get_image(output = 'batoms_render.png')
    h2o.get_image(viewport = [1, 0, 0], output = 'batoms_render_viewport.png')
    h2o.get_image(canvas=[5, 5, 5], output = 'batoms_render.png_canvas')

def test_ase_arrays():
from batoms.butils import removeAll
from batoms import Batoms
from batoms.pdbparser import read_pdb
removeAll()
atoms = read_pdb('test/datas/1tim.pdb')
p1tim = Batoms('p1tim', aseAtoms = atoms)
p1tim.attributes
p1tim.atoms

def test_set_arrays():
from batoms.batoms import Batoms
from ase.build import molecule
from batoms.butils import removeAll
removeAll()
mol = molecule('H2O')
h2o = Batoms('h2o', atoms = mol)
h2o.pbc = True
h2o.cell = [3, 3, 3]
h2o = h2o*[2, 1, 1]
print(h2o.arrays)
del h2o[[2]]
print(h2o.arrays)
h2o.set_arrays({'positions': h2o.arrays['positions'] + 5})
print(h2o.positions)


def test_ase_sort():
from batoms.butils import removeAll
from batoms import Batoms
from ase.build import molecule
removeAll()
mol = molecule('C2H6SO')
mol.get_chemical_symbols()
c2h6so = Batoms('c2h6so', atoms = mol)
c2h6so.arrays['elements']

def test_ase_species():
from batoms.butils import removeAll
from ase.build import molecule, bulk
from batoms import Batoms
import numpy as np
removeAll()
h2o = molecule('H2O')
h2o.new_array('species', np.array(h2o.get_chemical_symbols(), dtype = 'U20'))
h2o.arrays['species'][1] = 'H_1'
h2o.arrays['species'][2] = 'H_test2'
h2o = Batoms('h2o', atoms = h2o)
species = h2o.species
species.sort()
assert species == ['H_1', 'H_test2', 'O']
# bulk
fe = bulk('Fe')
fe = Batoms(label = 'fe', atoms=fe)
assert fe.pbc == [True, True, True]


def test_pymatgen_species():
from batoms.butils import removeAll
from batoms import Batoms
from pymatgen.core import Lattice, Structure
from pymatgen.core.structure import Molecule
removeAll()
# molecule
co = Molecule(["C","O"], [[0.0, 0.0, 0.0], [0.0, 0.0, 1.2]])
co = Batoms(label = 'co', atoms=co)
# lattice
fe = Structure(Lattice.cubic(2.8), ["Fe", "Fe"], [[0, 0, 0], [0.5, 0.5, 0.5]])
fe = Batoms(label = 'fe', atoms=fe)
assert fe.pbc == [True, True, True]

def test_occupancy():
    """
    """
from batoms.butils import removeAll
from batoms import Batoms
removeAll()
from ase.build import bulk
au = bulk('Au', cubic = True)
au = Batoms('au', atoms = au)
au['atom_Au'].elements = {'Au':0.75, 'Ag': 0.25}
assert len(au['atom_Au'].elements) == 2
au.draw_cell()
au.get_image(output = 'batoms_occupancy')

def test_get_and_set_positions():
from batoms.butils import removeAll
from batoms import Batoms
from ase.build import molecule
import numpy as np
removeAll()
h2o = Batoms('h2o', {'O': [[0, 0, 0.40]], 'H': [[0, -0.76, -0.2], [0, 0.76, -0.2]]})
positions = h2o.positions
mol = molecule('H2O')
mol.positions[:, 2] += 5
h2o.positions = mol.positions
assert np.isclose(h2o.positions[0, 2], 5.11926)

def test_extend():
from batoms import Batoms
from ase.build import molecule
from batoms.butils import removeAll
removeAll()
h2o = Batoms('h2o', species = ['O', 'H', 'H'], positions= [[0, 0, 0.40], [0, -0.76, -0.2], [0, 0.76, -0.2]])
co = Batoms('co', species = ['C', 'O'], positions= [[1, 0, 0], [2.3, 0, 0]])
h2o.extend(co)
assert len(h2o.species) == 3
assert len(h2o) == 5

def test_transform():
from batoms import Batoms
from batoms.butils import removeAll
from batoms.bio import read
removeAll()
tio2 = read('test/datas/tio2.cif')
# tio2.model_style = 2
tio2_t = tio2.transform([[1, 1, 0, 0], [-1, 1, 0, 0], [0, 0, 1, 0]])
assert len(tio2_t) == 12

def test_repeat():
from batoms import Batoms
from ase.build import molecule
from batoms.butils import removeAll
removeAll()
h2o = molecule('H2O')
h2o = Batoms(label = 'h2o', atoms = h2o)
h2o.cell = [3, 3, 3]
h2o.pbc = True
h2o.repeat([2, 2, 2])
h2o.model_style = 1
assert len(h2o) == 24
h2o.arrays

def test_repeat_animation():
from batoms import Batoms
from batoms.butils import removeAll
from batoms.bio import read
removeAll()
tio2 = read('test/datas/tio2_10.xyz', index = ':')
tio2.set_frames()
tio2.model_style = 1
tio2.repeat([2, 2, 2])
tio2.model_style = 1
assert len(tio2) == 48


def test_boundary():
from batoms.bio import read
from batoms.butils import removeAll
removeAll()
mof = read('datas/mof-5.cif')
mof.boundary = 0.01
mof.boundary = 1

def test_cavity():
    from batoms.bio import read
    from batoms.butils import removeAll
    removeAll()
    mof = read('datas/mof-5.cif')
    mof.draw_cavity_sphere(9.0, boundary = [[0.2, 0.8], [0.2, 0.8], [0.2, 0.8]])
    mof.model_style = 2
    mof.draw_cell()


def test_get_geometry():
    from ase.build import molecule
    from batoms.butils import removeAll
    removeAll()
    atoms = molecule('H2O')
    h2o = Batoms(atoms = atoms, label = 'h2o')
    angle = h2o.get_angle('H', 0, 'O', 0, 'H', 1)
    d = h2o.get_distances('H', 0, 'H', 1)
    com = h2o.get_center_of_mass()
    cog = h2o.get_center_of_geometry()

def test_make_real():
    from ase.build import molecule
    from batoms.butils import removeAll
    removeAll()
    atoms = molecule('H2O')
    h2o = Batoms(atoms = atoms, label = 'h2o')
    h2o.make_real()

if __name__ == '__main__':
    test_from_batom()
    test_batoms()
    test_from_coll()
    test_ase_arrays()
    test_ase_species()
    test_pymatgen_species()
    test_occupancy()
    test_get_and_set_positions()
    test_cavity()
    test_get_geometry()
    test_repeat()
    test_repeat_animation()
    print('\n Batoms: All pass! \n')