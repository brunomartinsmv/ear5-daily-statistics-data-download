# Surface Net Solar Radiation

## Overview
Surface net solar radiation represents the net shortwave (solar) radiative flux at the Earth's surface, defined as the difference between downward (incoming) and upward (reflected) solar radiation. This fundamental energy balance component drives surface heating, evaporation, and photosynthesis, making it critical for climate, hydrological, and biological processes.

## Scientific Description
The net solar radiation at the surface is defined as:

**Rn_solar = SW↓ - SW↑ = SW↓ × (1 - α)**

where:
- SW↓ = downward (incoming) solar radiation
- SW↑ = upward (reflected) solar radiation  
- α = surface albedo (reflectivity)

In ERA5, this variable represents the accumulated net solar radiation over the specified time period (e.g., daily). The sign convention is:
- **Positive values**: Net energy gain at surface (downward > upward)
- **Negative values**: Generally not occur for solar radiation (except at night when both are zero)

Key controlling factors:
1. **Solar zenith angle**: Determines incident solar flux (latitude, season, time of day)
2. **Cloud cover**: Reduces incoming solar radiation
3. **Atmospheric composition**: Aerosols, water vapor, ozone affect transmission
4. **Surface albedo**: Determines fraction reflected (snow: 0.6-0.9; ocean: 0.06; vegetation: 0.15-0.25)

## Units
- **Standard Unit**: Joules per square metre (J m⁻²)
- **Alternative**: Watts per square metre (W m⁻²) - divide by accumulation period in seconds
- **Daily average**: Typically 50-300 W m⁻² (global mean ~185 W m⁻²)
- **Instantaneous**: Can exceed 1000 W m⁻² at solar noon under clear skies

## Applications in Climate Research

### Surface Energy Balance
Net solar radiation is the dominant energy source:
- **Energy balance**: Rn = Rn_solar + Rn_thermal = H + LE + G
  - H = sensible heat flux
  - LE = latent heat flux (evaporation)
  - G = ground heat flux
- **Bowen ratio**: Partitioning between sensible and latent heat
- **Surface temperature**: Determined by energy balance

### Climate Change and Radiative Forcing
Solar radiation at surface affected by:
- **Aerosol direct effect**: Scattering and absorption reduce surface solar
- **Cloud feedbacks**: Cloud changes alter surface radiation
- **Surface albedo feedback**: Snow/ice loss reduces albedo, increases absorption
- **Dimming/brightening**: Observed trends in surface solar radiation

### Photosynthesis and Primary Production
Net solar radiation (especially photosynthetically active radiation, PAR):
- **Gross primary production (GPP)**: Carbon uptake by vegetation
- **Crop yields**: Agricultural productivity depends on solar energy
- **Ecosystem function**: Light availability for photosynthesis

### Evapotranspiration
Solar radiation is primary energy source for evaporation:
- **Penman-Monteith equation**: Radiation term dominant in ET calculation
- **Soil moisture**: Drying rate depends on available energy
- **Irrigation demand**: Crop water requirements scale with radiation

### Solar Energy Applications
Net surface solar determines:
- **Photovoltaic potential**: Direct relationship to PV power generation
- **Solar thermal systems**: Collector performance
- **Building energy**: Passive solar heating, cooling loads
- **Site selection**: Resource assessment for solar installations

### Climate Zones and Habitability
Solar radiation distribution defines:
- **Tropical/subtropical**: High solar input year-round
- **Temperate**: Strong seasonal cycle
- **Polar**: Extreme seasonal variation (continuous summer sun, winter darkness)
- **Desert formation**: High solar input + low humidity → high evaporative demand

## Related Variables
- **surface_solar_radiation_downwards**: Incoming component (before surface reflection)
- **surface_net_thermal_radiation**: Longwave component of net radiation
- **total_cloud_cover**: Cloud amount attenuates solar radiation
- **2m_temperature**: Surface temperature affected by radiative heating
- **total_evaporation**: Driven by available radiative energy
- **snow_cover**: High albedo surfaces reduce net solar radiation

## Mathematical Relationships
- **Net = Downward - Upward**: Rn_solar = SW↓ - SW↑
- **Albedo**: α = SW↑ / SW↓
- **Absorbed**: Rn_solar = SW↓ × (1 - α)
- **Clear-sky maximum**: ~1000 W m⁻² cos(θ) × transmissivity, where θ is solar zenith angle

