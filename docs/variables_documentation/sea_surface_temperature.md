# Sea Surface Temperature

## Overview
Sea surface temperature (SST) represents the temperature of the ocean's surface layer, typically measured within the top meter of the water column. This critical variable serves as the primary indicator of ocean-atmosphere heat exchange and is fundamental to understanding climate variability, marine ecosystems, and weather patterns.

## Scientific Description
In ERA5, sea surface temperature is defined as the temperature of the uppermost layer of the ocean, representing the interface where the ocean and atmosphere exchange heat, momentum, and moisture. The SST field in ERA5 is constrained by observational data through the data assimilation system, integrating information from:

1. **In-situ observations**: Ships, buoys, and drifters measuring bucket or hull intake temperatures
2. **Satellite retrievals**: Infrared and microwave radiometers measuring skin temperature
3. **Model ocean dynamics**: NEMO ocean model providing physical consistency

The SST impacts atmospheric conditions through:
- **Sensible heat flux**: Direct temperature exchange between ocean and air
- **Latent heat flux**: Evaporation controlled by SST and surface wind
- **Boundary layer stability**: SST gradient affects atmospheric stratification
- **Convection initiation**: Warm SST (>26-27°C) necessary for tropical cyclones

## Units
- **Standard Unit**: Kelvin (K)
- **Common Alternative**: Degrees Celsius (°C) - subtract 273.15 from Kelvin
- **Typical Range**: 
  - Polar regions: 271-273 K (-2°C to 0°C) near freezing point of seawater
  - Tropical oceans: 298-303 K (25°C to 30°C)
  - Mid-latitudes: 273-293 K (0°C to 20°C) with strong seasonal variation

## Applications in Climate Research

### El Niño-Southern Oscillation (ENSO)
SST in the tropical Pacific defines ENSO phases:
- **El Niño**: Anomalously warm SST in eastern equatorial Pacific
- **La Niña**: Anomalously cool SST in eastern equatorial Pacific
- **Niño indices**: Based on SST anomalies in specific regions (Niño 3, 3.4, 4, etc.)

### Tropical Cyclone Development
SST is the primary energy source for hurricanes/typhoons:
- Threshold for genesis: SST > 26-27°C
- Ocean heat content: Depth of warm layer determines intensification potential
- Rapid intensification: Occurs over SST > 28°C with favorable atmospheric conditions

### Marine Heatwaves
Extreme SST events impact marine ecosystems:
- Coral bleaching (SST exceeds normal summer maximum by 1-2°C)
- Fish migration and distribution shifts
- Harmful algal blooms
- Ecosystem regime shifts

### Ocean-Atmosphere Coupling
SST influences atmospheric circulation:
- **Walker Circulation**: Driven by SST gradients in tropical Pacific
- **Madden-Julian Oscillation (MJO)**: Influenced by Indo-Pacific SST patterns
- **Monsoon systems**: SST gradients drive land-sea thermal contrasts
- **Mid-latitude storm tracks**: Positioned along strong SST fronts

