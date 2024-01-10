from posecheck import PoseCheck

# Initialize the PoseCheck object
pc = PoseCheck()

# Load a protein from a PDB file (will run reduce in the background)
pc.load_protein_from_pdb("data/examples/1a2g.pdb")

# Load ligands from an SDF file
pc.load_ligands_from_sdf("data/examples/1a2g_ligand.sdf")
# Alternatively, load RDKit molecules directly
# pc.load_ligands_from_mol(rdmol)

# Check for clashes
clashes = pc.calculate_clashes()
print(f"Number of clashes in example molecule: {clashes[0]}")

# Check for strain
strain = pc.calculate_strain_energy()
print(f"Strain energ of example moleculey: {strain[0]}")

# Check for interactions
interactions = pc.calculate_interactions()
print(f"Interactions of example molecule: {interactions}")