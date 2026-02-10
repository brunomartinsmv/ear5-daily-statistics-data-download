# Total Evaporation

## Overview
Total evaporation represents the combined flux of water from the Earth's surface (land and ocean) and vegetation into the atmosphere. In ERA5, this variable integrates evaporation from soil, open water bodies, and transpiration from vegetation. By convention, evaporation is negative (water leaving the surface) and precipitation is positive (water arriving at the surface).

## Scientific Description
Total evaporation in ERA5 encompasses several physical processes:

1. **Bare Soil Evaporation**: Direct evaporation from soil surfaces
2. **Open Water Evaporation**: Evaporation from oceans, lakes, rivers
3. **Transpiration**: Water vapor released by plant stomata
4. **Interception Evaporation**: Evaporation of water intercepted by canopy before reaching ground
5. **Snow Sublimation**: Direct conversion of snow/ice to water vapor

The variable is computed from the surface energy budget and moisture availability:

**E = ρa × CE × U × (qs - qa)**

where:
- ρa = air density
- CE = transfer coefficient for moisture
- U = wind speed
- qs = saturation specific humidity at surface temperature
- qa = specific humidity of near-surface air

The actual evaporation is limited by:
- Available surface moisture (soil moisture, snow cover, water bodies)
- Vegetation characteristics (stomatal resistance, leaf area)
- Atmospheric demand (vapor pressure deficit)
- Energy availability (net radiation, sensible heat flux)

## Units
- **Standard Unit**: Metres (m) of liquid water equivalent
- **Common Alternative**: Millimetres (mm) - multiply by 1000
- **Alternative Units**: kg m⁻² (numerically equivalent to mm)
- **Sign Convention**: Negative values indicate evaporation (water loss from surface)
- **Typical Range**: 
  - Arid regions: 1-3 mm/day
  - Humid continents: 3-6 mm/day
  - Tropical oceans: 5-8 mm/day
  - Can approach 10 mm/day in hot, dry, windy conditions

## Applications in Climate Research

### Water Balance and Hydrology
Evaporation is a critical component of the water balance:
- **Surface water budget**: P - E - R = ΔS (precipitation minus evaporation minus runoff equals storage change)
- **Lake and reservoir management**: Evaporative losses affect water availability
- **Irrigation requirements**: Crop water needs determined by evapotranspiration
- **Groundwater recharge**: P - E determines infiltration potential

### Climate and Energy Balance
Evaporation transfers energy through latent heat:
- **Latent heat flux**: QL = Lv × E where Lv ≈ 2.5 × 10⁶ J kg⁻¹
- **Surface energy partitioning**: Bowen ratio = QH/QL (sensible/latent heat)
- **Climate feedback**: Evaporation affects temperature, humidity, clouds
- **Land-atmosphere coupling**: Soil moisture-evaporation-precipitation feedbacks

### Drought and Aridity
Evaporation relative to precipitation determines:
- **Aridity index**: E/P characterizes climate moisture
- **Drought severity**: High evaporative demand exacerbates water deficits
- **Agricultural drought**: Soil moisture depletion rate
- **Evaporative stress index**: Actual/potential evaporation ratio

### Ocean-Atmosphere Interaction
Over oceans, evaporation:
- **Freshwater flux**: E - P determines ocean salinity tendency
- **Moisture source for precipitation**: Oceanic evaporation feeds atmospheric moisture
- **Subtropical-tropical exchange**: Trade wind evaporation sustains tropical precipitation
- **SST feedback**: Evaporative cooling regulates sea surface temperature

### Vegetation and Ecosystems
Evapotranspiration (ET) reflects:
- **Plant water use**: Transpiration component of ET
- **Ecosystem productivity**: ET correlates with gross primary production
- **Phenology**: Seasonal ET cycle tracks vegetation growing season
- **Land cover change impacts**: Deforestation alters evapotranspiration

### Climate Change
Evaporation trends indicate:
- **Intensifying hydrological cycle**: E and P both increasing globally
- **Regional patterns**: "Dry gets drier, wet gets wetter" paradigm
- **Evaporative demand increase**: Rising temperatures increase potential ET
- **Drought risk**: Enhanced evaporation under warming

## Related Variables
- **total_precipitation**: Complements evaporation in water balance
- **2m_temperature**: Higher temperature increases evaporative capacity
- **2m_dewpoint_temperature**: Vapor pressure deficit (T - Td) drives evaporation
- **10m_wind_speed**: Wind enhances evaporation rate
- **surface_net_solar_radiation**: Energy source for evaporation
- **soil_moisture**: Availability of water for evaporation

## Mathematical Relationships
- **Water Balance**: ΔS = P - E - R where S is storage (soil moisture, snow, etc.)
- **Penman-Monteith Equation**: Combines energy balance and aerodynamic approaches for potential ET
- **Latent Heat**: QL = Lv × ρw × E where ρw is water density
- **Priestley-Taylor**: E = α × (Δ/(Δ+γ)) × Rn/Lv (simplified equilibrium evaporation)

