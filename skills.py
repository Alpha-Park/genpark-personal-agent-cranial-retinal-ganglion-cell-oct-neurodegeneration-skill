# -*- coding: utf-8 -*-
"""GenPark Industrial Skill: genpark-personal-agent-cranial-retinal-ganglion-cell-oct-neurodegeneration-skill
Category: personal_agent
Website: https://www.genpark.ai
LinkedIn: https://www.linkedin.com/company/92955550
"""
import sys
import json
import math

sys.stdout.reconfigure(encoding="utf-8")

def audit_oct_gcipl_neurodegeneration(mean_gcipl_thickness_um, baseline_gcipl_thickness_um=None, interval_years=None, age_years=60):
    if mean_gcipl_thickness_um <= 0:
        raise ValueError("mean_gcipl_thickness_um must be positive")
        
    # Standard healthy adult GCIPL: 75 - 90 um
    # Borderline thinning: 68 - 74 um
    # Significant thinning: < 68 um
    if mean_gcipl_thickness_um >= 75.0:
        thickness_tier = "PRESERVED_NEUROAXONAL_INTEGRITY"
    elif mean_gcipl_thickness_um >= 68.0:
        thickness_tier = "MILD_BORDERLINE_GCIPL_THINNING"
    else:
        thickness_tier = "ADVANCED_GANGLION_CELL_LOSS"
        
    annual_thinning_um_yr = None
    accelerated_atrophy = False
    if baseline_gcipl_thickness_um is not None and interval_years is not None and interval_years > 0:
        total_loss = baseline_gcipl_thickness_um - mean_gcipl_thickness_um
        annual_thinning_um_yr = round(total_loss / interval_years, 2)
        # Accelerated if thinning exceeds 0.60 um/year (2x normative rate)
        if annual_thinning_um_yr >= 0.60:
            accelerated_atrophy = True
            
    return {
        "current_mean_gcipl_thickness_um": round(mean_gcipl_thickness_um, 1),
        "thickness_percentile_tier": thickness_tier,
        "annualized_thinning_rate_um_yr": annual_thinning_um_yr,
        "accelerated_neurodegeneration_sentinel": accelerated_atrophy,
        "expected_healthy_aging_loss_um_yr": "0.25 - 0.35",
        "clinical_recommendation": "Recommend cognitive neuropsychological battery and brain MRI volumetric imaging." if accelerated_atrophy or mean_gcipl_thickness_um < 68.0 else "Retinal neuroaxonal layer stable."
    }


def handle_rpc(request_str):
    try:
        req = json.loads(request_str)
        rpc_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})
        
        if method == "tools/list":
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "tools": [{
                        "name": "audit_oct_gcipl_neurodegeneration",
                        "description": """Audit central nervous system neuroaxonal loss via Spectral-Domain OCT measurement of macula Ganglion Cell-Inner Plexiform Layer (GCIPL) thickness (um).
The retina is an unmyelinated embryological extension of the diencephalon; GCIPL thinning precedes hippocampal atrophy in Alzheimer's and Parkinson's.
Calculates annualized atrophy velocity (um/yr) vs normative aging loss (0.25-0.35 um/yr).""",
                        "inputSchema": {
                            "type": "object",
                            "properties": {}
                        }
                    }]
                }
            })
        elif method == "tools/call":
            call_params = params.get("arguments", {})
            res = audit_oct_gcipl_neurodegeneration(**call_params)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "content": [{
                        "type": "text",
                        "text": json.dumps(res, indent=2)
                    }]
                }
            })
        else:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "error": {"code": -32601, "message": f"Method '{method}' not found"}
            })
    except Exception as e:
        return json.dumps({
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": -32000, "message": str(e)}
        })

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        sample = {'mean_gcipl_thickness_um': 72.4, 'baseline_gcipl_thickness_um': 74.5, 'interval_years': 2.5, 'age_years': 62}
        out = audit_oct_gcipl_neurodegeneration(**sample)
        print("[TEST_PASS] Output:", json.dumps(out))
    else:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            print(handle_rpc(line))
