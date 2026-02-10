# Surface Pressure

## Overview
Surface pressure represents the atmospheric pressure at the Earth's surface, which is the weight of the atmospheric column above a given point. This fundamental meteorological variable is critical for understanding atmospheric dynamics, weather systems, and mass distribution in the atmosphere.

## Scientific Description
Surface pressure is defined as the pressure exerted by the atmosphere at the actual surface elevation, including the weight of air from the surface to the top of the atmosphere. In ERA5, surface pressure is a prognostic variable computed directly by the atmospheric model at each grid point's orography height.

Unlike mean sea level pressure (which is a diagnostic variable adjusted to sea level), surface pressure represents the actual pressure at the model's surface, making it the physically consistent variable for:
- Mass budget calculations
- Hydrostatic pressure profile integration
- Terrain-following coordinate transformations
- Surface flux computations

The surface pressure field exhibits strong spatial gradients related to:
1. **Synoptic-scale weather systems**: Cyclones (low pressure) and anticyclones (high pressure)
2. **Orographic effects**: Lower pressure at higher elevations following the barometric formula
3. **Thermal forcing**: Warm air columns expand, creating surface pressure deficits
4. **Mass convergence/divergence**: Associated with vertical motion

## Units
- **Standard Unit**: Pascals (Pa)
- **Common Alternative**: Hectopascals (hPa) - divide by 100
- **Alternative Units**: Millibars (mb) - numerically equivalent to hPa
- **Typical Range**: 
  - Sea level: ~950-1050 hPa
  - High elevations: Can be as low as 500 hPa on high plateaus
  - Extremes: <870 hPa in intense tropical cyclones; >1085 hPa in strong anticyclones

## Applications in Climate Research

### Atmospheric Dynamics
Surface pressure gradients drive horizontal wind through the pressure gradient force, fundamental to understanding:
- Geostrophic wind balance
- Cyclogenesis and storm development
- Frontal systems and baroclinic waves

### Mass Budget and Continuity
Surface pressure is proportional to the mass of the atmospheric column, making it essential for:
- Global atmospheric mass conservation
- Vertical velocity calculations
- Continuity equation applications

### Altitude Corrections
Surface pressure is required to:
- Convert between pressure-level and height-level data
- Compute geopotential height
- Adjust observations to standard pressure levels

### Climate Indices
Surface pressure anomalies define important climate patterns:
- **Southern Oscillation Index (SOI)**: Tahiti-Darwin pressure difference
- **North Atlantic Oscillation (NAO)**: Iceland-Azores pressure dipole
- **Arctic Oscillation (AO)**: Northern Hemisphere annular mode

### Aviation and Transport
Surface pressure determines:
- Altimeter settings for aircraft
- Density altitude for aircraft performance
- Pressure altitude for flight level determination

### Vertical Structure Analysis
Combined with temperature, surface pressure determines the entire atmospheric vertical structure through hydrostatic equilibrium.

## Related Variables
- **mean_sea_level_pressure**: Surface pressure reduced to sea level for synoptic analysis
- **surface_temperature**: Related through equation of state
- **10m_u_component_of_wind** / **10m_v_component_of_wind**: Driven by surface pressure gradients
- **2m_temperature**: Influences pressure through air density changes

## Mathematical Relationships
- **Barometric Formula**: P(z) = P₀ exp(-∫(g/(RT))dz) for pressure variation with height
- **Ideal Gas Law**: P = ρRT where ρ is density, R is specific gas constant, T is temperature
- **Hydrostatic Balance**: dP/dz = -ρg where g is gravitational acceleration
- **Pressure Gradient Force**: F = -(1/ρ)∇P

## Data Characteristics in ERA5 Daily Statistics
- **Temporal Resolution**: Daily statistics (mean, minimum, maximum, spread) from hourly values
- **Spatial Resolution**: ~0.25° × 0.25° (approximately 25-30 km)
- **Vertical Level**: Surface (model orography height)
- **Availability**: 1940 to present

## Quality Considerations
- **Orographic representation**: Pressure values strongly depend on accurate surface elevation in model
- **Data assimilation**: Surface pressure observations are heavily assimilated, generally providing high-quality fields
- **Grid-point vs. area-average**: Pressure at a grid point represents conditions at that specific elevation
- **Sub-grid orography**: Unresolved terrain features can create microscale pressure variations
- **Temporal variability**: Diurnal and semidiurnal atmospheric tides produce small but systematic pressure oscillations

## Physical Context
Surface pressure is fundamentally determined by the weight of the atmospheric column:

**Ps = g ∫₀^∞ ρ dz ≈ 101,325 Pa at mean sea level**

where:
- g = gravitational acceleration (~9.81 m s⁻²)
- ρ = air density (function of temperature and humidity)
- z = height above surface

Key controlling factors:
1. **Atmospheric mass distribution**: Convergence increases surface pressure; divergence decreases it
2. **Temperature profile**: Warm columns have lower surface pressure at equivalent mass
3. **Water vapor content**: Moist air is less dense than dry air at same pressure and temperature
4. **Orography**: Higher elevation implies less atmospheric mass above, hence lower pressure

The global mean surface pressure (~985 hPa at Earth's mean elevation) represents the total mass of the atmosphere (~5.15 × 10¹⁸ kg).

## Meteorological Significance
- **Low Pressure Systems**: Associated with ascending motion, cloud formation, precipitation, and unstable weather
- **High Pressure Systems**: Associated with descending motion, clear skies, and stable weather conditions
- **Pressure Tendency**: Rate of pressure change indicates system intensification or weakening

## References
1. Hersbach, H., et al. (2020). The ERA5 global reanalysis. *Quarterly Journal of the Royal Meteorological Society*, 146(730), 1999-2049.
2. Wallace, J. M., & Hobbs, P. V. (2006). *Atmospheric Science: An Introductory Survey* (2nd ed.). Academic Press.
3. Holton, J. R., & Hakim, G. J. (2012). *An Introduction to Dynamic Meteorology* (5th ed.). Academic Press.
