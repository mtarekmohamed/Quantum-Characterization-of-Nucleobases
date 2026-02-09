 # Quantum Characterization of Nucleobases

This repository contains **quantum mechanical benchmark calculations** of non-covalent interactions between nucleobase fragments, supporting the analysis presented in:

**Quantum Mechanics Characterization of Non-Covalent Interaction in Nucleotide Fragments**  
*Molecules* **2024**, 29, 3258  
DOI: https://doi.org/10.3390/molecules29143258

The calculations focus on **hydrogen-bonding and π–π stacking interactions** in isolated nucleobase pairs, analyzed using **high-level symmetry-adapted perturbation theory (SAPT)** and energy decomposition methods.

---

## Repository Structure and Level of Theory

### `Nucleobases Pair (Interstrand)`
- Nucleobase pairs arranged in **interstrand-like geometries**
- **Distance-dependent interaction scans** over multiple intermolecular spacings
- All spacings computed at the **same level of theory**

**Level of theory:**
- **SAPT2+(3)/dMP2**

---

### `Nucleobases Pair (Intrastrand)`
- Nucleobase pairs arranged in **intrastrand / stacking-like geometries**
- Uses a **different spacing grid** than the interstrand set
- **Same level of theory and basis set** as the Interstrand calculations

**Level of theory:**
- **SAPT2+(3)/dMP2**

---

### `Nucleobases Pair (Sherrill Database Structures)`
- Benchmark geometries taken from established **non-covalent interaction databases**
- Used for **methodological comparison and validation**

**Levels of theory included:**
- SAPT (SAPT0, SAPT2+, SAPT2+(3)/dMP2)
- ALMO Energy Decomposition Analysis (ALMO-EDA)

## File Descriptions

- **`.xyz` files**  
  Cartesian coordinate files defining the **nucleobase fragment geometries** used in the QM calculations. These structures correspond to specific intermolecular orientations and spacings.

- **`.log` files**  
  Raw **quantum chemistry output files**, containing:
  - Total interaction energies  
  - SAPT energy decomposition components  
  - Convergence and computational details  

  These files provide the primary data used for analysis and benchmarking.
---

## Basis Sets Used

As reported in the associated paper, the following **basis sets** were employed to assess basis-set dependence and method accuracy:

- **aug-cc-pVDZ**
- **aug-cc-pVTZ**
- **jun-cc-pVDZ**

**Method × basis usage summary:**
- **SAPT0**: jun-cc-pVDZ, aug-cc-pVDZ, aug-cc-pVTZ  
- **SAPT2+**: aug-cc-pVDZ, aug-cc-pVTZ  
- **SAPT2+(3)/dMP2**: aug-cc-pVDZ, aug-cc-pVTZ  
- **ALMO-EDA**: aug-cc-pVTZ  

The **Interstrand** and **Intrastrand** distance scans use a **fixed level of theory and basis set**, while the **Sherrill Database** folder includes multiple basis sets to highlight method and basis-set sensitivity.

---

## Methods Summary

Interaction energies are decomposed into:
- Electrostatics
- Exchange-repulsion
- Induction (polarization)
- Dispersion

The paper demonstrates that **SAPT2+(3)/dMP2**, combined with sufficiently large augmented basis sets, is required to accurately capture dispersion-dominated nucleobase stacking and polarization effects.

---

## Purpose

This dataset provides:
- **High-accuracy QM benchmarks** for nucleobase interactions
- Reference data for **force-field validation and polarizable model development**
- Reproducible computational support for the conclusions of the associated publication

---

## Citation

If you use this data, please cite:

> *Quantum Mechanics Characterization of Non-Covalent Interaction in Nucleotide Fragments*,  
> Molecules 2024, 29, 3258.  
> https://doi.org/10.3390/molecules29143258

---

