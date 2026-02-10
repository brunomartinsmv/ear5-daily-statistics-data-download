# Surface Solar Radiation Downwards

## Overview
Surface solar radiation downwards (also called incoming shortwave radiation or insolation) represents the total solar radiation reaching the Earth's surface from above, including both direct and diffuse components. This is the primary energy input to the surface during daytime.

## Scientific Description
Downward solar radiation at the surface (SW↓) has been attenuated from the top-of-atmosphere value by:

**Atmospheric Attenuation**:
1. **Scattering**: Rayleigh (molecules), Mie (aerosols, cloud droplets)
2. **Absorption**: O₃ (UV), H₂O, CO₂ (near-IR), aerosols
3. **Cloud effects**: Major control (can reduce by 50-90%)

Components:
- **Direct beam**: Sunlight reaching surface directly
- **Diffuse**: Scattered sunlight from sky and clouds
- **Total**: SW↓ = Direct + Diffuse

Clear-sky maximum: ~1000 W m⁻² (solar noon, sea level, perpendicular to sun)

Factors affecting SW↓:
- **Solar zenith angle**: cos(θ) dependence
- **Atmospheric path length**: Longer at high zenith angles
- **Cloud optical depth**: Thicker clouds block more
- **Aerosol loading**: Scattering and absorption
- **Surface elevation**: Higher elevation → less atmosphere → more radiation

## Units
- Joules per square metre (J m⁻²) for daily accumulation
- Watts per square metre (W m⁻²) for instantaneous flux
- Daily mean: 100-300 W m⁻² typical; 0 W m⁻² polar winter

## Applications
- **Photosynthesis**: Light availability for plant growth
- **Evapotranspiration**: Primary energy source for evaporation
- **Solar energy**: Photovoltaic and solar thermal potential
- **Surface temperature**: Daytime heating source
- **Snowmelt**: Solar radiation melts snow
- **Climate**: Radiative forcing and energy balance

## Related Variables
- surface_net_solar_radiation: SW↓ - SW↑ (accounts for albedo)
- total_cloud_cover: Major control on SW↓
- 2m_temperature: Heated by absorbed solar radiation
- surface_pressure: Affects atmospheric path length

## Diurnal and Seasonal Patterns
**Diurnal**: Bell-shaped curve, maximum at solar noon, zero at night

**Seasonal**:
- Summer: Maximum (long days, high sun angle)
- Winter: Minimum (short days, low sun angle)  
- Tropics: Relatively constant
- High latitudes: Extreme range (24-h sun to 24-h darkness)

## Cloud Effects
- Clear sky: High SW↓ (up to ~1000 W m⁻²)
- Thin clouds: Moderate reduction (500-700 W m⁻²)
- Thick clouds: Large reduction (100-300 W m⁻²)
- Overcast: Can be <100 W m⁻² even at noon

## References
1. Hersbach, H., et al. (2020). *Q. J. R. Meteorol. Soc.*, 146(730), 1999-2049.
2. Iqbal, M. (1983). *An Introduction to Solar Radiation*. Academic Press.