## Data Characteristics in ERA5 Daily Statistics
- **Temporal Resolution**: Daily accumulations from hourly fluxes
- **Spatial Resolution**: ~0.25° × 0.25° (approximately 25-30 km)
- **Sign Convention**: Positive downward (energy gain at surface)
- **Availability**: 1940 to present
- **Diurnal Cycle**: Maximum at local solar noon, zero at night

## Quality Considerations
- **Cloud representation**: Radiative transfer through clouds parameterized
- **Aerosol effects**: Direct and indirect aerosol effects on radiation
- **Surface albedo**: Parameterized based on land cover, snow, ice
- **Temporal averaging**: Daily values smooth diurnal variability
- **Complex terrain**: Topographic shading and slope effects at sub-grid scale
- **Validation**: Surface radiation networks (BSRN, SURFRAD) provide validation data

## Physical Context

### Solar Radiation Budget
Incoming solar radiation at top of atmosphere (TOA):
- **Solar constant**: ~1361 W m⁻² (perpendicular to sun's rays)
- **Global mean**: ~340 W m⁻² (accounting for geometry and night)

Atmospheric attenuation:
- **Scattering**: Rayleigh (molecules), Mie (aerosols)
- **Absorption**: O₃ (UV), H₂O, CO₂ (near-IR)
- **Cloud reflection**: Major control on surface radiation

Surface budget:
- **Absorption**: (1-α) × SW↓
- **Reflection**: α × SW↓

### Geographic Patterns
- **Equatorial maximum**: High sun angle year-round
- **Subtropical deserts**: High values (clear skies, high sun angle)
- **Mid-latitudes**: Strong seasonal variation
- **Polar regions**: Extreme seasonal cycle (24-h sun/darkness)

### Diurnal Cycle
- **Dawn**: Radiation increases from zero
- **Solar noon**: Maximum (sun highest in sky)
- **Dusk**: Radiation decreases to zero
- **Night**: Zero solar radiation
- **Daily integral**: Depends on day length, cloud cover, latitude

## Practical Interpretation
- **< 50 W m⁻²**: Low (cloudy, high latitude winter)
- **50-150 W m⁻²**: Moderate (temperate regions, partial cloud)
- **150-250 W m⁻²**: High (tropics, clear skies)
- **> 250 W m⁻²**: Very high (subtropical deserts, summer, clear)

### Seasonal Variation
- **Summer**: Maximum (long days, high sun angle)
- **Winter**: Minimum (short days, low sun angle)
- **Equinoxes**: Intermediate values
- **Tropics**: Relatively constant (sun always high)

## Albedo Effects
Surface type strongly affects net radiation:

| Surface | Albedo | Net (from 1000 W m⁻² incident) |
|---------|--------|--------------------------------|
| Fresh snow | 0.80-0.90 | 100-200 W m⁻² |
| Sea ice | 0.50-0.70 | 300-500 W m⁻² |
| Desert sand | 0.30-0.40 | 600-700 W m⁻² |
| Grassland | 0.18-0.25 | 750-820 W m⁻² |
| Forest | 0.10-0.15 | 850-900 W m⁻² |
| Ocean | 0.06-0.10 | 900-940 W m⁻² |

## Climate Change Context
Observed and projected changes:
1. **Global dimming (1950s-1980s)**: Surface solar decreased (aerosol increase)
2. **Global brightening (1990s-2000s)**: Surface solar increased (aerosol regulations)
3. **Cloud feedbacks**: Uncertain sign and magnitude in projections
4. **Albedo feedback**: Snow/ice loss → lower albedo → more absorption → warming
5. **Aerosol uncertainties**: Future aerosol emissions affect surface solar

## Solar Energy Implications
For photovoltaics:
- **Resource assessment**: Long-term climatology determines site viability
- **Variability**: Cloud cover creates intermittency challenges
- **Forecast need**: Short-term predictions for grid integration
- **Capacity factor**: Typically 15-25% (ratio of actual to peak output)

## References
1. Hersbach, H., et al. (2020). The ERA5 global reanalysis. *Quarterly Journal of the Royal Meteorological Society*, 146(730), 1999-2049.
2. Wild, M., et al. (2013). The global energy balance from a surface perspective. *Climate Dynamics*, 40(11-12), 3107-3134.
3. Ohmura, A., et al. (1998). Baseline Surface Radiation Network (BSRN/WCRP): New precision radiometry for climate research. *Bulletin of the American Meteorological Society*, 79(10), 2115-2136.
4. Trenberth, K. E., & Fasullo, J. T. (2012). Tracking Earth's energy: From El Niño to global warming. *Surveys in Geophysics*, 33(3-4), 413-426.