### Climate Change and Variability
SST trends indicate:
- Global ocean heat uptake (~90% of Earth's energy imbalance)
- Ocean warming patterns and hotspots
- Sea level rise contribution from thermal expansion
- Changes in ocean stratification and mixing

### Marine Ecosystem Modeling
SST affects:
- Primary productivity and phytoplankton growth
- Species distribution and migration patterns
- Fish stock dynamics and fisheries management
- Biogeochemical cycles

### Weather Forecasting
SST provides lower boundary condition for:
- Numerical weather prediction models
- Precipitation forecasts (especially tropical regions)
- Tropical cyclone track and intensity prediction
- Marine fog formation

## Related Variables
- **2m_temperature**: Air temperature influenced by underlying SST
- **10m_u/v_component_of_wind**: Surface winds affect SST through mixing and heat flux
- **total_precipitation**: SST influences evaporation and convective precipitation
- **sea_ice_area_fraction**: Ice cover insulates ocean from atmosphere
- **mean_sea_level_pressure**: Pressure patterns influenced by SST gradients

## Mathematical Relationships
- **Air-Sea Heat Flux**: Q = Qsensible + Qlatent + Qsolar + Qlongwave
- **Sensible Heat Flux**: Qs = ρa cp CH U(SST - Ta) where ρa is air density, cp is specific heat, CH is transfer coefficient, U is wind speed, Ta is air temperature
- **Latent Heat Flux**: QL = ρa Lv CE U(qs - qa) where Lv is latent heat, CE is transfer coefficient, qs is saturation humidity at SST, qa is air humidity
- **SST Tendency**: ∂SST/∂t = (Q + Qocean)/(ρw cw h) where ρw is water density, cw is heat capacity of water, h is mixed layer depth

## Data Characteristics in ERA5 Daily Statistics
- **Temporal Resolution**: Daily statistics (mean, minimum, maximum, spread) from hourly values
- **Spatial Resolution**: ~0.25° × 0.25° (approximately 25-30 km)
- **Vertical Level**: Sea surface (typically top ~1 meter)
- **Coverage**: Ocean grid points only; undefined over land
- **Availability**: 1940 to present

## Quality Considerations
- **Satellite vs. in-situ differences**: Satellite measures skin temperature (~10 μm depth); in-situ measures bulk temperature (~1 m depth)
- **Diurnal warm layer**: Daytime solar heating can create thin warm layer at surface
- **Cool skin effect**: Molecular layer at surface typically 0.1-0.5°C cooler than bulk SST
- **Sea ice transition**: SST near ice edge subject to strong gradients
- **Coastal regions**: Land-sea boundary effects and unresolved ocean features
- **Observational coverage**: Sparse in early period (pre-satellite era before ~1980)

## Physical Context
SST is determined by the balance of heat fluxes:

### Heat Gain
- **Solar radiation**: Shortwave radiation penetrating the surface
- **Downward longwave radiation**: Infrared from atmosphere

### Heat Loss
- **Upward longwave radiation**: Infrared emission from ocean surface
- **Sensible heat flux**: Conduction/convection to atmosphere
- **Latent heat flux**: Evaporative cooling (dominant in tropics)

### Ocean Processes
- **Horizontal advection**: Ocean currents transport heat
- **Vertical mixing**: Entrainment of deeper water modifies SST
- **Upwelling**: Cold deep water brought to surface
- **Ekman transport**: Wind-driven surface currents

## Climate Significance
SST patterns define:
1. **Tropical warm pools**: Regions of deep atmospheric convection
2. **Cold tongue**: Equatorial Pacific upwelling region
3. **Western boundary currents**: Gulf Stream, Kuroshio transport warm water poleward
4. **Upwelling zones**: Nutrient-rich, biologically productive regions

SST anomalies can persist for months to years, providing:
- Predictability for seasonal climate forecasts
- Memory in the climate system
- Modulation of atmospheric teleconnections

## Interpretation Notes
- **SST > 26-27°C**: Threshold for tropical convection and cyclone development
- **SST gradients**: Strong fronts (Gulf Stream, Kuroshio) associated with storm tracks
- **Seasonal cycle**: Largest in mid-latitudes (10-15°C); smaller in tropics (2-3°C)
- **ENSO indicators**: Monitor Niño 3.4 region (5°N-5°S, 170°W-120°W)

## References
1. Hersbach, H., et al. (2020). The ERA5 global reanalysis. *Quarterly Journal of the Royal Meteorological Society*, 146(730), 1999-2049.
2. Reynolds, R. W., et al. (2002). An improved in situ and satellite SST analysis for climate. *Journal of Climate*, 15(13), 1609-1625.
3. Fairall, C. W., et al. (2003). Bulk parameterization of air-sea fluxes: Updates and verification for the COARE algorithm. *Journal of Climate*, 16(4), 571-591.
4. Oliver, E. C., et al. (2018). Longer and more frequent marine heatwaves over the past century. *Nature Communications*, 9(1), 1324.