## Data Characteristics in ERA5 Daily Statistics
- **Temporal Resolution**: Daily accumulations from hourly fluxes
- **Spatial Resolution**: ~0.25° × 0.25° (approximately 25-30 km)
- **Sign Convention**: Negative for evaporation (upward flux)
- **Availability**: 1940 to present

## Quality Considerations
- **Model parameterization**: Evaporation depends on surface and vegetation schemes
- **Soil moisture**: Evaporation limited by available soil water (model-dependent)
- **Vegetation representation**: Stomatal resistance and canopy structure parameterized
- **Energy balance closure**: Observed fluxes often don't close energy budget; reanalysis should close
- **Heterogeneous surfaces**: Grid cell represents mix of land types
- **Observational constraints**: Few direct evaporation observations; mostly estimated

## Physical Context

### Evaporation Controls
Evaporation rate depends on:

1. **Energy Supply**:
   - Solar radiation (primary energy source)
   - Air temperature (affects vapor pressure gradient)
   - Net longwave radiation

2. **Vapor Gradient**:
   - Surface humidity (saturation at surface temperature)
   - Air humidity (determines gradient)
   - Vapor pressure deficit (qs - qa)

3. **Turbulent Transport**:
   - Wind speed (enhances vapor removal)
   - Atmospheric stability (affects turbulent mixing)
   - Surface roughness (affects momentum and moisture transfer)

4. **Water Availability**:
   - Soil moisture content
   - Surface water extent
   - Snow/ice presence
   - Vegetation water stress

### Regional Patterns
- **Tropical oceans**: High evaporation (6-8 mm/day) due to warm SST, trade winds
- **Subtropics**: Peak oceanic evaporation (8-10 mm/day) in subsidence regions
- **Mid-latitude oceans**: Moderate evaporation (3-5 mm/day), seasonal variation
- **Continental interiors**: Limited by soil moisture availability
- **Rainforests**: High ET (4-6 mm/day) from transpiration
- **Deserts**: Low evaporation (<1 mm/day) due to water limitation

### Diurnal Cycle
- **Peak evaporation**: Afternoon when radiation maximum and vapor deficit largest
- **Minimum**: Night when radiation absent and humidity high
- **Amplitude**: Large over land (water availability dependent), small over ocean

## Practical Interpretation
- **|E| < 2 mm/day**: Low evaporation (arid, winter, cloudy)
- **|E| 2-4 mm/day**: Moderate evaporation (temperate, adequate moisture)
- **|E| 4-6 mm/day**: High evaporation (humid, vegetated, or warm oceans)
- **|E| > 6 mm/day**: Very high evaporation (hot, dry, windy conditions or tropical oceans)

### E/P Ratio
- **E/P < 0.5**: Humid regions (runoff generation)
- **E/P 0.5-1.0**: Semi-humid to semi-arid
- **E/P > 1.0**: Arid regions (moisture deficit)

## Evapotranspiration (ET) Components
Over vegetated land:
- **Transpiration**: 50-80% of total ET (varies by vegetation type)
- **Soil evaporation**: 20-40% of total ET
- **Interception**: 10-20% of precipitation in forests

Reference ET (grass): ~3-6 mm/day in mid-latitudes during growing season

## Climate Change Impacts
Observed and projected changes:
1. **Potential ET increase**: ~1-2% per °C warming (energy-limited)
2. **Actual ET trends**: More complex, depends on moisture availability
3. **Regional patterns**: Increases in humid tropics, decreases in dry subtropics
4. **Extreme events**: Heat waves increase evaporative demand
5. **Vegetation response**: CO₂ effects on stomatal conductance may reduce ET

## Measurement and Validation
Evaporation is challenging to measure:
- **Eddy covariance towers**: Direct flux measurements (point scale)
- **Pan evaporation**: Surrogate for potential evaporation
- **Lysimeters**: Weighing devices for ET measurement
- **Remote sensing**: Satellite-based ET estimates
- **Water balance**: Residual method (P - R - ΔS = E)

## References
1. Hersbach, H., et al. (2020). The ERA5 global reanalysis. *Quarterly Journal of the Royal Meteorological Society*, 146(730), 1999-2049.
2. Allen, R. G., et al. (1998). Crop evapotranspiration: Guidelines for computing crop water requirements. FAO Irrigation and Drainage Paper 56.
3. Trenberth, K. E., et al. (2007). Estimates of the global water budget and its annual cycle using observational and model data. *Journal of Hydrometeorology*, 8(4), 758-769.
4. Miralles, D. G., et al. (2011). Global land-surface evaporation estimated from satellite-based observations. *Hydrology and Earth System Sciences*, 15(2), 453-469.
