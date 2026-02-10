# 10-Metre Wind Speed

## Overview
The 10-metre wind speed is the magnitude of the horizontal wind vector at 10 metres above the Earth's surface, representing the combined effect of the zonal (U) and meridional (V) wind components. This fundamental variable is essential for wind energy applications, surface flux calculations, and general weather characterization.

## Scientific Description
Wind speed (WS) is defined as the magnitude of the horizontal wind vector:

**WS = √(U² + V²)**

where:
- U = 10-metre zonal (east-west) wind component
- V = 10-metre meridional (north-south) wind component

The 10-metre height is the WMO standard for surface wind observations, chosen to be:
- Above the immediate surface roughness layer
- Representative of the near-surface wind field
- Consistent with anemometer installation standards
- Relevant for human-scale applications

In ERA5, the 10-metre wind speed is diagnosed from the atmospheric model's lowest level using Monin-Obukhov similarity theory, accounting for:
- Surface roughness characteristics (land use, vegetation, urban areas)
- Atmospheric stability (stable, neutral, unstable conditions)
- Momentum flux and surface stress
- Buoyancy effects

Unlike wind components (U, V) which can be positive or negative, wind speed is always non-negative (WS ≥ 0).

## Units
- **Standard Unit**: Metres per second (m s⁻¹)
- **Common Alternatives**:
  - Kilometres per hour (km h⁻¹) - multiply by 3.6
  - Knots (kt or kn) - multiply by 1.944
  - Miles per hour (mph) - multiply by 2.237
- **Typical Range**: 0-30 m s⁻¹; extremes in tropical cyclones can exceed 80 m s⁻¹ (>150 kt)

### Beaufort Scale Reference
- 0-0.5 m s⁻¹: Calm (0)
- 0.5-3.3 m s⁻¹: Light air to gentle breeze (1-3)
- 3.3-10.7 m s⁻¹: Moderate to fresh breeze (4-5)
- 10.7-20.7 m s⁻¹: Strong to near gale (6-7)
- 20.7-32.6 m s⁻¹: Gale to violent storm (8-11)
- >32.6 m s⁻¹: Hurricane force (12)

## Applications in Climate Research

### Wind Energy Assessment
Wind speed is the primary variable for wind power applications:
- **Power density**: P = ½ρ × WS³ (cubic relationship)
- Capacity factor calculations for wind turbines
- Site selection and wind resource mapping
- Temporal variability and intermittency analysis
- Extreme wind load assessment for turbine design

### Ocean-Atmosphere Exchange
Wind speed controls surface fluxes:
- **Momentum flux**: Wind stress τ = ρₐ Cᴰ × WS² (quadratic relationship)
- Sensible and latent heat fluxes (linear dependence)
- Gas exchange (CO₂, O₂) across air-sea interface
- Ocean surface wave generation and development

### Wind Erosion and Dust Transport
Wind speed determines:
- Threshold for soil particle mobilization (~6-8 m s⁻¹ depending on soil)
- Dust emission flux from arid regions
- Sandstorm frequency and intensity
- Agricultural soil loss

### Evapotranspiration
Wind speed affects:
- Aerodynamic resistance in Penman-Monteith equation
- Crop water requirements
- Irrigation scheduling
- Drought impact assessment

### Fire Weather
Wind speed is critical for fire behavior:
- Fire spread rate (nearly linear with wind speed)
- Fire weather indices (e.g., Fosberg Fire Weather Index)
- Ember transport and spotting potential
- Firefighting resource allocation

### Storm Intensity
Wind speed characterizes storm strength:
- Tropical cyclone categories (Saffir-Simpson scale)
- Extratropical cyclone intensity
- Damaging wind event identification
- Insurance and disaster risk assessment

### Air Quality Dispersion
Wind speed controls pollutant dispersion:
- Ventilation of urban areas
- Pollutant concentration dilution
- Long-range transport of aerosols
- Industrial plume modeling

## Related Variables
- **10m_u_component_of_wind**: Zonal component; U = WS × sin(θ) where θ is wind direction
- **10m_v_component_of_wind**: Meridional component; V = WS × cos(θ)
- **surface_pressure**: Pressure gradient drives wind
- **mean_sea_level_pressure**: MSLP gradient relates to geostrophic wind speed
- **100m_u/v_component_of_wind**: Wind speed at turbine hub height
- **total_evaporation**: Wind enhances evaporation
- **sea_surface_temperature**: Wind affects ocean mixing and heat flux

