# 2-Metre Temperature

## Overview
The 2-metre temperature represents the air temperature at a height of 2 metres above the Earth's surface. This variable is one of the most fundamental meteorological parameters in atmospheric science and climate research, serving as a primary indicator of surface thermal conditions.

## Scientific Description
This parameter represents the instantaneous temperature of the air at 2 metres above the ground surface, which is the standard meteorological measurement height established by the World Meteorological Organization (WMO). The measurement height is chosen to minimize the influence of surface heterogeneity while remaining close enough to be representative of human-scale environmental conditions.

The 2-metre temperature is computed in the ERA5 reanalysis using the surface energy balance and vertical temperature profile from the atmospheric model, employing similarity theory to extrapolate from the lowest model level to the 2-metre height. This extrapolation accounts for surface roughness, stability conditions, and sensible heat flux.

## Units
- **Standard Unit**: Kelvin (K)
- **Common Alternative**: Degrees Celsius (°C) - subtract 273.15 from Kelvin
- **Range**: Typically 200-330 K (-73°C to 57°C) for terrestrial observations

## Applications in Climate Research

### Climate Change Analysis
The 2-metre temperature is the primary variable used to quantify global warming trends and regional climate change patterns. It is central to computing temperature anomalies, trend analysis, and climate model validation.

### Heat Wave Detection
Daily maximum 2-metre temperatures are used to identify extreme heat events, which have significant implications for public health, agriculture, and energy demand.

### Agricultural Modeling
Growing degree days, frost events, and thermal time calculations for crop phenology all depend on accurate 2-metre temperature data.

### Urban Climate Studies
The parameter is essential for studying urban heat island effects and assessing thermal comfort in urban planning contexts.

### Energy Demand Forecasting
Heating and cooling degree days calculated from 2-metre temperature are crucial for energy consumption modeling and infrastructure planning.

## Related Variables
- **2m_dewpoint_temperature**: Used together to calculate relative humidity and atmospheric moisture content
- **2m_maximum_temperature** / **2m_minimum_temperature**: Derived statistics showing diurnal temperature range
- **surface_temperature**: Surface skin temperature, which differs from air temperature

## Data Characteristics in ERA5 Daily Statistics
- **Temporal Resolution**: Daily statistics (mean, minimum, maximum, spread) computed from hourly data
- **Spatial Resolution**: ~0.25° × 0.25° (approximately 25-30 km)
- **Vertical Level**: 2 metres above surface (diagnostic level)
- **Availability**: 1940 to present

## Quality Considerations
- Reanalysis temperatures show improved skill over regions with dense observation networks
- Greater uncertainty exists in data-sparse regions (e.g., polar areas, remote oceans)
- Urban areas may exhibit biases due to unresolved microscale heterogeneity
- High-elevation terrain requires careful interpretation due to model resolution limitations

## References
1. Hersbach, H., et al. (2020). The ERA5 global reanalysis. *Quarterly Journal of the Royal Meteorological Society*, 146(730), 1999-2049.
2. WMO (2018). Guide to Meteorological Instruments and Methods of Observation (WMO-No. 8).
3. IPCC (2021). Climate Change 2021: The Physical Science Basis. Contribution of Working Group I to the Sixth Assessment Report.
