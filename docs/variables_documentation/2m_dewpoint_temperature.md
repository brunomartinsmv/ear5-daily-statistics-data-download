# 2-Metre Dewpoint Temperature

## Overview
The 2-metre dewpoint temperature is the temperature to which air must be cooled at constant pressure to reach saturation with respect to liquid water. This fundamental thermodynamic variable quantifies atmospheric moisture content and is essential for weather forecasting, human comfort assessment, and atmospheric boundary layer studies.

## Scientific Description
Dewpoint temperature (Td) is defined as the temperature at which the air's water vapor pressure equals the saturation vapor pressure. At this temperature, the relative humidity reaches 100%, and condensation begins to form (dew, fog, or clouds). The dewpoint is an absolute measure of atmospheric moisture content—unlike relative humidity, which depends on temperature.

In ERA5, the 2-metre dewpoint is diagnosed from:
1. **2-metre temperature**: Standard air temperature at 2m height
2. **Specific humidity**: Water vapor mixing ratio at 2m height
3. **Surface pressure**: For vapor pressure calculation

The dewpoint is computed using empirical formulations (e.g., Magnus or August-Roche-Magnus equations) that relate saturation vapor pressure to temperature. The diagnostic accounts for the phase of water (liquid vs. ice) depending on temperature range.

Key relationships:
- **Td < T** always (dewpoint cannot exceed air temperature)
- **Td = T** at saturation (RH = 100%)
- **T - Td** = dewpoint depression (inverse measure of relative humidity)

## Units
- **Standard Unit**: Kelvin (K)
- **Common Alternative**: Degrees Celsius (°C) - subtract 273.15 from Kelvin
- **Typical Range**: 
  - Arctic winter: 200-250 K (-73°C to -23°C)
  - Tropical: 290-300 K (17°C to 27°C)
  - Desert: Can be <250 K (<-23°C)
  - Humid tropics: Can reach 303 K (30°C)

## Applications in Climate Research

### Atmospheric Moisture Content
Dewpoint temperature is a direct measure of absolute humidity:
- Higher dewpoint = more atmospheric moisture
- Essential for quantifying moisture availability for precipitation
- Used to compute water vapor mass and precipitable water

### Human Thermal Comfort
Dewpoint is the preferred metric for assessing oppressive conditions:
- **Td < 10°C**: Dry, comfortable
- **Td 10-15°C**: Comfortable
- **Td 16-18°C**: Sticky, noticeable
- **Td 19-23°C**: Uncomfortable, muggy
- **Td > 24°C**: Oppressive, dangerous for outdoor activity

### Fog and Low Cloud Formation
Conditions for fog/low stratus formation:
- Small dewpoint depression (T - Td < 2°C) indicates high RH
- Nocturnal cooling can reach dewpoint, forming radiation fog
- Advection of moist air over cool surfaces creates advection fog

### Convective Potential Assessment
High surface dewpoint indicates:
- Large convective available potential energy (CAPE)
- Favorable conditions for severe thunderstorms
- Moisture availability for deep convection
- Flash flood potential

### Air Mass Classification
Dewpoint helps identify air mass characteristics:
- **Continental Polar**: Td < 0°C (dry, cold)
- **Maritime Tropical**: Td > 20°C (humid, warm)
- **Continental Tropical**: Td < 10°C, T high (hot, dry)

### Moisture Transport
Dewpoint patterns reveal:
- Advection of humid vs. dry air masses
- Low-level jets transporting moisture
- Atmospheric rivers and moisture corridors
- Drought vs. humid region boundaries

### Climate Change Impacts
Changes in dewpoint temperature indicate:
- Atmospheric moisture content trends (Clausius-Clapeyron relation: ~7% increase per °C warming)
- Heat stress risk evolution
- Shifting humid vs. arid climate zones

## Related Variables
- **2m_temperature**: Air temperature; together define relative humidity
- **total_precipitation**: Dewpoint indicates moisture available for precipitation
- **total_column_water_vapor**: Integrated atmospheric moisture
- **2m_relative_humidity**: Can be computed from T and Td
- **10m_u/v_component_of_wind**: Transport humid vs. dry air masses

## Mathematical Relationships
- **Relative Humidity**: RH ≈ 100 × exp(c(Td - T)/(T + a)) where c ≈ 17.27, a ≈ 237.7°C (Td, T in °C)
- **Mixing Ratio**: w = 0.622 × es(Td)/(P - es(Td)) where es is saturation vapor pressure, P is pressure
- **Vapor Pressure**: e = es(Td)
- **Specific Humidity**: q = w/(1 + w)
- **Dewpoint Depression**: D = T - Td

### Magnus Formula (approximate):
**es(T) = 6.112 × exp(17.67T/(T + 243.5))** (T in °C, es in hPa)

## Data Characteristics in ERA5 Daily Statistics
- **Temporal Resolution**: Daily statistics (mean, minimum, maximum, spread) from hourly values
- **Spatial Resolution**: ~0.25° × 0.25° (approximately 25-30 km)
- **Vertical Level**: 2 metres above surface (diagnostic level)
- **Availability**: 1940 to present

## Quality Considerations
- **Calculation method**: Dewpoint is diagnosed from humidity and temperature; accuracy depends on both
- **Saturation assumptions**: Computed with respect to liquid water above 0°C; ice below 0°C
- **Boundary layer processes**: Vertical mixing affects near-surface humidity
- **Data assimilation**: Humidity observations (radiosondes, surface stations) improve dewpoint quality
- **Coastal regions**: Sharp land-sea moisture gradients at scales finer than model resolution
- **Nocturnal inversions**: Decoupling between surface and 2m level can occur

## Physical Context
The dewpoint temperature is fundamentally tied to the Clausius-Clapeyron relation, which describes how saturation vapor pressure increases exponentially with temperature:

**des/dT = (L·es)/(Rv·T²)**

where:
- L = latent heat of vaporization (~2.5 × 10⁶ J kg⁻¹)
- Rv = gas constant for water vapor
- T = temperature

Key physical insights:
1. **Moisture capacity**: Warm air can hold more moisture than cold air
2. **Dewpoint depression**: Indicates distance from saturation
3. **Conservative property**: Dewpoint conserved during dry adiabatic processes (unlike RH)
4. **Evaporation/condensation**: Dewpoint increases with evaporation, decreases with precipitation

## Practical Interpretation
- **Dewpoint depression < 3°C**: Fog/low cloud likely with cooling
- **Dewpoint depression > 10°C**: Low relative humidity, dry conditions
- **Rising dewpoint**: Moisture advection or surface evaporation
- **Falling dewpoint**: Dry air advection or precipitation removing moisture

## References
1. Hersbach, H., et al. (2020). The ERA5 global reanalysis. *Quarterly Journal of the Royal Meteorological Society*, 146(730), 1999-2049.
2. Wallace, J. M., & Hobbs, P. V. (2006). *Atmospheric Science: An Introductory Survey* (2nd ed.). Academic Press.
3. WMO (2018). Guide to Meteorological Instruments and Methods of Observation (WMO-No. 8).
4. Bolton, D. (1980). The computation of equivalent potential temperature. *Monthly Weather Review*, 108(7), 1046-1053.