## Mathematical Relationships
- **Wind Speed from Components**: WS = √(U² + V²)
- **Wind Direction**: θ = arctan2(U, V) (direction *from* which wind blows)
- **Wind Stress**: τ = ρₐ Cᴰ WS² where ρₐ is air density and Cᴰ is drag coefficient (~0.001-0.003)
- **Wind Power Density**: P/A = ½ρₐ WS³ (W m⁻²)
- **Turbine Power**: Pₜᵤᵣբᵢₙₑ = ½ρₐ A Cₚ WS³ where A is rotor area and Cₚ is power coefficient

## Data Characteristics in ERA5 Daily Statistics
- **Temporal Resolution**: Daily statistics (mean, minimum, maximum, spread) from hourly values
- **Spatial Resolution**: ~0.25° × 0.25° (approximately 25-30 km)
- **Vertical Level**: 10 metres above surface (diagnostic height)
- **Availability**: 1940 to present

## Quality Considerations
- **Complex terrain**: Mountain flows, valley channeling not fully resolved at model resolution
- **Coastal zones**: Strong land-sea wind gradients at sub-grid scales
- **Gustiness**: Mean wind speed doesn't capture short-term gusts important for wind loads
- **Surface roughness**: Urban and vegetation roughness parameterized; microscale variations unresolved
- **Calm conditions**: Model tends to slightly overestimate very light winds (WS < 2 m s⁻¹)
- **Extreme winds**: Tropical cyclone core winds may be underestimated due to model resolution

## Physical Context

### Wind Speed Drivers
1. **Pressure Gradient Force**: Strong gradients → high wind speed
2. **Coriolis Force**: Deflects moving air, not affecting speed magnitude directly
3. **Friction**: Surface drag reduces wind speed (stronger effect in rough terrain)
4. **Thermal Effects**: Sea/land breeze, mountain/valley winds modify speed

### Vertical Wind Profile
Wind speed increases with height above surface following:
- **Power law**: WS(z) = WS(z₀) × (z/z₀)^α where α ≈ 1/7 for neutral conditions
- **Logarithmic profile**: WS(z) = (u*/κ) × ln(z/z₀) where u* is friction velocity, κ is von Kármán constant, z₀ is roughness length

### Diurnal Variation
- **Daytime**: Strong turbulent mixing can enhance surface winds
- **Nighttime**: Stable stratification can decouple surface from upper-level flow, reducing surface wind
- **Coastal**: Sea breeze (daytime onshore) and land breeze (nighttime offshore)

## Practical Interpretation
- **WS < 3 m s⁻¹**: Light winds, limited wind power generation
- **WS 3-12 m s⁻¹**: Moderate winds, optimal range for wind turbines
- **WS 12-25 m s⁻¹**: Strong winds, maximum turbine output; caution for exposed areas
- **WS > 25 m s⁻¹**: High winds, turbines shut down; damaging wind potential
- **WS > 33 m s⁻¹**: Hurricane-force winds, structural damage risk

### Statistical Distributions
Wind speed often follows:
- **Weibull distribution**: Two-parameter distribution commonly used for wind statistics
- **Shape parameter**: Typically 1.5-3.0 for different locations
- **Scale parameter**: Related to mean wind speed

## Climate Change Context
Observed and projected wind speed changes:
1. **Global mean**: Slight decrease in land surface winds ("stilling") observed in recent decades, though trend reversal noted post-2010
2. **Ocean winds**: General strengthening in Southern Ocean
3. **Extreme winds**: Changes depend on storm track shifts and intensity
4. **Tropical cyclones**: Intensity projected to increase (stronger winds)

## Wind Energy Implications
Wind power is highly sensitive to wind speed:
- **Cubic relationship**: 10% wind speed increase → 33% power increase
- **Cut-in speed**: Typically 3-4 m s⁻¹ for turbine operation
- **Rated speed**: 12-15 m s⁻¹ for maximum power output
- **Cut-out speed**: 25 m s⁻¹ for turbine protection

## References
1. Hersbach, H., et al. (2020). The ERA5 global reanalysis. *Quarterly Journal of the Royal Meteorological Society*, 146(730), 1999-2049.
2. Stull, R. B. (1988). *An Introduction to Boundary Layer Meteorology*. Springer.
3. Manwell, J. F., et al. (2009). *Wind Energy Explained: Theory, Design and Application* (2nd ed.). Wiley.
4. Zeng, Z., et al. (2019). A reversal in global terrestrial stilling and its implications for wind energy production. *Nature Climate Change*, 9(12), 979-985.
