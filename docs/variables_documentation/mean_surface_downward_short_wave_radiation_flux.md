# Mean Surface Downward Short Wave Radiation Flux

## Overview
Mean surface downward shortwave radiation flux is synonymous with surface solar radiation downwards, representing the incoming solar (shortwave) radiation at the Earth's surface. The term "shortwave" emphasizes that this radiation is in the 0.2-4 μm wavelength range, distinguishing it from thermal (longwave) radiation.

## Scientific Description
Shortwave radiation from the sun is attenuated through the atmosphere by:

**Scattering** (wavelength-dependent):
- Rayleigh: Molecular scattering (blue sky)
- Mie: Aerosol and cloud droplet scattering
- Result: Direct→diffuse conversion

**Absorption**:
- UV: Ozone (~3% of solar)
- Visible: Minimal (atmospheric window)
- Near-IR: Water vapor, CO₂ (~20% of solar)

**Cloud effects**: Dominant control
- Reflection back to space
- Forward scattering (increases diffuse)
- Net effect: Reduces surface SW↓

Surface receives:
- Global average: ~185 W m⁻² (24-hour, all-sky)
- Clear-sky maximum: ~1000 W m⁻² (solar noon)
- Cloudy conditions: 100-700 W m⁻² (depends on cloud thickness)

## Units
- J m⁻² (daily accumulation) or W m⁻² (instantaneous)

## Applications
Identical to "surface_solar_radiation_downwards":
- Solar energy resource assessment
- Photosynthesis and agriculture
- Evapotranspiration modeling
- Building energy analysis
- Climate and radiation budget studies

## Quality Considerations
- Well-constrained by satellite observations
- Surface networks (BSRN) provide validation
- Cloud representation major uncertainty
- Aerosol effects important (dimming/brightening)

## Relationship to Other Variables
**SW↓ = SW_net / (1 - albedo)**

Where SW_net is absorbed shortwave, albedo is surface reflectance

## References
1. Hersbach, H., et al. (2020). The ERA5 global reanalysis. *Quarterly Journal of the Royal Meteorological Society*, 146(730), 1999-2049.
2. See "surface_solar_radiation_downwards.md" for comprehensive details
