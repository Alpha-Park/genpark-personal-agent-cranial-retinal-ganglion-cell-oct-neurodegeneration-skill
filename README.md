# genpark-personal-agent-cranial-retinal-ganglion-cell-oct-neurodegeneration-skill

[![GenPark AI](https://img.shields.io/badge/GenPark-AI%20Ecosystem-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0077b5)](https://www.linkedin.com/company/92955550)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](https://www.python.org/)

Optical Coherence Tomography (OCT) ganglion cell-inner plexiform layer (GCIPL) thinning rate & preclinical neurodegeneration sentinel.

## Overview

Part of the **GenPark Industrial Multi-Agent Skill Matrix**. Zero external pip dependencies; built purely with standard Python library modules for instant deterministic orchestration.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## Tool Specification

- **Tool Name**: `audit_oct_gcipl_neurodegeneration`
- **Category**: `personal_agent`

### Method Documentation
Audit central nervous system neuroaxonal loss via Spectral-Domain OCT measurement of macula Ganglion Cell-Inner Plexiform Layer (GCIPL) thickness (um).
The retina is an unmyelinated embryological extension of the diencephalon; GCIPL thinning precedes hippocampal atrophy in Alzheimer's and Parkinson's.
Calculates annualized atrophy velocity (um/yr) vs normative aging loss (0.25-0.35 um/yr).

## JSON-RPC 2.0 Integration

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "audit_oct_gcipl_neurodegeneration",
    "arguments": {
    "mean_gcipl_thickness_um": 72.4,
    "baseline_gcipl_thickness_um": 74.5,
    "interval_years": 2.5,
    "age_years": 62
}
  }
}
```

## Running Self Tests

```bash
python skills.py --test
```
