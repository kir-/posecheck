from posecheck import PoseCheck
from rdkit import Chem

smiles = 'c1([CH:14]2[CH2:13][CH:12]([NH2:17])[CH2:16][N:15]2[C:20]([NH2:19])=[O:21])[c:1]([CH2:24][NH2:25])[c:2]([CH:22]=[CH2:23])[n:3][c:4](-[c:6]2[c:7]([F:18])[cH:8][n:9][cH:10][cH:11]2)[cH:5]1'
# Initialize the PoseCheck object
pc = PoseCheck()

# Load a protein from a PDB file (will run reduce in the background)
pc.load_protein_from_pdb("data/examples/1a2g.pdb")

# Load ligands from an SDF file
# pc.load_ligands_from_sdf("data/examples/1a2g_ligand.sdf")
# Alternatively, load RDKit molecules directly
rdmol = Chem.MolFromSmiles(smiles)
pc.load_ligands_from_mol(rdmol)

# Check for interactions
interactions = pc.calculate_interactions()
print(f"Interactions of example molecule: {interactions}")