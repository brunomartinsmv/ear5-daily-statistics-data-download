# 2-Metre Relative Humidity

## Overview
The 2-metre relative humidity is the ratio of the actual water vapor pressure to the saturation water vapor pressure at 2 metres above the surface, expressed as a percentage. This dimensionless variable quantifies how close the air is to saturation and is widely used in meteorology, human comfort assessment, and agricultural applications.

## Scientific Description
Relative humidity (RH) is defined as:

**RH = (e / es) × 100%**

where:
- e = actual water vapor pressure
- es = saturation water vapor pressure (function of temperature)

In ERA5, 2-metre relative humidity is diagnosed from:
1. **2-metre temperature** (T)
2. **2-metre dewpoint temperature** (Td)
3. **Surface pressure** (for accurate vapor pressure calculations)

The key characteristic of relative humidity is its strong dependence on temperature: even with constant moisture content, RH increases when temperature decreases and vice versa. This makes RH highly variable diurnally (high at night, low during day) and seasonally.

Alternative formulation using dewpoint:
**RH ≈ 100 × exp(L/Rv × (1/T - 1/Td))**

where L is latent heat of vaporization and Rv is the gas constant for water vapor.

## Units
- **Standard Unit**: Percent (%)
- **Alternative**: Ratio (0-1) - divide by 100
- **Range**: 0-100% by definition
- **Typical Values**:
  - Deserts: 10-30%
  - Temperate regions: 50-80%
  - Tropical rainforests: 80-95%
  - Fog conditions: ~100%

## Applications in Climate Research

### Human Thermal Comfort
RH is the standard metric for assessing comfort and heat stress:
- **RH < 30%**: Dry, potential for static electricity and respiratory discomfort
- **RH 30-60%**: Comfortable range for most people
- **RH > 70%**: Muggy, uncomfortable; impedes evaporative cooling
- Combined with temperature in heat index calculations

### Agricultural and Crop Science
Relative humidity affects:
- Evapotranspiration rates from crops and soil
- Disease pressure (fungal, bacterial pathogens thrive at high RH)
- Pest population dynamics
- Crop water stress indicators
- Optimal harvest timing

### Fire Weather
Low RH is critical for fire danger assessment:
- **RH < 30%**: Elevated fire risk
- **RH < 15%**: Critical fire weather conditions
- Combined with wind and temperature in fire weather indices

### Air Quality
Relative humidity influences:
- Aerosol hygroscopic growth
- Visibility reduction (haze formation)
- Chemical reaction rates in atmosphere
- Particulate matter concentrations

### Building and Materials
RH affects:
- Structural material moisture content
- Mold and mildew growth (typically >60% RH)
- Corrosion rates of metals
- Wood expansion/contraction

### Cloud and Fog Formation
Near-saturation conditions (RH approaching 100%):
- Indicate potential for fog formation when cooling occurs
- Cloud base estimation using surface RH
- Low-level cloud fraction correlation

## Related Variables
- **2m_temperature**: Temperature determines saturation vapor pressure
- **2m_dewpoint_temperature**: Alternative moisture measure; related by RH = f(T, Td)
- **total_precipitation**: High RH often precedes precipitation
- **total_cloud_cover**: Surface RH correlates with low cloud amount
- **10m_wind_speed**: Wind affects local moisture distribution

## Mathematical Relationships
- **RH from T and Td**: RH = 100 × exp(17.27 × Td/(237.3 + Td)) / exp(17.27 × T/(237.3 + T)) (T, Td in °C)
- **Vapor pressure**: e = es × (RH/100)
- **Mixing ratio**: w = 0.622 × RH × es/(P - RH × es) approximately
- **Specific humidity**: q ≈ 0.622 × RH × es/P for small q

### Magnus Formula for Saturation Vapor Pressure:
**es(T) = 6.112 × exp(17.67 × T/(T + 243.5))** hPa, T in °C

## Data Characteristics in ERA5 Daily Statistics
- **Temporal Resolution**: Daily statistics (mean, minimum, maximum, spread) from hourly values
- **Spatial Resolution**: ~0.25° × 0.25° (approximately 25-30 km)
- **Vertical Level**: 2 metres above surface (diagnostic)
- **Availability**: 1940 to present
- **Diurnal Variation**: Typically maximum at dawn (lowest T), minimum in afternoon (highest T)

## Quality Considerations
- **Temperature sensitivity**: Small errors in temperature produce large RH errors
- **Diagnostic variable**: Computed from other variables; inherits their uncertainties
- **Saturation assumptions**: Different formulations exist for liquid vs. ice saturation
- **Local heterogeneity**: RH can vary significantly at sub-grid scales
- **Coastal gradients**: Sharp RH transitions at land-sea boundaries
- **Nocturnal inversions**: Decoupling between surface and 2m level affects RH

## Physical Context
Relative humidity is not a conserved quantity during atmospheric motions:

### Diurnal Cycle
- **Early morning**: Maximum RH as temperature reaches minimum
- **Afternoon**: Minimum RH as temperature peaks
- **Night**: RH increases as temperature falls

### Adiabatic Processes
- **Ascending air**: RH increases (cooling reduces es)
- **Descending air**: RH decreases (warming increases es)
- **Unsaturated ascent**: Eventually reaches RH = 100% at lifted condensation level (LCL)

### Moisture Addition/Removal
- **Evaporation**: Increases RH
- **Precipitation**: Initially increases RH, but removal of vapor can decrease RH
- **Advection**: Transport of dry/moist air masses changes RH

## Practical Interpretation
- **RH > 95%**: Fog/low cloud likely with any cooling
- **RH < 20%**: Very dry; increased fire danger, evapotranspiration stress
- **High RH + high T**: Heat stress risk (reduced evaporative cooling effectiveness)
- **Low RH + high T**: Increased evaporative demand, drought stress

### Dewpoint vs. Relative Humidity
While related, these measure different aspects of moisture:
- **Dewpoint**: Absolute moisture content (conserved in dry processes)
- **Relative Humidity**: How close to saturation (not conserved)

Example: Air with Td = 15°C
- At T = 15°C: RH = 100%
- At T = 20°C: RH = 68%
- At T = 25°C: RH = 48%

Same moisture, but RH changes dramatically with temperature.

## Climate Change Context
In a warming climate:
- Absolute humidity (dewpoint) is generally increasing (~7% per °C from Clausius-Clapeyron)
- Relative humidity trends are more complex and region-dependent
- Over land: Many regions show decreasing RH due to soil moisture feedbacks
- Over ocean: RH tends to remain relatively constant

## References
1. Hersbach, H., et al. (2020). The ERA5 global reanalysis. *Quarterly Journal of the Royal Meteorological Society*, 146(730), 1999-2049.
2. Bolton, D. (1980). The computation of equivalent potential temperature. *Monthly Weather Review*, 108(7), 1046-1053.
3. Willett, K. M., et al. (2014). HadISDH land surface multi-variable humidity and temperature record for climate monitoring. *Climate of the Past*, 10(6), 1983-2006.
4. Lawrence, M. G. (2005). The relationship between relative humidity and the dewpoint temperature in moist air. *Bulletin of the American Meteorological Society*, 86(2), 225-233.
