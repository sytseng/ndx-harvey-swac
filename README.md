# ndx-harvey-swac Extension for NWB

This is a Neurodata Extension (NDX) for Neurodata Without Borders: Neurophysiology (NWB:N) 2.0 for reading lab metadata in the DANDI dataset of the SWAC project in Harvey Lab, Harvard Medical School.

Link to the DANDI dataset:

To be added

Reference:

Tseng, S.-Y., Chettih, S.N., Arlt, C., Barroso-Luque, R., and Harvey, C.D. (2022). Shared and specialized coding across posterior cortical areas for dynamic navigation decisions. Neuron 110, 2484–2502.e16. [[link]](https://www.sciencedirect.com/science/article/pii/S0896627322004536) 

## Installation

```
pip install git+https://github.com/sytseng/ndx-harvey-swac.git
```

## Usage

There are two extnesion to the `LabMetaData` type. The `LabMetaDataSession` is for reading metadata in the NWB files for individual imaging sessions. Load the class before reading the NWB file:
```python
from ndx_harvey_swac import LabMetaDataSession
```
The `LabMetaDataSession` contains information about the task parameters (`TaskParam`), AAVretro injection sites (`AAVretroInjSite`), imaging setup (`Imaging`) and FOV registration (`Registration`).



The other type of extension, the `LabMetaDataMouse`, is for reading metadata in the NWB files for individual mice that contain the widefield retinotopy and vessel image of the cranial window under two photon microscope. Load the class before reading the NWB file:
```python
from ndx_harvey_swac import LabMetaDataMouse
```
The `LabMetaDataSession` contains information about the registration parameters (`Registration`) for aligning widefield data and two-photon cranial window vessel image to Allen Mouse Common Coordinate Framework (CCF).


---
This extension was created using [ndx-template](https://github.com/nwb-extensions/ndx-template).
